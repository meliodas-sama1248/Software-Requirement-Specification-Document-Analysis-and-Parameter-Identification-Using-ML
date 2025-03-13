from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
import os
from PIL import Image
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS

# Set environment variables
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ["GOOGLE_API_KEY"] = "Your_API_Key"

# Initialize Flask application
app = Flask(__name__)

# Configure session to use filesystem (server-side session management)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your_secret_key_here'
Session(app)

def load_pdf_and_index():
    pdf_folder = "pdf"
    pdf_files = [f for f in os.listdir(pdf_folder) if f.endswith('.pdf')]
    all_pages = []
    for pdf_file in pdf_files:
        file_path = os.path.join(pdf_folder, pdf_file)
        loader = PyPDFLoader(file_path)
        pages = loader.load_and_split()
        all_pages.extend(pages)
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    db = FAISS.from_documents(all_pages, embeddings)
    return db

db = load_pdf_and_index()

@app.route('/')
def index():
    # Initialize chat history in session
    if 'history' not in session:
        session['history'] = []
        welcome_message = "SRS Bot: Hello! I am your assistant. How may I help you today?"
        session['history'].append({'message': welcome_message, 'sender': 'bot'})
    return render_template('index.html', history=session['history'])

@app.route('/submit', methods=['POST'])
def on_submit():
    query = request.form['query']
    session.setdefault('history', []).append({'message': query, 'sender': 'user'})
    
    content = retrieve_content(db, query)
    response = generate_response(content, query)
    response_message = f"Assistant Response: {response}"
    session['history'].append({'message': response_message, 'sender': 'bot'})
    
    return jsonify({'query': query, 'response': response_message})

def retrieve_content(db, query):
    docs = db.similarity_search(query)
    return "\n".join([x.page_content for x in docs])

def generate_response(content, query):
    qa_prompt = "Use the following pieces of context to answer the user's question. If you don't know the answer, just say that you don't know, don't try to make up an answer.----------------"
    input_text = f"{qa_prompt}\nContext:{content}\nUser question:\n{query}"
    llm = ChatGoogleGenerativeAI(model="gemini-pro")
    result = llm.invoke(input_text)
    return result.content

if __name__ == '__main__':
    app.run(debug=True)
