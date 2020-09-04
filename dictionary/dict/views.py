from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from dict.models import Word

def index(request):

    if 'term' in request.GET:
        qs = Word.objects.filter(term__icontains=request.GET.get('term'))
        word_list = list()
        for word in qs:
            word_list.append(word.term)
        return JsonResponse(word_list, safe=False)

    if request.method =='GET':
        search_word = request.GET.get('searchbar')
        translated_word = Word.objects.filter(term=search_word)
        word_list = Word.objects.all()
        context = {"word_list" : word_list}

        context = {"translated_word" : translated_word, "word_list" : word_list}
        return render(request, 'dictionary/main.html', context)
 
