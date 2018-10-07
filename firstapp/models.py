from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=500)
    blog = models.CharField(max_length=2000)
    date = models.DateField()
