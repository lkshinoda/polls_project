from polls.models import Test, Question, Poll
from django.forms import ModelForm


class CreateTestForm(ModelForm):
    def __init__(self, *args, **kwargs): # переопределение конструктора с целью передачи стиля для каждого из полей
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['overview'].widget.attrs.update({'class': 'form-control'})
        
    class Meta:
        model = Test
        fields = ['title', 'overview']


class CreateQuestionForm(ModelForm):
    def __init__(self, *args, **kwargs): # переопределение конструктора с целью передачи стиля для каждого из полей
        super().__init__(*args, **kwargs)
        self.fields['question_text'].widget.attrs.update({'class': 'form-control'})
        self.fields['option_a'].widget.attrs.update({'class': 'form-control'})
        self.fields['option_b'].widget.attrs.update({'class': 'form-control'})
        self.fields['option_c'].widget.attrs.update({'class': 'form-control'})
        self.fields['option_d'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Question
        fields = ['question_text', 'option_a', 'option_b', 'option_c', 'option_d']


class CreatePollForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({'class': 'form-control'})
        self.fields['overview'].widget.attrs.update({'class': 'form-control'})

    class Meta:
        model = Poll
        fields = ['title', 'overview']
