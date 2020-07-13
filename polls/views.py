from polls.forms import CreateTestForm, CreateQuestionForm, CreatePollForm
from polls.models import Question, Poll, Test
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView, View
from django.shortcuts import get_object_or_404, render, redirect
from django.http import JsonResponse


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


class PollDetailView(DetailView):
    model = Poll
    template_name = 'polls/detail_poll.html'


class PollUpdateView(View):
    def get(self, request, slug):
        tests = Test.objects.all()
        poll = Poll.objects.get(slug__iexact=slug)
        form = CreatePollForm(instance=poll)
        template_name = 'polls/update_poll.html'
        context = {'form': form, 'poll': poll, 'tests': tests}
        return render(request, template_name, context)
    
    def post(self, request, slug):
        slug = Poll.objects.get(slug__iexact=slug)
        form = CreatePollForm(request.POST, instance=slug)
        
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
        question_text = request.POST.get('question_text')
        true_answer = request.POST.get('true_answer')
        option_a = request.POST.get('option_a')
        option_b = request.POST.get('option_b')
        option_c = request.POST.get('option_c')

        response_data['question_text'] = question_text
        response_data['true_answer'] = true_answer
        response_data['option_a'] = option_a
        response_data['option_b'] = option_b
        response_data['option_c'] = option_c

        Question.objects.create(
            question_text=question_text,
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
    
    
class CreateSelfPollView(View):
    def get(self, request):
        question_form = CreateQuestionForm()
        template_name = 'polls/create_poll.html'
        context = {'question_form': question_form}
        return render(request, template_name, context)
    
    def post(self, request):
        pass