from polls.forms import CreateTestForm, CreateQuestionForm, CreatePollForm
from polls.models import Question, Poll, Test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse
from polls.services import *

""" Test """

class TestListView(ListView):
    title = 'Список тестов'
    model = Test
    template_name = 'polls/test_list.html'


class TestDetailView(View):
    def get(self, request, slug):
        test = Test.objects.get(slug__iexact=slug)
        template_name = 'polls/detail_test.html'
        context = {'test': test}
        return render(request, template_name, context)
        
    def post(self, request, slug):
        test = Test.objects.get(slug__iexact=slug)
        test.delete()
        return redirect('/test/')


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
    success_url = '/test/'


""" Question """


class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'


class QuestionCreateView(CreateView):
    form_class = CreateQuestionForm
    template_name = 'polls/create_question.html'


class QuestionDetailView(DetailView):
    def get(self, request, pk):
        question = Question.objects.get(id=pk)
        template_name = 'polls/detail_question.html'
        context = {'question': question}
        return render(request, template_name, context)
        
    def post(self, request, pk):
        quest = Question.objects.get(id=pk)
        quest.delete()
        return redirect('/question/')


class QuestionUpdateView(UpdateView):
    model = Question
    form_class = CreateQuestionForm
    template_name = 'polls/update_question.html'


class QuestionDeleteView(DeleteView):
    model = Question
    template_name = 'polls/delete_question.html'
    success_url = '/question/'


""" Poll """


class PollDetailView(View):
    def get(self, request, slug):
        poll = Poll.objects.get(slug__iexact=slug)
        template_name = 'polls/detail_poll.html'
        context = {'poll': poll}
        return render(request, template_name, context)

    def post(self, request, slug):
        poll = Poll.objects.get(slug__iexact=slug)
        poll.delete()
        return redirect('/')


class PollUpdateView(View):
    def get(self, request, slug):
        tests = Test.objects.all()
        poll = Poll.objects.get(slug__iexact=slug)
        related_tests = poll.test.all()

        related_id = []
        for test in tests:
            if test in related_tests:
                related_id.append(test.id)

        form = CreatePollForm(instance=poll)
        template_name = 'polls/update_poll.html'
        context = {'form': form, 'poll': poll, 'tests': tests, 'related_id': related_id}
        return render(request, template_name, context)

    def post(self, request, slug):
        tests = request.POST.getlist('tests')
        poll = Poll.objects.get(slug__iexact=slug)
        poll.test.clear()
        form = CreatePollForm(request.POST, instance=poll)

        for test_id in tests:
            test = Test.objects.get(id=test_id)
            poll.test.add(test)

        if form.is_valid():
            new_poll = form.save()
            return redirect(new_poll)


class PollDeleteView(DeleteView):
    model = Poll
    template_name = 'polls/delete_poll.html'
    success_url = '/'


class RunTestView(DetailView):
    model = Test
    template_name = 'polls/run_test.html'


def view_poll(request):
    tests = Test.objects.all()
    polls = Poll.objects.all()
    response_data = {}
    context = {'polls': polls, 'tests': tests}

    if request.POST.get('action') == 'add':
        title = request.POST.get('title')
        description = request.POST.get('description')

        response_data['title'] = title
        response_data['description'] = description

        Poll.objects.create(
            title=title,
            description=description
        )
        return JsonResponse(response_data)

    return render(request, 'polls/index.html', context)
    
def create_question(request):
    questions = Question.objects.all()
    response_data = {}
    context = {'questions': questions}

    if request.POST.get('action') == 'add':
        title = request.POST.get('title')
        true_answer = request.POST.get('true_answer')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')

        response_data['title'] = title
        response_data['true_answer'] = true_answer
        response_data['option_a'] = option_a
        response_data['option_b'] = option_b
        response_data['option_c'] = option_c

        Question.objects.create(
            title=title,
            true_answer=true_answer,
            option_a=option_a,
            option_b=option_b,
            option_c=option_c
        )
        return JsonResponse(response_data)

    return render(request, 'polls/test.html', context)


# def create_poll(request):
#     question_form = CreateQuestionForm(instance=Question)
#     tests = Test.objects.all()
#     polls = Poll.objects.all()
#     response_data = {}
#     context = {'polls': polls, 'tests': tests}

#     if request.POST.get('action') == 'add':
#         title = request.POST.get('title')
#         description = request.POST.get('description')

#         response_data['title'] = title
#         response_data['description'] = description

#         Poll.objects.create(
#             title=title,
#             description=description
#         )
#         return JsonResponse(response_data)

#     return render(request, 'polls/create_poll.html', context)
    
    
class CreateSelfTestView(View):
    def get(self, request):
        question_form = CreateQuestionForm()
        test_form = CreateTestForm()
        template_name = 'polls/create_test.html'
        context = {'question_form': question_form, 'test_form': test_form}
        return render(request, template_name, context)
            
    def post(self, request):
        data = request.POST
        save_m2m_data(data)
        template_name = 'polls/test_list.html'

        return redirect('/test/')
        

def AnswerHandler(request):
    pass

