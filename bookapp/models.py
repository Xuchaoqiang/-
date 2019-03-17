from django.db import models
# Create your models here.

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=32)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    pub_date = models.DateField()
    publish = models.ForeignKey(to="Publish", on_delete=models.CASCADE)
    authors = models.ManyToManyField(to="Author")

class Author(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32, default='alex')
    birthday = models.DateField()
    telephone = models.BigIntegerField()
    addr = models.CharField(max_length=32)

class Publish(models.Model):
    nid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    city = models.CharField(max_length=32)

