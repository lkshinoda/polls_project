from django.contrib import admin
from polls.models import Question, Test, Poll, Answer
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
    list_display = ['title']


admin.site.register(Poll, PollPageAdmin)
admin.site.register(Test, TestPageAdmin)
admin.site.register(Question, QuestionPageAdmin)
admin.site.register(Answer)
