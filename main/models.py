from django.db import models

class Profile(models.Model):
    image = models.ImageField()
    name = models.CharField(max_length=20)
