from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
import pandas as pd
from .search_frequency import start, analyze
from textanalysis.models import WordCountUrl
from textanalysis.forms import WordCountUrlForm

# Create your views here.

def index_analysis(request):
    form = WordCountUrlForm()
    wordcount = WordCountUrl.objects.all()
    return render(request, 'index_analysis.html', {"form": form, "wordcount": wordcount})

def getSearchResults(request):
    removepunc =  request.GET.get('removepunc','off')
    fullcaps = request.GET.get('fullcapitalize','off')
    newline = request.GET.get('newlineremove','off')
    spaceremove = request.GET.get('spaceremove','off')
    charcount = request.GET.get('charcount','off')
    query = request.GET.get('term')
    if WordCountUrl.objects.filter(url=WordCountUrl.url).exists():
        return JsonResponse({'Search_Result': WordCountUrl.objects.get('url')})
    else:
        searchResult,clean_list = start(query)
        result = analyze(clean_list, removepunc, fullcaps, newline, spaceremove, charcount)
        if removepunc == 'on' or fullcaps == 'on' or newline == 'on' or spaceremove == 'on' or charcount == 'on':
            return (render(request, 'analysis.html', result))
        #else:
        #    return HttpResponse('Please select the analysis for text entered!!!')
    