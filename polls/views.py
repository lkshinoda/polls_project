from django.shortcuts import render, redirect
from polls.forms import CreateTestForm
from polls.models import Question, Poll, Test


def indexpage(request):
    tests = Test.objects.all()
    context = {'tests': tests}
    return render(request, 'polls/index.html', context)


#TODO check work the create func
def create_test(request):
    form = CreateTestForm()
    if request.method == 'POST':
        form = CreateTestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'polls/create_test.html', context)


def update_test(request, pk):
    question = Question.objects.get(id=pk)
    form = CreateTestForm(instance=question)
    if request.method == 'POST':
        form = CreateTestForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'form': form}
    return render(request, 'polls/update_test.html', context)

def test_view(request, slug):
    test = Test.objects.get(slug__iexact=slug)
    context = {'test': test}
    return render(request, 'polls/test.html', context)

