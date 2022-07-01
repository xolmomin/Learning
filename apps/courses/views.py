from django.shortcuts import render
from django.views.generic import TemplateView


#courses
class CoursesGrid(TemplateView):
    template_name = 'apps/courses/courses-grid.html'


class CoursesList(TemplateView):
    template_name = 'apps/courses/courses_list.html'


class CoursesDetails(TemplateView):
    template_name = 'apps/courses/courses_detail.html'


#student_courses
class MyCourses(TemplateView):
    template_name = 'apps/students/my_courses.html'


class TakeCourses(TemplateView):
    template_name = 'apps/students/take_course.html'


class CoursesForums(TemplateView):
    template_name = 'apps/students/course_forums.html'


class Messages(TemplateView):
    template_name = 'apps/students/messages.html'


class CourseForumThread(TemplateView):
    template_name = 'apps/students/course_forum_thread.html'


#instructor
class InstructorMyCourse(TemplateView):
    template_name = 'apps/instructor/instructor_my_course.html'


class EditCourse(TemplateView):
    template_name = 'apps/instructor/edit_course.html'


class EditCourseMeta(TemplateView):
    template_name = 'apps/instructor/edit_course_meta.html'


class EditCourseLesson(TemplateView):
    template_name = 'apps/instructor/edit_course_lesson.html'


class MessagesInstructor(TemplateView):
    template_name = 'apps/instructor/messages_instructor.html'
