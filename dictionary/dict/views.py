from django.shortcuts import render
from django.http import JsonResponse
from django.views.generic import ListView
from dict.models import Word

def index(request):

    if 'term' in request.GET:
        qs = Word.objects.filter(term__icontains=request.GET.get('term'))
        search_list = list()
        for word in qs:
            search_list.append(word.term)
        return JsonResponse(search_list, safe=False)

    if request.method =='GET':
        search_word = request.GET.get('searchbar','')
        word_list = Word.objects.order_by('term')
        translated_word = Word.objects.filter(term__icontains=search_word).order_by('term')

        context = {"translated_word" : translated_word, "word_list" : word_list}
        return render(request, 'dictionary/main.html', context)
