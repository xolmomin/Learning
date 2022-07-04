from django.contrib import messages
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpResponse
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.encoding import force_str
from django.utils.http import urlsafe_base64_decode
from django.views.generic import FormView, TemplateView

from apps.users.forms import RegisterForm, LoginForm, ForgotPasswordForm, send_email
from apps.users.models import User
from apps.users.token import account_activation_token


class ForumHome(TemplateView):
    template_name = 'apps/forum/forum_home.html'


class ForumCategory(TemplateView):
    template_name = 'apps/forum/forum_home.html'


class ForumThread(TemplateView):
    template_name = 'apps/forum/forum_thread.html'


#students
class EditProfile(TemplateView):
    template_name = 'apps/students/edit_profile.html'


#instructor
class Dashboard(TemplateView):
    template_name = 'apps/instructor/dashboard.html'


class EditProfileInstructor(TemplateView):
    template_name = 'apps/instructor/edit_profile_instructor.html'


#auth
class LoginMixin:

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('index_page')
        return super().get(request, *args, **kwargs)


class Login(LoginMixin, LoginView):
    form_class = LoginForm
    success_url = reverse_lazy('index_page')
    template_name = 'apps/auth/login.html'


class Register(LoginMixin, FormView):
    form_class = RegisterForm
    success_url = reverse_lazy('login')
    template_name = 'apps/auth/register.html'

    def form_valid(self, form):
        form.save()
        send_email(form.data.get('email'), self.request, 'register')
        messages.add_message(
            self.request,
            level=messages.WARNING,
            message='Successfully send your email, Please activate your profile'
        )
        return super().form_valid(form)


class Logout(LogoutView):
    template_name = 'apps/auth/logout.html'


class ForgotPasswordPage(FormView):
    form_class = ForgotPasswordForm
    success_url = reverse_lazy('confirm_mail')
    template_name = 'apps/auth/forgot_password.html'

    def form_valid(self, form):
        send_email(form.data.get('email'), self.request, 'forgot')
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class ResetPassword(TemplateView):
    template_name = 'apps/auth/reset_password.html'


class ActivateEmailView(TemplateView):
    template_name = 'apps/auth/confirm_mail.html'

    def get(self, request, *args, **kwargs):
        uid = kwargs.get('uid')
        token = kwargs.get('token')

        try:
            uid = force_str(urlsafe_base64_decode(uid))
            user = User.objects.get(pk=uid)
        except Exception as e:
            print(e)
            user = None
        if user is not None and account_activation_token.check_token(user, token):
            user.is_active = True
            user.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            messages.add_message(
                request=request,
                level=messages.SUCCESS,
                message="Your account successfully activated!"
            )
            return redirect('login')
        else:
            return HttpResponse('Activation link is invalid!')