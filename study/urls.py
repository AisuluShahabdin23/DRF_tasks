from django.urls import path
from rest_framework.routers import DefaultRouter

from study.apps import StudyConfig
from study.views import CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, \
  LessonUpdateAPIView, LessonDestroyAPIView

app_name = StudyConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
  path('', LessonListAPIView.as_view(), name='lesson_list'),
  path('<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson_retrieve'),
  path('create/', LessonCreateAPIView.as_view(), name='lesson_create'),
  path('<int:pk>/', LessonUpdateAPIView.as_view(), name='lesson_update'),
  path('<int:pk>/', LessonDestroyAPIView.as_view(), name='lesson_destroy'),
] + router.urls
