from django.db import models

class Prescription(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    dosage = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
