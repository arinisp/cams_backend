from django.db import models

JENIS_KELAMIN = (
    ('L', 'Laki-Laki'),
    ('P', 'Perempuan')
)

OCCUPATION = (
    ('n', 'Non-Fix'),
    ('f', 'Fix')
)

# Create your models here.
class Customer (models.Model):
    name = models.fields.CharField(max_length=255)
    jenis_kelamin = models.fields.CharField(max_length=1, choices=JENIS_KELAMIN, default='L')
    total_income = models.fields.FloatField()
    existing = models.fields.BooleanField()
    occupation = models.fields.CharField(max_length=1, choices=OCCUPATION, default='n')
    alamat = models.fields.TextField()

    def __str__(self):
        return self.name
    def __repr__(self):
        return self.name

