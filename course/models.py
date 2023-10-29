from django.db import models

NULLABLE = {'null': True, 'blank': True}


class Course(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    title = models.CharField(max_length=50, verbose_name='название')
    preview = models.ImageField(upload_to='course_images', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Курс'
        verbose_name_plural = 'Курсы'


class Lesson(models.Model):
    created_at = models.DateTimeField(verbose_name='creation date', auto_now_add=True)
    changed_at = models.DateTimeField(verbose_name='change date', auto_now=True)
    title = models.CharField(max_length=50, verbose_name='название')
    course = models.ForeignKey(to=Course, on_delete=models.CASCADE)
    preview = models.ImageField(upload_to='course_images', verbose_name='Превью', **NULLABLE)
    description = models.TextField(verbose_name='Описание')
    video_url = models.URLField(verbose_name='Ссылка на видео', **NULLABLE)

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Урок'
        verbose_name_plural = 'Уроки'
