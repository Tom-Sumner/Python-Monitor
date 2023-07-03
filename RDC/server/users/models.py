from django.db import models

class Person(models.Model):
    name = models.TextField(max_length=20)
    email = models.EmailField()