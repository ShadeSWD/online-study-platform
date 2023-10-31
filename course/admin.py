from django.contrib import admin
from course.models import Course, Lesson, Payment

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payment)
