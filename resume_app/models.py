# resume_app/models.py

from django.db import models

class Summary(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    address = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()

class Education(models.Model):
    title = models.CharField(max_length=100)
    period = models.CharField(max_length=50)
    institution = models.CharField(max_length=255)
    description = models.TextField()

class Certification(models.Model):
    title = models.CharField(max_length=100)
    year = models.CharField(max_length=10)
    description = models.TextField()

class Project(models.Model):
    name = models.CharField(max_length=100)
    duration = models.CharField(max_length=50)
    description = models.TextField()
