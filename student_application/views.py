from django.shortcuts import render
from django.views.generic import TemplateView


class IndexPage(TemplateView):
    template_name = 'edu/index.html'


class AppStudentDashboard(TemplateView):
    template_name = 'edu/students/app-student-dashboard.html'


#forum
class ForumHome(TemplateView):
    template_name = 'edu/forum/forum_home.html'


class ForumCategory(TemplateView):
    template_name = 'edu/forum/forum_home.html'


class ForumThread(TemplateView):
    template_name = 'edu/forum/forum_thread.html'


#courses
class CoursesGrid(TemplateView):
    template_name = 'edu/courses/courses-grid.html'


class CoursesList(TemplateView):
    template_name = 'edu/courses/courses_list.html'


class CoursesDetails(TemplateView):
    template_name = 'edu/courses/courses_detail.html'


#students
class MyCourses(TemplateView):
    template_name = 'edu/students/my_courses.html'


class TakeCourses(TemplateView):
    template_name = 'edu/students/take_course.html'


class CoursesForums(TemplateView):
    template_name = 'edu/students/course_forums.html'


class TakeQuiz(TemplateView):
    template_name = 'edu/students/take_quiz.html'


class EditProfile(TemplateView):
    template_name = 'edu/students/edit_profile.html'


class EditBilling(TemplateView):
    template_name = 'edu/students/edit_billing.html'


class Messages(TemplateView):
    template_name = 'edu/students/messages.html'


class CourseForumThread(TemplateView):
    template_name = 'edu/students/course_forum_thread.html'


#instructor
class Dashboard(TemplateView):
    template_name = 'edu/instructor/dashboard.html'


class InstructorMyCourse(TemplateView):
    template_name = 'edu/instructor/instructor_my_course.html'


class EditCourse(TemplateView):
    template_name = 'edu/instructor/edit_course.html'


class EditCourseMeta(TemplateView):
    template_name = 'edu/instructor/edit_course_meta.html'


class EditCourseLesson(TemplateView):
    template_name = 'edu/instructor/edit_course_lesson.html'


class Earnings(TemplateView):
    template_name = 'edu/instructor/earnings.html'


class Statement(TemplateView):
    template_name = 'edu/instructor/statement.html'


class EditProfileInstructor(TemplateView):
    template_name = 'edu/instructor/edit_profile_instructor.html'


class EditBillingInstructor(TemplateView):
    template_name = 'edu/instructor/edit_billing_instructor.html'


class MessagesInstructor(TemplateView):
    template_name = 'edu/instructor/messages_instructor.html'


#auth
class Login(TemplateView):
    template_name = 'edu/auth/login.html'


class Register(TemplateView):
    template_name = 'edu/auth/register.html'


#website
class WebsiteStudentDashboard(TemplateView):
    template_name = 'edu/website/website_student_dashboard.html'