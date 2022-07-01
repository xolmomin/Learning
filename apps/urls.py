
from .views import IndexPage, AppStudentDashboard
from django.urls import path, include

urlpatterns = [
    path('', include('apps.billings.urls')),
    path('', include('apps.courses.urls')),
    path('', include('apps.users.urls')),
    path('', IndexPage.as_view(), name='index_page'),
    path('app-student-dashboard/', AppStudentDashboard.as_view(), name='app_student_dashboard')
]
