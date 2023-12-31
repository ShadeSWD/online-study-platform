# Generated by Django 4.2.6 on 2023-10-29 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='название')),
                ('preview', models.ImageField(upload_to='course_images', verbose_name='Превью')),
                ('description', models.TextField(verbose_name='Описание')),
                ('video_url', models.URLField(verbose_name='Ссылка на видео')),
            ],
            options={
                'verbose_name': 'Урок',
                'verbose_name_plural': 'Уроки',
            },
        ),
    ]
