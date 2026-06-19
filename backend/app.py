from flask import Flask, request, jsonify
from flask_cors import CORS
from model import get_response

app = Flask(__name__)
CORS(app)

def log_chat(user, bot):
    with open("chat_logs.txt", "a") as f:
        f.write(f"{user} -> {bot}\n")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json["message"]

    bot_response = get_response(user_input)

    if not bot_response:
        bot_response = "Sorry, I don't understand. Please contact support."

    log_chat(user_input, bot_response)

    return jsonify({"response": bot_response})

if __name__ == "__main__":
    app.run(debug=True)