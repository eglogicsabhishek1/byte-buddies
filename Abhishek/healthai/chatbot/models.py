from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from django.db import models

class ChatbotPage(Page):
    # Add fields if necessary for chatbot (we'll add a simple form for data collection)
    chatbot_form_data = models.CharField(max_length=100)

    content_panels = Page.content_panels + [
        FieldPanel('chatbot_form_data'),
    ]
