from django.db import models

# Create your models here.

class wordKorean(models.Model):
    term = models.CharField(max_length=30)
    acronym = models.CharField(max_length=20, default=None)
    note = models.TextField(max_length=500)
    VERB = 'V'
    NOUN = 'N'
    ADJECTIVE = 'ADJ'
    TYPE_CHOICES = [
        (VERB, 'Verb'),
        (NOUN, 'Noun'),
        (ADJECTIVE, 'Adjective'),
    ]

class wordEnglish(models.Model):
    wordkorean = models.OneToOneField(
        wordKorean,
        on_delete = models.CASCADE,
        primary_key = True,
    )
    term = models.CharField(max_length=30)
    acronym = models.CharField(max_length=20, default=None)
    note = models.TextField(max_length=500)
    VERB = 'V'
    NOUN = 'N'
    ADJECTIVE = 'ADJ'
    TYPE_CHOICES = [
        (VERB, 'Verb'),
        (NOUN, 'Noun'),
        (ADJECTIVE, 'Adjective'),
    ]
