from django.urls import path
from .views import CoursesList, CoursesDetails, CoursesGrid, MyCourses, TakeCourses, CoursesForums, Messages,\
      CourseForumThread, EditCourse, EditCourseLesson, EditCourseMeta, InstructorMyCourse, MessagesInstructor


urlpatterns = [
    #courses
    path('courses-grid/', CoursesGrid.as_view(), name='courses_grid'),
    path('courses-list/', CoursesList.as_view(), name='courses_list'),
    path('courses-details/', CoursesDetails.as_view(), name='courses_details'),

    #students_courses
    path('my-courses/', MyCourses.as_view(), name='my_courses'),
    path('take-courses/', TakeCourses.as_view(), name='take_courses'),
    path('course-forums/', CoursesForums.as_view(), name='courses_forums'),
    path('messages/', Messages.as_view(), name='messages'),
    path('course-forum-thread/', CourseForumThread.as_view(), name='course_forum_thread'),

    #instructor
    path('instructor-my-course/', InstructorMyCourse.as_view(), name='instructor_my_course'),
    path('edit-course/', EditCourse.as_view(), name='edit_course'),
    path('edit-course-meta/', EditCourseMeta.as_view(), name='edit_course_meta'),
    path('edit-course-lesson/', EditCourseLesson.as_view(), name='edit_course_lesson'),
    path('messages-instructor/', MessagesInstructor.as_view(), name='messages_instructor'),
]