from django.shortcuts import render, redirect
from polls.forms import CreateQuestion
from polls.models import Question, Poll, Test


def indexpage(request):
    questions = Question.objects.all()
    context = {'questions': questions}
    return render(request, 'polls/index.html', context)


#TODO check work the create func
def create(request):
    form = CreateQuestion()
    if request.method == 'POST':
        form = CreateQuestion(request.POST)
        if form.is_valid():
            form.save()
        return redirect

    context = {'form': form}
    return render(request, 'polls/create.html', context)


def update(request, pk):
    question = Question.objects.get(id=pk)
    form = CreateQuestion(instance=question)
    context = {'form': form}
    return render(request, 'polls/update.html', context)