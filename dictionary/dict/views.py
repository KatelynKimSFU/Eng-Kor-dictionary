from django.shortcuts import render

from django.views.generic import ListView
from dict.models import word

def index(request):
    word_list = word.objects.all()
    context = {'word_list': word_list}
    return render(request, 'dictionary/main.html', context)
