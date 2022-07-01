from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'apps/index.html'


class AppStudentDashboard(TemplateView):
    template_name = 'apps/students/app-student-dashboard.html'