from django.db import models

# Create your models here.

class word(models.Model):
    term = models.CharField(max_length=30, default=None)
    translated = models.CharField(max_length=30,default=None)
    acronym = models.CharField(max_length=20, default=None, blank=True)
    note = models.TextField(max_length=500, blank=True)

    def  __str__(self):
       return self.term
