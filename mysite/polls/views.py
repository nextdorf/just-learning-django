from django.shortcuts import render

# Create your views here.

from django.shortcuts import get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


def index(request):
  latest_questions = Question.objects.order_by('-pub_date')[:5]
  # template = loader.get_template('polls/index.html')
  # ctx = dict(latest_question_list = latest_questions)
  # return HttpResponse(template.render(ctx, request))
  ctx = dict(latest_question_list = latest_questions)
  return render(request, 'polls/index.html', ctx)


def detail(request, question_id):
  # q = Question.objects.get(f'question_id = {question_id}')
  # return HttpResponse(f'You are requesting "{q}"')

  # try:
  #   q = Question.objects.get(pk = question_id) #pk stands for "primary key" and refers to the id here
  # except Question.DoesNotExist:
  #   raise Http404(f'Question with id = {question_id} does not exist')

  q = get_object_or_404(Question, pk = question_id) #pk stands for "primary key" and refers to the id here
  return render(request, 'polls/detail.html', dict(question = q))

def vote(request, question_id):
  return HttpResponse(f'You are voting on Question {question_id}')

def results(request, question_id):
  return HttpResponse(f'You are looking at the results of Question {question_id}')

