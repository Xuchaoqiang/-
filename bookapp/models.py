from django.db import models

# Create your models here.

class Books(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=20)
    pub_date = models.DateField()
    press = models.CharFie ld(max_length=20)