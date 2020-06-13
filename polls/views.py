from polls.forms import CreateTestForm
from polls.models import Question, Poll, Test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView



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
