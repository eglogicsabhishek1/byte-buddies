from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('prescriptions/', views.prescriptions_list, name='prescriptions_list'),
    path('prescriptions/add/', views.add_prescription, name='add_prescription'),
    path('chat/', views.chat, name='chat'),
    path('chatbot/', views.chatbot_view, name='chatbot_view'),


]

