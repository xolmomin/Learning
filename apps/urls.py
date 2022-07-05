
from django.urls import path, include

from .views import IndexPage, StudentDashboard

urlpatterns = [
    path('', include('apps.billings.urls')),
    path('', include('apps.courses.urls')),
    path('', include('apps.users.urls')),
    path('', IndexPage.as_view(), name='index_page'),
    path('student-dashboard/', StudentDashboard.as_view(), name='student_dashboard')
]
