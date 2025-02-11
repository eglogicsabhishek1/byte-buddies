import random

responses = {
    "hello": ["Hi! How can I assist you today?", "Hello! How are you feeling today?"],
    "symptoms": ["Can you describe your symptoms in detail?", "Tell me more about your health issue."],
    "fever": ["It sounds like you have a fever. You should rest and stay hydrated."],
    "bye": ["Goodbye! Stay healthy!", "Take care!"],
    "blood pressure": ["Your blood pressure is {value}. If it's too high or too low, consider consulting a doctor."]
}

def chatbot_response(user_input):
    user_input = user_input.lower()

    # Extract BP value (if mentioned)
    if "blood pressure" in user_input or "bp" in user_input:
        words = user_input.split()
        for word in words:
            if "/" in word and word.replace("/", "").isdigit():
                return responses["blood pressure"][0].format(value=word)

    # General responses
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I'm not sure, but you should consult a doctor."

# Only run this when executing train_chatbot.py directly
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", chatbot_response(user_input))
