from django.db import models

# Create your models here.
class Customer (models.Model):
    name = models.fields.CharField(max_length=255)

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name
