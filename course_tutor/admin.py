from django.contrib import admin
from .models import Course, Topic, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice

class QuestionInline(admin.TabularInline):
    model = Question

class TopicInline(admin.TabularInline):
    model = Topic

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'image_link')
    inlines = [TopicInline, QuestionInline]

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'videoUrl', 'details', 'transcript', 'image_link')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'question_text')
    inlines = [ChoiceInline]

@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'is_correct')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'selected_choice', 'is_correct')
