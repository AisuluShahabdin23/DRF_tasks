from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView

from study.models import Course, Lesson
from study.serializers import CourseSerializer, LessonSerializer


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
