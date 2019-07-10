from django import forms
from .models import Question, Answer
from django.contrib.auth.models import User


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


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean_username(self):
        username = self.cleaned_data['username']
        if username == '':
            raise forms.ValidationError(u'Username is empty', code='validation_error')
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError(u'User already exists', code='validation_error')
        return username

    def clean_password(self):
        password = self.cleaned_data['password']
        if password == '':
            raise forms.ValidationError(
                u'Password is empty',
                code='validation_error'
            )
        return password

    def save(self):
        user = User.objects.create_user(**self.cleaned_data)
        user.save()
        return user
