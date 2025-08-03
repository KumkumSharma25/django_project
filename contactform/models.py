from django.db import models

class Contactform (models.Model):
    fullname=models.CharField( max_length=150)
    email=models.CharField( max_length=150)
    subject=models.CharField( max_length=150)
    message=models.TextField()