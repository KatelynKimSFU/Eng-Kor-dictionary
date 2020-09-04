from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from dict.models import Word

def index(request):

    if 'term' in request.GET:
        qs = Word.objects.filter(term__istartswith=request.GET.get('term'))
        word_list = list()
        for word in qs:
            word_list.append(word.term)
        return JsonResponse(word_list, safe=False)
    return render(request, 'dictionary/main.html')
