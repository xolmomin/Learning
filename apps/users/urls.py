from django.urls import path

from .views import ForumHome, ForumCategory, EditProfile, Dashboard, EditProfileInstructor, Login, ForumThread, \
    Register, ResetPassword, ActivateEmailView, ForgotPasswordPage, Logout

urlpatterns = [

    #forums
    path('forum-home/', ForumHome.as_view(), name='forum_home'),
    path('forum-category/', ForumCategory.as_view(), name='forum_category'),
    path('forum-thread/', ForumThread.as_view(), name='forum_thread'),

    #students
    path('edit-profile/', EditProfile.as_view(), name='edit_profile'),

    #instructor
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('edit-profile-instructor/', EditProfileInstructor.as_view(), name='edit_profile_instructor'),

    #auth
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
    path('logout/', Logout.as_view(), name='logout'),
    path('forgot-password/', ForgotPasswordPage.as_view(), name='forgot_password'),
    path('reset-password/', ResetPassword.as_view(), name='reset_password'),
    path('activate/<str:uid>/<str:token>', ActivateEmailView.as_view(), name='confirm_mail'),
]



