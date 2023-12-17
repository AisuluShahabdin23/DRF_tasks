from django.db import models

# Create your models here.
NULLABLE = {'blank': 'True', 'null': 'True'}


class Course(models.Model):
    title_course = models.CharField(max_length=50, verbose_name='Название курса')
    image_course = models.ImageField(upload_to='course/', verbose_name='Картинка(превью) курса', **NULLABLE)
    description_course = models.TextField(verbose_name='Описание курса')

    def __str__(self):
        return f'{self.title_course}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    title_lesson = models.CharField(max_length=50, verbose_name='Название урока')
    description_lesson = models.TextField(verbose_name='Описание урока')
    image_lesson = models.ImageField(upload_to='lesson/', verbose_name='Картинка(превью) урока', **NULLABLE)
    url_lesson = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)
    url_course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name='Ссылка на курс', **NULLABLE)

    def __str__(self):
        return f'{self.title_lesson}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
