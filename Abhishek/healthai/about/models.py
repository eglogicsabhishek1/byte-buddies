from wagtail.models import Page
from wagtail.admin.edit_handlers import FieldPanel
from django.db import models

class AboutPage(Page):
    description = models.TextField()

    content_panels = Page.content_panels + [
        FieldPanel('description'),
    ]
