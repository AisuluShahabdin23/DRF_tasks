from django.urls import path
from rest_framework.routers import DefaultRouter
from study.apps import StudyConfig
from study.views import CourseViewSet, LessonListAPIView, LessonRetrieveAPIView, LessonCreateAPIView, \
  LessonUpdateAPIView, LessonDestroyAPIView, PaymentListAPIView, PaymentRetrieveAPIView

app_name = StudyConfig.name

router = DefaultRouter()
router.register(r'course', CourseViewSet, basename='course')

urlpatterns = [
  path('lesson/', LessonListAPIView.as_view(), name='lesson_list'),
  path('lesson/<int:pk>/detail/', LessonRetrieveAPIView.as_view(), name='lesson_detail'),
  path('lesson/create/', LessonCreateAPIView.as_view(), name='lesson_create'),
  path('lesson/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson_update'),
  path('lesson/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson_delete'),

  path('payments/', PaymentListAPIView.as_view(), name='payments_list'),
  path('payments/<int:pk>/', PaymentRetrieveAPIView.as_view(), name='payments_get'),
] + router.urls
