from polls.forms import CreateTestForm, CreateQuestionForm, CreatePollForm
from polls.models import Question, Poll, Test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator


class IndexPageView(ListView):
    model = Poll
    template_name = 'polls/index.html'

""" Test """

class TestListView(ListView):
    title = 'Список тестов'
    model = Test
    template_name = 'polls/test_list.html'


class TestDetailView(DetailView):
    model = Test
    template_name = 'polls/detail_test.html'


class TestCreateView(CreateView):
    form_class = CreateTestForm
    template_name = 'polls/create_test.html'


class TestUpdateView(UpdateView):
    model = Test
    form_class = CreateTestForm
    template_name = 'polls/update_test.html'


class TestDeleteView(DeleteView):
    model = Test
    template_name = 'polls/delete_test.html'
    success_url = '/'


""" Question """

class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'


class QuestionCreateView(CreateView):
    form_class = CreateQuestionForm
    template_name = 'polls/create_question.html'


class QuestionDetailView(DetailView):
    model = Question
    template_name = 'polls/detail_question.html'


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = CreateQuestionForm
    template_name = 'polls/update_question.html'


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'polls/delete_question.html'
    success_url = '/question/'

""" Poll """

class PollCreateView(CreateView):
    form_class = CreatePollForm
    template_name = 'polls/create_poll.html'


class PollListView(ListView):
    model = Poll
    template_name = 'polls/poll_list.html'


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/detail_poll.html'


class PollUpdateView(UpdateView):
    model = Poll
    form_class = CreatePollForm
    template_name = 'polls/update_poll.html'


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'polls/delete_poll.html'
    success_url = '/poll/'


class RunTestView(DetailView):
    model = Test
    template_name = 'polls/run_test.html'



def CreateTestFunc(View):

    test = Test.objects.all()
    context = 4

    return render(request, 'polls/run_test.html', context)

def answer(request, question_id):
    pass
