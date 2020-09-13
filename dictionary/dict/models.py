from django.db import models

# Create your models here.

class Word(models.Model):
    
    term = models.CharField(max_length=100, default=None)
    translated = models.CharField(max_length=100,default=None)
    acronym = models.CharField(max_length=20, default=None, blank=True)
    note = models.TextField(max_length=500, blank=True)

    def  __str__(self):
       return self.term
