
from django.urls import path
from django.http import HttpResponse
from core.views import (
    login_view, logout_view, teacher_panel,
    add_report, report_pdf, weekly_summary
)

urlpatterns = [
    path("", lambda request: HttpResponse("Sundrama Panel Aktif ✅")),
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("panel/", teacher_panel, name="panel"),
    path("add-report/", add_report, name="add_report"),
    path("report-pdf/", report_pdf, name="report_pdf"),
    path("weekly-summary/", weekly_summary, name="weekly_summary"),
]
path("favicon.ico", lambda request: HttpResponse("", content_type="image/x-icon")),
from .views import login_view

path("login/", login_view, name="login"),
path("panel/", teacher_panel, name="teacher_panel"),
from .views import home_view

urlpatterns += [
    path("home/", home_view, name="home"),
]
