from flask import Flask, render_template, request, jsonify
import openai
import os

app = Flask(__name__)

# Configura tu clave API de OpenAI
openai.api_key = os.getenv("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")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    data = request.json
    user_message = data['message']

    response = openai.Completion.create(
      engine="text-davinci-003",
      prompt=user_message,
      max_tokens=150
    )

    return jsonify({'reply': response.choices[0].text.strip()})

if __name__ == '__main__':
    app.run(debug=True)
