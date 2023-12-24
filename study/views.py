#from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, generics, serializers
from rest_framework.filters import OrderingFilter
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.relations import SlugRelatedField
from study.models import Course, Lesson, Payment
from study.serializers import CourseSerializer, LessonSerializer, PaymentSerializer
from users.models import User


# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    """ViewSet для вывода информации"""
    serializer_class = CourseSerializer
    queryset = Course.objects.all()


class LessonListAPIView(ListAPIView):
    """Отображение списка сущностей(через Generic-класс)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonRetrieveAPIView(RetrieveAPIView):
    """Отображение одной сущности(через Generic-класс)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonCreateAPIView(CreateAPIView):
    """Создание сущности (через Generic-класс)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonUpdateAPIView(UpdateAPIView):
    """Редактирование сущности(через Generic-класс)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class LessonDestroyAPIView(DestroyAPIView):
    """Удаление сущности(через Generic-класс)"""
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()


class PaymentListAPIView(generics.ListAPIView):
    """ Для вывода списка платежей(через Generic-класс) """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'owner', 'method',)
    ordering_fields = ('payment_date',)      # Определяем фильтрацию по дате


class PaymentRetrieveAPIView(generics.RetrieveAPIView):
    """ Для просмотра платежа(через Generic-класс) """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
