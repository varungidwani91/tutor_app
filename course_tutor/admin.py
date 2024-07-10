from django.contrib import admin
from .models import Course, Question, Choice, Submission

class ChoiceInline(admin.TabularInline):
    model = Choice

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'videoUrl', 'details', 'transcript', 'image_link')

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('course', 'question_text')
    inlines = [ChoiceInline]

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'selected_choice', 'is_correct')
