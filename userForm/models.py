from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=20)
    username = models.CharField(max_length=15)
    email = models.EmailField()
    text = models.CharField(max_length=300)

    def __str__(self):
        return self.email