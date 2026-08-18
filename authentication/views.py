from django.shortcuts import render,redirect
from django.contrib.auth import login,logout
from .forms import LoginForm,RegisterForm

# Create your views here.
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)

        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.role == "ADMIN":
                return redirect("admin_dashboard")
            elif user.role == "TEACHER":
                return redirect("teacher_dashboard")
            elif user.role == "STUDENT":
                return redirect("student_dashboard")

    else:
        form = LoginForm()

    return render(request,"authentication/login.html",{"form":form})

def logout_view(request):
    logout(request)

    return redirect("login")

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("login")

    else:
        form = RegisterForm()

    return render(request,"authentication/register.html",{"form":form})
    