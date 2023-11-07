from django.contrib import admin
from course.models import Course, Lesson, Payment, Subscription

admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Payment)
admin.site.register(Subscription)
