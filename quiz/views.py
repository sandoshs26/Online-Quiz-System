from django.shortcuts import render,get_object_or_404
from .models import Quiz,Question,Result
from django.contrib.auth.decorators import login_required

# Create your views here.
def quiz_list(request):
    quizzes = Quiz.objects.all()

    return render(request,"quiz/quiz_list.html",{"quizzes":quizzes})

def quiz_detail(request,quiz_id):
    quiz = get_object_or_404(Quiz,id=quiz_id)
    questions = Question.objects.filter(quiz=quiz)

    if request.method == "POST":
        score = 0

        for question in questions:
            selected_answer = request.POST.get(f"question_{question.id}")

            if selected_answer == question.correct_answer:
                score += 1

        total = questions.count()
        percentage = (score/total)*100 if total > 0 else 0

        Result.objects.create(
            student=request.user,
            quiz=quiz,
            score=score,
            total=total,
        )

        return render(request,"quiz/result.html",{"quiz":quiz,"score":score,"total":total,"percentage":percentage})

    return render(request,"quiz/quiz_detail.html",{ "quiz":quiz,"questions":questions})

@login_required
def result_history(request):
    results = Result.objects.filter(student = request.user)

    return render(request,"quiz/result_history.html",{"results":results})