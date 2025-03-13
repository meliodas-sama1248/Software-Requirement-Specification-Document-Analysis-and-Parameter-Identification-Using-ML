# 📄 Software Requirement Specification Document Analysis and Parameter Identification Using Machine Learning

This project aims to enhance software development efficiency and reduce manual errors by automating the analysis of Software Requirement Specification (SRS) documents using machine learning techniques.

---

## 🎯 Project Objective

Manual analysis of SRS documents is time-consuming and error-prone. This study introduces a machine learning-based solution to automatically classify requirement sentences from SRS documents into predefined parameters such as *Availability, **Pricing Models*, and more.

---

## 🗂 Dataset Overview

- *Total Records:* 94  
- *Data Format:* Sentence (Requirement) + Corresponding Parameter  
- *Preprocessing:*
  - Removed missing values
  - Label Encoding for target parameters
  - Train-test split (80:20)

---

## ⚙ Machine Learning Pipeline

- *Text Vectorization:* TF-IDF (Term Frequency - Inverse Document Frequency)
- *Classifier:* Support Vector Machine (SVM)
- *Performance Evaluation:*
  - Accuracy
  - Precision
  - Recall
  - F1-Score
  - Confusion Matrix

The trained model and label encoder were saved using joblib for easy reusability.

---

## 📥 PDF Text Extraction

- Implemented PDF parsing using *PyMuPDF (fitz)* to extract text directly from uploaded SRS documents.
- Sentences are then classified into corresponding parameters using the trained ML model.

---

## 🤖 Chatbot Integration

To enhance user interaction and assistance:
- A *Flask-based chatbot* was integrated.
- Used *LangChain* for response generation and clarification support on the extracted and classified parameters.

---

## 💻 Tech Stack

- Python (scikit-learn, pandas, numpy)
- Flask (Web Framework)
- PyMuPDF (PDF Text Extraction)
- TF-IDF Vectorizer
- SVM Classifier
- LangChain (Conversational AI)
- HTML/CSS (Frontend Interface)

---

## 📊 Output
Real-time classification of requirements from uploaded PDFs
Chatbot-based explanation of classified parameters
Model performance summary (accuracy, confusion matrix, etc.)

---
## 📌 Conclusion
This project demonstrates a powerful approach to automate SRS document analysis using machine learning. It reduces manual work, increases accuracy, and helps developers gain quicker insights into requirement parameters, making the software development process more efficient and intelligent.

---

## 🙌 Acknowledgements
Python & Open-source Community
scikit-learn, PyMuPDF, LangChain, Flask

---

🔗 Let’s Automate the Boring Stuff — One Requirement at a Time!


## 📜 License
This project is licensed under the [MIT License](./LICENSE).

----
