from django.shortcuts import render,redirect
from .models import Prescription

from .forms import PrescriptionForm

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

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from finalbot.chatbot import get_response  # Import chatbot function

@csrf_exempt  # Disable CSRF protection for simplicity (secure it later)
def chatbot(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)  # Get user message
            user_message = data.get("message", "")
            if not user_message:
                return JsonResponse({"error": "Empty message"}, status=400)

            bot_response = get_response(user_message)  # Process with chatbot
            return JsonResponse({"response": bot_response})
        except json.JSONDecodeError:
            return JsonResponse({"error": "Invalid JSON"}, status=400)
    return JsonResponse({"error": "Invalid request"}, status=405)


