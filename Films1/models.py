from django.db import models

# Create your models here.
class film(models.Model):
    release_date=models.DateField()
    film_name=models.CharField(max_length=50)
    description=models.CharField(max_length=255)
class actor(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birthday=models.DateField()
    film=models.ManyToManyField(to=film)
class director(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    birthday=models.DateField()
    film=models.ManyToManyField(to=film)
