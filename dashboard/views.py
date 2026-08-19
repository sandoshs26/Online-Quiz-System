from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden,HttpResponse
from quiz.models import Quiz,Question,Result
from subject.models import Subject
from authentication.models import CustomUser
from django.db.models import Max

# Create your views here.

@login_required
def admin_dashboard(request):
    if request.user.role != "ADMIN":
        return HttpResponseForbidden("Access Denied")
    
    return render(request, "dashboard/admin_dashboard.html")

@login_required
def teacher_dashboard(request):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    quizzes = Quiz.objects.filter(teacher=request.user)

    total_quizzes = Quiz.objects.count()
    total_questions = Question.objects.filter(quiz__teacher=request.user).count()
    total_students = Result.objects.filter(quiz__teacher=request.user).values("student").distinct().count()
    total_attempts = Result.objects.filter(quiz__teacher=request.user).count()

    return render(request, "dashboard/teacher_dashboard.html",{
        "quizzes":quizzes,
        "total_quizzes":total_quizzes,
        "total_questions":total_questions,
        "total_students":total_students,
        "total_attempts":total_attempts,
        }
    )

@login_required
def student_dashboard(request):
    if request.user.role != "STUDENT":
        return HttpResponseForbidden("Access Denied")
    
    return render(request, "dashboard/student_dashboard.html")

@login_required
def create_quiz(request):
     if request.user.role != "TEACHER":
         return HttpResponseForbidden("Access Denied")

     subjects = Subject.objects.all()

     if request.method == "POST":
         title = request.POST.get("title")
         subject = Subject.objects.get(id=request.POST.get("subject"))

         Quiz.objects.create(
             title = title,
             subject = subject,
             teacher = request.user
         )

         return redirect("teacher_dashboard")

     return render(request,"dashboard/create_quiz.html",{"subjects":subjects})

@login_required
def edit_quiz(request,quiz_id):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    quiz = get_object_or_404(Quiz,id=quiz_id,teacher=request.user)
    subjects = Subject.objects.all()

    if request.method == "POST":
        quiz.title = request.POST.get("title")
        quiz.subject = Subject.objects.get(id=request.POST.get("subject"))
        quiz.save()

        return redirect("teacher_dashboard")

    return render(request,"dashboard/edit_quiz.html",{"quiz":quiz,"subjects":subjects})

@login_required
def delete_quiz(request,quiz_id):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    quiz = get_object_or_404(Quiz,id=quiz_id,teacher=request.user)
    quiz.delete()

    return redirect("teacher_dashboard")

@login_required
def add_question(request,quiz_id):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    quiz = get_object_or_404(Quiz, id = quiz_id,teacher=request.user)

    if request.method == "POST":

        
        Question.objects.create(
            quiz = quiz,
            question = request.POST.get("question"),
            option1 = request.POST.get("option1"),
            option2 = request.POST.get("option2"),
            option3 = request.POST.get("option3"),
            option4 = request.POST.get("option4"),
            correct_answer = request.POST.get("correct_answer"),
        )

        return redirect("teacher_dashboard")

    return render(request,"dashboard/add_question.html",{"quiz":quiz})

@login_required
def view_questions(request,quiz_id):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    quiz = get_object_or_404(Quiz,id=quiz_id,teacher=request.user)
    questions = Question.objects.filter(quiz=quiz)

    return render(request,"dashboard/view_questions.html",{"quiz":quiz,"questions":questions})

@login_required
def edit_question(request,question_id):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    question = get_object_or_404(Question,id=question_id,quiz__teacher=request.user)

    if request.method == "POST":
        question.question = request.POST.get("question")
        question.option1 = request.POST.get("option1")
        question.option2 = request.POST.get("option2")
        question.option3 = request.POST.get("option3")
        question.option4 = request.POST.get("option4")
        question.correct_answer = request.POST.get("correct_answer")

        question.save()

        return redirect("view_questions",quiz_id=question.quiz.id)

    return render(request,"dashboard/edit_question.html",{"question":question})

@login_required
def delete_question(request,question_id):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    question = get_object_or_404(Question,id=question_id,quiz_teacher=request.user)
    quiz_id = question.quiz.id

    question.delete()

    return redirect("view_questions",quiz_id=quiz_id)

@login_required
def teacher_results(request):
    if request.user.role != "TEACHER":
        return HttpResponseForbidden("Access Denied")

    results = Result.objects.filter(quiz__teacher=request.user).order_by("-id")

    return render(request,"dashboard/teacher_results.html",{"results":results})

@login_required
def manage_users(request):
    if request.user.role != "ADMIN":
        return HttpResponseForbidden("Access Denied")

    teachers = CustomUser.objects.filter(role = "TEACHER")
    students = CustomUser.objects.filter(role = "STUDENT")

    return render(request,"dashboard/manage_users.html",{"teachers":teachers,"students":students})

@login_required
def leaderboard(request):
    if request.user.role not in ["TEACHER","STUDENT"]:
        return HttpResponseForbidden("Access Denied")

    if request.user.role == "TEACHER":
        leaderboard = Result.objects.filter(
            quiz__teacher=request.user
        ).select_related(
            "student","quiz"
        ).order_by("-score","created_at")
    else:
        leaderboard = Result.objects.select_related(
            "student","quiz"
        ).orderby("-score","created_at")

    return render(request,"dashboard/leaderboard.html",{"leaderboard":leaderboard})
