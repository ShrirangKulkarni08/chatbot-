import random
from flask import Flask, request, jsonify, send_from_directory

app = Flask(__name__, static_folder="static")


def chatbot_response(user_choice):
    user_choice = user_choice.lower()

    if "hello" in user_choice or "hi" in user_choice:
        return "Hello! How can I help you today?"

    elif "how are you" in user_choice:
        return "I'm doing great. Thank you for asking!"

    elif "your name" in user_choice:
        return "My name is ChatBot."

    elif "joke" in user_choice:
        jokes = [
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fake noodle? An impasta!"
        ]
        return random.choice(jokes)

    elif "bye" in user_choice:
        return "Goodbye! Have a great day!"

    else:
        return "Sorry, I didn't understand that."


@app.route("/")
def index():
    return send_from_directory("static", "index.html")


@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json(silent=True) or {}
    user_message = data.get("message", "")
    reply = chatbot_response(user_message)
    return jsonify({"reply": reply})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
