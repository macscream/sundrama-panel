
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.template.loader import render_to_string
import weasyprint

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

def logout_view(request):
    logout(request)
    return redirect("login")

@login_required
def teacher_panel(request):
    return render(request, "panel.html")

@login_required
def add_report(request):
    if request.method == "POST":
        student_name = request.POST.get("student_name")
        notes = request.POST.get("notes")
        print("Report added:", student_name, notes)
        messages.success(request, "Report successfully added!")
        return redirect("panel")
    return render(request, "add_report.html")

@login_required
def report_pdf(request):
    html = render_to_string("report_pdf.html", {"request": request})
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = 'inline; filename="report.pdf"'
    weasyprint.HTML(string=html).write_pdf(response)
    return response
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def weekly_summary(request):
    # Bu kısım ileride veritabanından haftalık veriler çekmek için genişletilebilir
    fake_data = [
        {"student": "Ali", "sessions": 3, "amount": "£90"},
        {"student": "Zara", "sessions": 2, "amount": "£60"},
    ]
    return render(request, "weekly_summary.html", {"summary": fake_data})
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user is not None:
            login(request, user)
            return redirect("teacher_panel")  # Giriş başarılı → panel sayfası
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

@login_required
def teacher_panel(request):
    return render(request, "teacher_panel.html")
from django.contrib.auth.decorators import login_required

from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def home_view(request):
    return render(request, "home.html")

