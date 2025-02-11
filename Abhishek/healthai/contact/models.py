from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from django import forms
from wagtail.forms import AbstractEmailForm
from django.db import models

class ContactPage(AbstractEmailForm):
    body = models.TextField()

    content_panels = AbstractEmailForm.content_panels + [
        FieldPanel('body'),
    ]
