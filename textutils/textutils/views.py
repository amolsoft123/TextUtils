from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def analyze(request):
    djtext = request.GET.get('text', 'default')
    removepunc=request.GET.get('removepunc', 'off')
    fullcaps=request.GET.get('fullcaps', 'off')
    lowercaps=request.GET.get('lowercaps', 'off')
    #analyzed = djtext

    if removepunc == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose':"Removing Punctuations", 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        params = {'purpose':"Change To Uppercase", 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)

    elif(lowercaps=="on"):
        analyzed= ""
        for char in djtext:
            analyzed = analyzed + char.lower()
        params = {'purpose':"Change To Lowercase", 'analyzed_text':analyzed}
        return render(request, 'analyze.html', params)


    else:
        return HttpResponse('Error')