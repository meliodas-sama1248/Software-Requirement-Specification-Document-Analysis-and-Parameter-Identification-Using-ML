function submitQuery() {
    const inputText = document.getElementById('input-text');
    const query = inputText.value.trim();
    if (!query) return;

    inputText.value = '';
    addChat(query, 'user');

    fetch('/submit', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/x-www-form-urlencoded',
        },
        body: 'query=' + encodeURIComponent(query)
    })
    .then(response => response.json())
    .then(data => {
        addChat(data.response, 'bot');
    })
    .catch(error => console.error('Error:', error));
}

function addChat(message, sender) {
    const chatHistory = document.getElementById('chat-history');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = message;
    messageDiv.className = sender;
    chatHistory.appendChild(messageDiv);
    chatHistory.scrollTop = chatHistory.scrollHeight;
}

function handleKeyPress(event) {
    if (event.key === 'Enter' && !event.shiftKey) {
        event.preventDefault();
        submitQuery();
    }
}
