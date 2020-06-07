from django.shortcuts import render

def indexpage(request):
    context = {}
    return render(request, 'polls/index.html', context)

def create(request):
    context = {}
    return render(request, 'polls/create.html', context)

def vote(request):
    context = {}
    return render(request, 'polls/vote.html', context)

def result(request):
    context = {}
    return render(request, 'polls/result.html', context)