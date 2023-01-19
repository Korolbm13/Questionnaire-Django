from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from .models import Choice, Question


def index(request):
        return render(request, "index.html")


class IndexView(generic.ListView):
    template_name = 'opros_index.html'
    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:3]


class DetailView(generic.DetailView):
    model = Question
    template_name = 'opros_detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'opros_results.html'


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'opros_detail.html', {
            'question': question,
            'error_message': "Вы не выбрали ответ.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))