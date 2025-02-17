import os
import json
import random
import nltk
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Prescription
from .forms import PrescriptionForm
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Download necessary NLTK resources
nltk.download("punkt")

# Get the path to the intents.json file in your Django app
BASE_DIR = os.path.dirname(os.path.abspath(__file__))  # Get the root of your app
INTENTS_FILE = os.path.join(BASE_DIR, 'chatbot_data', 'intents.json')  # Adjust the path to your file

# Load intents from JSON
try:
    with open(INTENTS_FILE, "r", encoding="utf-8") as file:
        data = json.load(file)
except FileNotFoundError:
    raise FileNotFoundError(f"Could not find intents.json at {INTENTS_FILE}")

# Extract training data from intents
patterns = []
tags = []
responses = {}
intents = data

for intent in intents["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

# Convert text to vector representation
vectorizer = TfidfVectorizer(stop_words="english")
X = vectorizer.fit_transform(patterns)

def get_response(user_input):
    """Match user input with the best intent using cosine similarity."""
    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, X)
    best_match = similarities.argmax()

    if similarities[0, best_match] > 0.2:  # Confidence threshold
        tag = tags[best_match]
        return random.choice(responses[tag])

    return "I'm sorry, I don't understand."


# Standard views
def homepage(request):
    return render(request, 'cms/home.html')

def about(request):
    return render(request, 'cms/about.html')

def contact(request):
    return render(request, 'cms/contact.html')

def prescriptions_list(request):
    prescriptions = Prescription.objects.all()
    return render(request, 'cms/prescriptions_list.html', {'prescriptions': prescriptions})

def add_prescription(request):
    if request.method == 'POST':
        form = PrescriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('prescriptions_list')
    else:
        form = PrescriptionForm()
    return render(request, 'cms/add_prescription.html', {'form': form})


# Chatbot views
def chatbot_view(request):
    """Render the chatbot page."""
    return render(request, 'cms/chatbot.html')  # Ensure this template exists

@csrf_exempt
def chat(request):
    """Handle the chatbot response in Django."""
    if request.method == "POST":
        user_message = json.loads(request.body).get("message")
        response = get_response(user_message)
        return JsonResponse({"response": response})
    return JsonResponse({"response": "Invalid request method"}, status=400)
