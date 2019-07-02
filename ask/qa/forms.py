from django import forms
from .models import Question, Answer


class AskForm(forms.Form):
    title = forms.CharField(max_length=255)  # поле заголовка
    text = forms.CharField(widget=forms.Textarea)  # поле текста вопроса

    def clean_title(self):
        title = self.cleaned_data['title']
        if title.strip() == '':
            raise forms.ValidationError(
                u'Title is empty', code='validation_error')
        return title

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(
                u'Text is empty', code='validation_error')
        return text

    def save(self):
        q = Question(**self.cleaned_data)
        q.save()
        return q


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)  # поле текста    ответа
    question = forms.ModelChoiceField(Question.objects.all())  # поле для связи с вопросом

    def clean_question(self):
        question = self.cleaned_data['question']
        if question == 0:
            raise forms.ValidationError(
                u'Title is empty', code='validation_error')
        return question

    def clean_text(self):
        text = self.cleaned_data['text']
        if text.strip() == '':
            raise forms.ValidationError(
                u'Text is empty', code='validation_error')
        return text

    def save(self):
        a = Answer(**self.cleaned_data)
        a.save()
        return a
