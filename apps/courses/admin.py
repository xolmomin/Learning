from django.contrib import admin

from courses.models import CourseCategory, Course, FeedBack, Chapter, Lesson, Tag, Comment, Question, Answer, \
    ForumCategory, Forum

admin.site.register([FeedBack, Chapter,Comment,  ForumCategory, Forum])

class QuestionInline(admin.TabularInline):
    model = Question
    extra = 20

class AnswerInline(admin.TabularInline):
    model = Answer
    extra = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    pass

class QuizAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}



@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
