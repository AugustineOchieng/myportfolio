from django.db import models

# Create your models here.
class Project(models.Model):
  name = models.CharField(max_length=500)
  description = models.TextField(max_length=100)
  link = models.CharField(max_length=500)

class Education(models.Model):
  level = models.CharField(max_length=500)
  place = models.TextField(max_length=100)
  details = models.TextField(max_length=100)
  start = models.DateTimeField(auto_now_add=True)
  end = models.DateTimeField(auto_now_add=True)