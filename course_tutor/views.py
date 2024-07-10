from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from .models import Course, Topic, Question, Choice, Submission
from .serializers import CourseListSerializer, CourseDetailSerializer, QuestionSerializer, SubmissionSerializer

@permission_classes([IsAuthenticated])
class CourseListView(generics.ListAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseListSerializer

@permission_classes([IsAuthenticated])
class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseDetailSerializer
    lookup_field = 'id'

@permission_classes([IsAuthenticated])
class QuestionListView(generics.ListAPIView):
    serializer_class = QuestionSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Question.objects.filter(course_id=course_id)

@permission_classes([IsAuthenticated])
class SubmissionCreateView(generics.CreateAPIView):
    serializer_class = SubmissionSerializer

    def create(self, request, *args, **kwargs):
        data = request.data
        user = request.user
        question = Question.objects.get(id=data['question'])
        selected_choice = Choice.objects.get(id=data['selected_choice'])
        is_correct = selected_choice.is_correct
        submission = Submission.objects.create(
            user=user,
            question=question,
            selected_choice=selected_choice,
            is_correct=is_correct
        )
        serializer = self.get_serializer(submission)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
