from django.forms import ModelForm
from polls.models import Test, Question

class CreateTestForm(ModelForm):
    class Meta:
        model = Test
        fields = ['title', 'overview']


class CreateQuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = '__all__'