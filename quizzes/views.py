from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from quizzes.models import Exam, Question, Options

def index(request):
    exam_list = Exam.objects.order_by('deadline')[:5]
    context = {'exam_list': exam_list}
    return render(request, 'quizzes/index.html', context)

def examination(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'quizzes/examination.html', {'exam': exam})

def result(request, exam_id):
    exam = get_object_or_404(Exam, pk=exam_id)
    return render(request, 'quizzes/result.html', {'exam': exam})

def answer(request, exam_id):
    p = get_object_or_404(Exam, pk=exam_id)
    try:
        selected_choice = p.question_set.get(pk=request.POST['choice'])
    except (KeyError, Options.DoesNotExist):
        # Redisplay the poll voting form.
        return render(request, 'quizzes/examination.html', {
            'exam': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        # selected_choice.votes += 1
        # selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))
