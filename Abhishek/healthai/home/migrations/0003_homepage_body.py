# Generated by Django 5.1.6 on 2025-02-11 12:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_create_homepage'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepage',
            name='body',
            field=models.TextField(blank=True),
        ),
    ]
