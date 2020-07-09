from django.contrib import admin
from polls.models import Question, Test, Poll
from polls.forms import CreateTestForm


class TestPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']


class PollPageAdmin(admin.ModelAdmin):
    list_display = ['title', 'description']
    list_filter = ['title', 'description']
    search_fields = ['title', 'description']
    

class QuestionPageAdmin(admin.ModelAdmin):
    list_display = ['question_text']


admin.site.register(Poll, PollPageAdmin)
admin.site.register(Test, TestPageAdmin)
admin.site.register(Question, QuestionPageAdmin)
