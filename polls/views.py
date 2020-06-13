from polls.forms import CreateTestForm, CreateQuestionForm
from polls.models import Question, Poll, Test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView


""" Test """

class TestListView(ListView):
    model = Test
    template_name = 'polls/index.html'


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
    #TODO add a form verify


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