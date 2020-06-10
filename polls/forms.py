from django.forms import ModelForm
from polls.models import Question

class CreateQuestion(ModelForm):
    class Meta:
        model = Question
        fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d']
