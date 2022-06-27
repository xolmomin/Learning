from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('index/', TemplateView.as_view(template_name='home.html'), name="index"),
    path('essential-buttons/', TemplateView.as_view(template_name="essential-buttons.html"), name="essential-buttons"),
    path('essential-icons/', TemplateView.as_view(template_name="essential-icons.html"), name="essential-icons"),
    path('essential-progress/', TemplateView.as_view(template_name="essential-progress.html"),
         name="essential-progress"),
    path('essential-grid/', TemplateView.as_view(template_name="essential-grid.html"), name="essential-grid"),
    path('essential-forms/', TemplateView.as_view(template_name="essential-forms.html"), name="essential-forms"),
    path('essential-tables/', TemplateView.as_view(template_name="essential-tables.html"), name="essential-tables"),
    path('essential-tabs/', TemplateView.as_view(template_name="essential-tabs.html"), name="essential-tabs"),
    path('essential-tabs/', TemplateView.as_view(template_name="essential-tabs.html"), name="essential-tabs"),
    path('login/', TemplateView.as_view(template_name='login.html'), name="login"),
    path('pricing/', TemplateView.as_view(template_name='pricing.html'), name="pricing"),
    path('sign-up/', TemplateView.as_view(template_name='sign-up.html'), name="sign-up"),
    path('survey/', TemplateView.as_view(template_name='survey.html'), name="survey"),
    path('tutors/', TemplateView.as_view(template_name='tutors.html'), name="tutors"),
    path('website-blog/', TemplateView.as_view(template_name='website-blog.html'), name="website-blog"),
    path('website-blog-post/', TemplateView.as_view(template_name='website-blog-post.html'), name="website-blog-post"),
]
