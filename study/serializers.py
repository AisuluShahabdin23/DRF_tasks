from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from study.models import Course, Lesson, Payment
from users.models import User


class LessonSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели уроков """
    class Meta:
        model = Lesson
        fields = '__all__'


class LessonListSerializer(serializers.ModelSerializer):
    """ Сериализотор для модели урока для использования его в выводе в курсах """
    class Meta:
        model = Lesson
        fields = ['id', 'name', 'description', 'preview', 'video_url']


class CourseSerializer(serializers.ModelSerializer):
    """ Сериализатор для модели курсов """
    lessons_count = serializers.IntegerField(source='lesson_set.count', read_only=True)
    lessons = serializers.SerializerMethodField()
    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Course
        fields = '__all__'

    def get_lessons(self, course):
        return LessonListSerializer(Lesson.objects.filter(course=course), many=True).data


class PaymentSerializer(serializers.ModelSerializer):
    """ Сериализотор для модели платежей """
    course = SlugRelatedField(slug_field='name', queryset=Course.objects.all())
    lesson = SlugRelatedField(slug_field='name', queryset=Lesson.objects.all())
    owner = SlugRelatedField(slug_field='first_name', queryset=User.objects.all())

    class Meta:
        model = Payment
        fields = '__all__'


class PaymentsForOwnerSerializer(serializers.ModelSerializer):
    """ Сериализотор для модели платежей для использования его в выводе у пользователей """
    class Meta:
        model = Payment
        fields = ['id', 'amount', 'payment_date', 'payment_method']
