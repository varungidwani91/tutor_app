from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import CourseListView, CourseDetailView, QuestionListView, SubmissionCreateView

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('courses/', CourseListView.as_view(), name='course-list'),
    path('courses/<int:id>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:course_id>/questions/', QuestionListView.as_view(), name='question-list'),
    path('submissions/', SubmissionCreateView.as_view(), name='submission-create'),
]
