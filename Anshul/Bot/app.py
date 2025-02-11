from flask import Flask, request, jsonify
from chat_bot import chatbot_response  # Import chatbot function

app = Flask(__name__)

# Default route to check if API is running
@app.route("/")
def home():
    return "Chatbot API is running. Use /chatbot for interaction."

# Chatbot API route
@app.route("/chatbot", methods=["POST"])
def chatbot():
    data = request.get_json()
    user_message = data.get("message", "")

    bot_reply = chatbot_response(user_message)  # Call chatbot function
    return jsonify({"response": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
