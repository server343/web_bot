document.getElementById('send-button').addEventListener('click', function() {
    const userInput = document.getElementById('user-input');
    const message = userInput.value.trim();
    if (message) {
        appendMessage('Tú', message);
        sendMessageToServer(message);
        userInput.value = '';
    }
});

function appendMessage(sender, message) {
    const messageContainer = document.getElementById('messages');
    const messageDiv = document.createElement('div');
    messageDiv.textContent = `${sender}: ${message}`;
    messageContainer.appendChild(messageDiv);
}

function sendMessageToServer(message) {
    fetch('/send_message', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage('Chatbot', data.reply);
    })
    .catch(error => {
        console.error('Error al enviar el mensaje:', error);
    });
}

