from django.http import HttpResponse
from .models import Question
from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404


def test(request, *args, **kwargs):
    return HttpResponse('OK')


def index(request):
    new_list = Question.objects.new()
    paginator = Paginator(new_list, 10)
    questions = paginator.page(request.GET.get('page', 1))
    return render(request, 'qa/index.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'qa/detail.html', {'question': question})


def popular(request):
    new_list = Question.objects.popular()
    paginator = Paginator(new_list, 10)
    questions = paginator.page(request.GET.get('page', 1))
    return render(request, 'qa/index.html', {'questions': questions})
