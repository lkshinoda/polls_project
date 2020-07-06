from django.contrib import admin
from polls.models import Question, Test, Poll
from polls.forms import CreateTestForm


class TestPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'overview']
    list_filter = ['title', 'overview']
    search_fields = ['title', 'overview']


class PollPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'overview']
    list_filter = ['title', 'overview']
    search_fields = ['title', 'overview']
    

class QuestionPageAdmin(admin.ModelAdmin):
    list_display = ['question_text']


admin.site.register(Poll, PollPageAdmin)
admin.site.register(Test, TestPageAdmin)
admin.site.register(Question, QuestionPageAdmin)
