from flask import Flask, request, jsonify
import openai

app = Flask(__name__)

# Reemplaza 'tu-clave-api' con tu clave de API de OpenAI
openai.api_key = 'tu-clave-api'

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Chatbot</title>
    <style>
        /* Estilos del chatbot */
        body {
            font-family: 'Arial', sans-serif;
            margin: 0;
            padding: 0;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #eaeaea;
        }
        #chat-container {
            width: 400px;
            height: 600px;
            box-shadow: 0 0 10px 0 rgba(0,0,0,0.2);
            border-radius: 8px;
            overflow: hidden;
            background: white;
        }
        #messages {
            height: 550px;
            overflow-y: auto;
            padding: 10px;
        }
        .message {
            background: #f1f1f1;
            padding: 10px 15px;
            margin: 5px;
            border-radius: 10px;
            width: fit-content;
        }
        .user {
            background: #007bff;
            color: white;
            margin-left: auto;
        }
        #input-box {
            display: flex;
            padding: 5px;
        }
        #user-input {
            flex: 1;
            padding: 10px;
            border: none;
            border-radius: 4px;
            margin-right: 5px;
        }
        #send-button {
            padding: 10px 15px;
            border: none;
            border-radius: 4px;
            background: #007bff;
            color: white;
            cursor: pointer;
        }
        #send-button:hover {
            background: #0056b3;
        }
    </style>
</head>
<body>
    <div id="chat-container">
        <div id="messages"></div>
        <div id="input-box">
            <input type="text" id="user-input" placeholder="Escribe un mensaje...">
            <button id="send-button">Enviar</button>
        </div>
    </div>
    <script>
        document.getElementById('send-button').onclick = function() {
            var userInput = document.getElementById('user-input');
            var message = userInput.value.trim();
            if (message) {
                addMessage('user', message);
                sendMessageToServer(message);
                userInput.value = '';
            }
        };

        function addMessage(sender, message) {
            var messagesContainer = document.getElementById('messages');
            var messageDiv = document.createElement('div');
            messageDiv.classList.add('message', sender === 'user' ? 'user' : 'bot');
            messageDiv.textContent = message;
            messagesContainer.appendChild(messageDiv);
            messagesContainer.scrollTop = messagesContainer.scrollHeight;
        }

        function sendMessageToServer(message) {
            fetch('/send_message', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ message: message }),
            })
            .then(response => response.json())
            .then(data => {
                addMessage('bot', data.reply);
            });
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return html

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data['message']
    
    # Llamada a la API de OpenAI
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=user_message,
        max_tokens=150
    )
    bot_reply = response.choices[0].text.strip()

    return jsonify({'reply': bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
