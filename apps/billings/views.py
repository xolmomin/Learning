from django.views.generic import TemplateView


#student
class TakeQuiz(TemplateView):
    template_name = 'apps/students/take_quiz.html'


class EditBilling(TemplateView):
    template_name = 'apps/students/edit_billing.html'


#instructor
class Earnings(TemplateView):
    template_name = 'apps/instructor/earnings.html'


class Statement(TemplateView):
    template_name = 'apps/instructor/statement.html'


class EditBillingInstructor(TemplateView):
    template_name = 'apps/instructor/edit_billing_instructor.html'