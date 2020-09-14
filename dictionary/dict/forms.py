from django.forms import ModelForm
from .models import Word
from django import forms

class WordForm(ModelForm):
    class Meta:
        model = Word
        fields = '__all__'

    widgets = {
        'term': forms.TextInput(attrs={'class': 'form-control'}),
        'translated': forms.TextInput(attrs={'class': 'form-control'}),
        'acronym': forms.Select(attrs={'class': 'form-control'}),
        'note': forms.Textarea(attrs={'class': 'form-control'}),
    }
