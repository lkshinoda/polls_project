from django.shortcuts import render

def home(request):
    context = {}
    return render(request, 'polls/index.html', context)