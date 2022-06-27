from django.contrib import admin
from django.urls import path, include
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('student_application.urls')),
    path('', TemplateView.as_view(template_name='index.html'), name="home"),
    path('html/', include('edu.urls')),

]


