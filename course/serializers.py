from rest_framework import serializers
from course.models import Course, Lesson, Payment, Subscription
from course.validators import UrlValidator


class LessonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lesson
        fields = '__all__'
        validators = [UrlValidator(field='video_url')]


class SubscriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subscription
        fields = '__all__'


class CourseSerializer(serializers.ModelSerializer):
    lessons_count = serializers.SerializerMethodField()
    subscription_status = serializers.SerializerMethodField()
    lessons = LessonSerializer(many=True, read_only=True)

    def get_subscription_status(self, obj):
        try:
            user = self.context['request'].user
            subscription = Subscription.objects.get(owner=user, course=obj.pk)
            return subscription.is_active
        except:
            return False

    def get_lessons_count(self, obj):
        return obj.lessons.count()

    class Meta:
        model = Course
        fields = ['id', 'title', 'lessons_count', 'description', 'lessons', 'subscription_status']


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = '__all__'
