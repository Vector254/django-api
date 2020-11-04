from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=155)
    link = models.URLField(max_length=255)
    description = models.TextField(max_length=255)
   # image = models.ImageField(upload_to = 'images/')
    user = models.ForeignKey(User, on_delete=models.CASCADE,null='True', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'{self.title}'
