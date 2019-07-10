from django.http import HttpResponse, HttpResponseRedirect
from .models import Question
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404, reverse
from .forms import AskForm, AnswerForm, SignUpForm
from django.contrib.auth import login


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    new_list = Question.objects.new()
    paginator = Paginator(new_list, 10)
    questions = paginator.page(request.GET.get('page', 1))
    return render(request, 'qa/index.html', {'questions': questions, 'username': request.user})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        if form.is_valid():
            form._user = request.user
            form.question = question
            form.save()
            return HttpResponseRedirect(reverse('qa:detail', args=[question.pk]))
    else:
        form = AnswerForm(initial={'question': question})
    return render(request, 'qa/detail.html',
                  {'question': question,
                   'form': form,
                   'username': request.user})


def popular(request):
    new_list = Question.objects.popular()
    paginator = Paginator(new_list, 10)
    questions = paginator.page(request.GET.get('page', 1))
    return render(request, 'qa/index.html', {'questions': questions, 'username': request.user})


def ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            form._user = request.user
            question = form.save()
            return HttpResponseRedirect(reverse('qa:detail', args=[question.pk]))
    else:
        form = AskForm()
    return render(request, 'qa/ask.html', {'form': form, 'username': request.user})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('qa:index'))
    else:
        form = SignUpForm()
    return render(request, 'qa/signup.html', {'form': form, 'username': request.user})
