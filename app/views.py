from django.shortcuts import render
from app.models import Question

def q_list(request):
	questions = Question.objects.all()
	return render(request, 'q_list.html', {'questions': questions})

def result(request):
	questions = Question.objects.all()
	total_score = get_score(request, questions)
	return render(request, 'result.html', {'total_score': total_score})

def get_score(request, questions):
	total_score = 0
	for question in questions:
		answer = question.answer
		user_answer = request.POST.get(str(question.id))
		if(user_answer == answer):
			total_score += 1
	return total_score
