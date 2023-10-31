from django.db import models
from users.models import User

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='дата изменения', auto_now=True)
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='course_images', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'курс'
        verbose_name_plural = 'курсы'


class Lesson(models.Model):
    created_at = models.DateTimeField(verbose_name='дата создания', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='дата изменения', auto_now=True)
    title = models.CharField(max_length=50, verbose_name='название')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='курс')
    preview = models.ImageField(upload_to='lesson_images', verbose_name='превью', **NULLABLE)
    description = models.TextField(verbose_name='описание')
    video_url = models.URLField(verbose_name='ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'урок'
        verbose_name_plural = 'уроки'


class Payment(models.Model):
    CASH = 0
    MONEY_TRANSFER = 1
    PAYMENT_METHODS = ((0, 'наличные'), (1, 'перевод'))

    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, verbose_name='пользователь')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE, verbose_name='курс')
    amount = models.DecimalField(verbose_name='сумма оплаты', max_digits=19, decimal_places=10)
    payment_method = models.IntegerField(verbose_name='способ оплаты', choices=PAYMENT_METHODS)

    class Meta:
        verbose_name = 'платёж'
        verbose_name_plural = 'платежи'
