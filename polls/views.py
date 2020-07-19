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


class TestUpdateView(View):
    def get(self, request, slug):
        questions = Question.objects.all()
        test = Test.objects.get(slug__iexact=slug)
        related_questions = test.question.all()

        related_id = []
        for quest in questions:
            if quest in related_questions:
                related_id.append(quest.id)

        form = CreatePollForm(instance=test)
        template_name = 'polls/update_test.html'
        context = {'form': form, 'test': test, 'questions': questions, 'related_id': related_id}
        return render(request, template_name, context)

    def post(self, request, slug):
        questions = request.POST.getlist('questions')
        test = Test.objects.get(slug__iexact=slug)
        test.question.clear()
        form = CreateTestForm(request.POST, instance=test)

        for quest_id in questions:
            question = Question.objects.get(id=quest_id)
            test.question.add(question)

        if form.is_valid():
            new_test = form.save()
            return redirect(new_test)


# class TestUpdateView(View):
#     def get(self, request, slug):
#         test = Test.objects.get(slug__iexact=slug)
#         questions = test.question.all()
#         template_name = 'polls/update_test.html'
#         form = CreateTestForm(instance=test)
#         context = {'test': test, 'form': form, 'questions': questions}
#         return render(request, template_name, context)
#
#     def post(self, request, slug):
#         test = Test.objects.get(slug__iexact=slug)
#         form = CreateTestForm(request.POST, instance=test)
#         if form.is_valid():
#             new_poll = form.save()
#             return redirect(new_poll)

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


class RunTestView(View):
    def get(self, request, slug):
        poll = Poll.objects.get(slug__iexact=slug)
        tests = poll.test.all()
        quest_list = []
        for test in tests:
            questions = test.question.all()
            for item in questions:
                quest_list.append(item)

        print(quest_list)


        context = {'poll': poll, 'tests': tests}
        template_name = 'polls/run_test.html'
        return render(request, template_name, context)
    def post(self, request, slug):
        result = request.POST.getlist('tests')
        data = request.POST

        pass


class IndexView(View):
    template_name = 'polls/index.html'
    def get(self, request):
        tests = Test.objects.all()
        polls = Poll.objects.all()
        context = {'polls': polls, 'tests': tests}

        return render(request, self.template_name, context)

    def post(self, request):
        tests = Test.objects.all()
        polls = Poll.objects.all()
        response_data = {}
        context = {'polls': polls, 'tests': tests}

        if request.POST.get('action') == 'add':
            tests = request.POST.getlist('tests[]')
            title = request.POST.get('title')
            description = request.POST.get('description')

            response_data['title'] = title
            response_data['description'] = description

            poll = Poll(
                title=title,
                description=description
            )
            poll.save()

            response_data['slug'] = poll.slug

            for test_id in tests:
                test = Test.objects.get(id=test_id)
                poll.test.add(test)

            return JsonResponse(response_data)

        return render(request, self.template_name, context)
    
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

