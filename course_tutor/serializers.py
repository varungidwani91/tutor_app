from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Course, Topic, Question, Choice, Submission

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ['id', 'title', 'videoUrl', 'details', 'transcript', 'image_link']

class CourseListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'image_link']

class CourseDetailSerializer(serializers.ModelSerializer):
    topics = TopicSerializer(many=True, read_only=True)

    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'topics']

class ChoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Choice
        fields = ['id', 'choice_text', 'is_correct']

class QuestionSerializer(serializers.ModelSerializer):
    options = serializers.SerializerMethodField()
    correctAnswer = serializers.SerializerMethodField()

    class Meta:
        model = Question
        fields = ['id', 'question_text', 'options', 'correctAnswer']

    def get_options(self, obj):
        return [choice.choice_text for choice in obj.choices.all()]

    def get_correctAnswer(self, obj):
        correct_choice = obj.choices.filter(is_correct=True).first()
        return correct_choice.choice_text if correct_choice else None

class SubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Submission
        fields = ['id', 'user', 'question', 'selected_choice', 'is_correct']
