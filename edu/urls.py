from django.urls import path

from edu.views import IndexPage, AppStudentDashboard, ForumHome, ForumCategory, CoursesGrid, \
    CoursesList, CoursesDetails, MyCourses, TakeCourses, CoursesForums, TakeQuiz, EditProfile, EditBilling, Messages, \
    Dashboard, InstructorMyCourse, EditCourse, Earnings, Statement, EditProfileInstructor, EditBillingInstructor, \
    MessagesInstructor, Login, CourseForumThread, ForumThread, WebsiteStudentDashboard, Register, EditCourseMeta, \
    EditCourseLesson

urlpatterns = [
    path('', IndexPage.as_view(), name='IndexPage'),
    path('app-student-dashboard/', AppStudentDashboard.as_view(), name='app_student_dashboard'),

    #forums
    path('forum-home/', ForumHome.as_view(), name='forum_home'),
    path('forum-category/', ForumCategory.as_view(), name='forum_category'),
    path('forum-thread/', ForumThread.as_view(), name='forum_thread'),

    #courses
    path('courses-grid/', CoursesGrid.as_view(), name='courses_grid'),
    path('courses-list/', CoursesList.as_view(), name='courses_list'),
    path('courses-details/', CoursesDetails.as_view(), name='courses_details'),

    #students
    path('my-courses/', MyCourses.as_view(), name='my_courses'),
    path('take-courses/', TakeCourses.as_view(), name='take_courses'),
    path('course-forums/', CoursesForums.as_view(), name='courses_forums'),
    path('take-quiz/', TakeQuiz.as_view(), name='take_quiz'),
    path('edit-profile/', EditProfile.as_view(), name='edit_profile'),
    path('edit-billing/', EditBilling.as_view(), name='edit_billing'),
    path('messages/', Messages.as_view(), name='messages'),
    path('course-forum-thread/', CourseForumThread.as_view(), name='course_forum_thread'),

    #instructor
    path('dashboard/', Dashboard.as_view(), name='dashboard'),
    path('instructor-my-course/', InstructorMyCourse.as_view(), name='instructor_my_course'),
    path('edit-course/', EditCourse.as_view(), name='edit_course'),
    path('edit-course-meta/', EditCourseMeta.as_view(), name='edit_course_meta'),
    path('edit-course-lesson/', EditCourseLesson.as_view(), name='edit_course_lesson'),
    path('earnings/', Earnings.as_view(), name='earnings'),
    path('statement/', Statement.as_view(), name='statement'),
    path('edit-profile-instructor/', EditProfileInstructor.as_view(), name='edit_profile_instructor'),
    path('edit-billing-instructor/', EditBillingInstructor.as_view(), name='edit_billing_instructor'),
    path('messages-instructor/', MessagesInstructor.as_view(), name='messages_instructor'),

    #auth
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),

    #website
    path('website-student-dashboard/', WebsiteStudentDashboard.as_view(), name='website_student_dashboard'),
]

