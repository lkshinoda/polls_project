from polls.forms import CreateTestForm, CreatePollForm
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



class TestDeleteView(DeleteView):
    model = Test
    template_name = 'polls/delete_test.html'
    success_url = '/test/'


""" Question """


class QuestionListView(ListView):
    model = Question
    template_name = 'polls/question_list.html'


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
    # form_class = CreateQuestionForm
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




class CreateSelfTestView(View):
    def get(self, request):
        test_form = CreateTestForm()
        template_name = 'polls/create_test.html'
        context = {'test_form': test_form}
        return render(request, template_name, context)

    def post(self, request):
        data = request.POST
        save_m2m_data(data)
        return redirect('/test/')


def AnswerHandler(request):
    pass


class RunTestView(View):
    template_name = 'polls/run_test.html'

    def get(self, request, slug):
        poll = Poll.objects.get(slug__iexact=slug)
        tests = poll.test.all()
        context = {'poll': poll, 'tests': tests}
        return render(request, self.template_name, context)

    def post(self, request, slug):
        data = request.POST
        result, count = answer_handler(data)
        poll = Poll.objects.get(slug__iexact=slug)
        context = {'poll': poll, 'result': result, 'count': count}
        template_name = 'polls/result.html'

        return render(request, template_name, context)


