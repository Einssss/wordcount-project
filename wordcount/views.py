from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, 'home.html',)


def count(request):
    fulltext = request.GET['fulltext']
    wordlist = fulltext.split()
    worddic = {}
    for word in wordlist:
        if word in worddic:
            worddic[word] += 1
        else:
            worddic[word] = 1
    return render(request, 'count.html', {'fulltext': fulltext, 'worddic': worddic.items(), 'count': len(wordlist)})


def about(request):
    return render(request, 'about.html')