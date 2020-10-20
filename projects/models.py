from django.db import models
from datetime import datetime

class Project(models.Model):
    id = models.IntegerField(blank=True, primary_key=True)
    title = models.CharField(max_length=40)
    image = models.ImageField(upload_to="%d%m%y")
    description = models.TextField(max_length=250)
    link = models.URLField(blank=True)
    date = models.DateTimeField(default=datetime.now())
    def __str__(self):
        return self.title

