from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)  # поле заголовка
    text = forms.CharField(widget=forms.Textarea)  # поле текста вопроса

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    question = forms.ModelChoiceField(Question.objects.all())  # поле для связи с вопросом
    text = forms.CharField(widget=forms.Textarea)  # поле текста    ответа

    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a
