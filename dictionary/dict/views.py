from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.generic import ListView
from dict.models import Word
from dict.forms import WordForm

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

def addWord(request):

    form = WordForm()
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/dict')

    context = {"form":form}
    return render(request, 'dictionary/add_word.html', context)

def updateWord(request, pk):

    word = Word.objects.get(id=pk)
    form = WordForm(instance=word)

    if request.method == 'POST':
        form = WordForm(request.POST ,instance=word)
        if form.is_valid():
            form.save()
            return redirect('/dict')

    context = {'form':form}
    return render(request, 'dictionary/update_word.html', context)

def deleteWord(request, pk):
    word = Word.objects.get(id=pk)
    if request.method =="POST":
        word.delete()
        return redirect('/dict')
    context={'word':word}
    return render(request, 'dictionary/delete_word.html', context)
