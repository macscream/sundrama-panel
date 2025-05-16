from django.contrib import admin
from django.urls import path
from core.views import login_view, logout_view, teacher_panel, add_report, report_pdf, weekly_summary

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('panel/', teacher_panel, name='teacher_panel'),
    path('report/<int:session_id>/', add_report, name='add_report'),
    path('report/pdf/<int:session_id>/', report_pdf, name='report_pdf'),
    path('weekly-summary/', weekly_summary, name='weekly_summary'),
]
