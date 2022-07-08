from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'apps/index.html'


class StudentDashboard(TemplateView):
    template_name = 'apps/students/app-student-dashboard.html'
