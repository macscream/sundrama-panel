from django.http import HttpResponse

from django.urls import path
from core.views import (
    login_view, logout_view, teacher_panel,
    add_report, report_pdf
)

urlpatterns = [
    path("login/", login_view, name="login"),
    path("logout/", logout_view, name="logout"),
    path("panel/", teacher_panel, name="panel"),
    path("add-report/", add_report, name="add_report"),
    path("report-pdf/", report_pdf, name="report_pdf"),
]
from core.views import weekly_summary

path("weekly-summary/", weekly_summary, name="weekly_summary"),
