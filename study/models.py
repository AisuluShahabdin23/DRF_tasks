from django.conf import settings
from django.db import models

# Create your models here.
NULLABLE = {'blank': 'True', 'null': 'True'}


class Course(models.Model):
    """ Модель курсов """
    title_course = models.CharField(max_length=50, verbose_name='Название курса')
    image_course = models.ImageField(upload_to='course/', verbose_name='Картинка(превью) курса', **NULLABLE)
    description_course = models.TextField(verbose_name='Описание курса')

    def __str__(self):
        return f'{self.title_course}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    """ Модель уроков """
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


class Payment(models.Model):
    """Модель платежей"""
    METHOD_CHOICES = (
        ('CASH', 'Наличные'),
        ('TRANSFER', 'Перевод на счет'),
    )

    date = models.DateTimeField(verbose_name='Дата оплаты')
    course = models.ForeignKey(Course, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Оплаченный курс')
    lesson = models.ForeignKey(Lesson, on_delete=models.SET_NULL, **NULLABLE, verbose_name='Оплаченный урок')
    amount = models.PositiveIntegerField(verbose_name='Сумма оплаты')
    method = models.CharField(max_length=25, choices=METHOD_CHOICES, verbose_name='Способ оплаты')

    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, verbose_name='Владелец платежа', **NULLABLE)

    def __str__(self):
        return f'Платеж от {self.user} на сумму {self.amount}'

    class Meta:
        verbose_name = 'Платеж'
        verbose_name_plural = 'Платежи'
