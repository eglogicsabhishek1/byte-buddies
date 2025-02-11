import random
import re

responses = {
    "hello": ["Hi! How can I assist you today?", "Hello! How are you feeling today?"],
    "symptoms": ["Can you describe your symptoms in detail?", "Tell me more about your health issue."],
    "fever": ["It sounds like you have a fever. You should rest and stay hydrated."],
    "blood pressure": ["Your blood pressure is {value}. If it's too high or too low, consider consulting a doctor."],
    "healthy": ["Maintain a balanced diet, exercise regularly, and get enough sleep."],  # ✅ Add this!
    "bye": ["Goodbye! Stay healthy!", "Take care!"]
}

def chatbot_response(user_input):
    user_input = user_input.lower()
    
    # Check for blood pressure format (e.g., "BP is 140/90")
    if "blood pressure" in user_input or "bp" in user_input:
        bp_value = ''.join(filter(lambda x: x.isdigit() or x == '/', user_input))
        return f"Your blood pressure is {bp_value}. If it's too high or too low, consider consulting a doctor."
    
    # General intent matching
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I'm not sure, but you should consult a doctor."


    for key in responses:
        if key in user_input:
            return random.choice(responses[key])

    return "I'm not sure, but you should consult a doctor."

# Testing
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        print("Bot:", chatbot_response(user_input))
