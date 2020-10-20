from django.db import models
from datetime import datetime
from django import forms

class Contact(models.Model):
    name= models.CharField(max_length=30)
    email = models.EmailField()
    mobile = models.CharField(max_length=10)
    subject = models.TextField(max_length=100)
    message = models.TextField(max_length=500)
    timing = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.name