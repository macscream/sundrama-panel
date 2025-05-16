from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("panel")
        else:
            messages.error(request, "Invalid credentials")
    return render(request, "login.html")
from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_view(request):
    logout(request)
    return redirect("login")
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def teacher_panel(request):
    return render(request, "panel.html")
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

@login_required
def add_report(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        notes = request.POST.get("notes")

        # Şimdilik sadece ekrana bastıracağız
        print("Report added:", student_name, notes)
        messages.success(request, "Report successfully added!")
        return redirect("panel")
        
    return render(request, "add_report.html")
