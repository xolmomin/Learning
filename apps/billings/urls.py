from django.urls import path
from .views import TakeQuiz, Earnings, Statement, EditBilling, EditBillingInstructor

urlpatterns = [
    #student
    path('take-quiz/', TakeQuiz.as_view(), name='take_quiz'),
    path('edit-billing/', EditBilling.as_view(), name='edit_billing'),

    #instructor
    path('earnings/', Earnings.as_view(), name='earnings'),
    path('statement/', Statement.as_view(), name='statement'),
    path('edit-billing-instructor/', EditBillingInstructor.as_view(), name='edit_billing_instructor'),
]