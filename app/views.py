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
	''' this function evaluate the answers submitted by the user,
	    if it is correct the total score is incrimented by one and
	    return the total score of the user '''
	total_score = 0
	for question in questions:
		answer = question.answer#fetching the correct answer
		user_answer = request.POST.get(str(question.id))#fetching the answer submitted by the user
		if(user_answer == answer):#evaluating the answer
			total_score += 1
	return total_score
