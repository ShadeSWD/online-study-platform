from django.urls import path
from rest_framework.routers import DefaultRouter
from course.apps import CourseConfig
from course.views import CourseViewSet, PaymentViewSet, LessonCreateAPIView, LessonListAPIView, LessonRetrieveAPIView, \
    LessonUpdateAPIView, LessonDestroyAPIView, SubscriptionViewSet

app_name = CourseConfig.name

router = DefaultRouter()
router.register(r'courses', CourseViewSet, basename='courses')
router.register(r'payments', PaymentViewSet, basename='payments')
router.register(r'subscriptions', SubscriptionViewSet, basename='subscriptions')

urlpatterns = [
    path('lessons/create/', LessonCreateAPIView.as_view(), name='lesson-create'),
    path('lessons/', LessonListAPIView.as_view(), name='lesson-list'),
    path('lessons/<int:pk>/', LessonRetrieveAPIView.as_view(), name='lesson-retrieve'),
    path('lessons/<int:pk>/update/', LessonUpdateAPIView.as_view(), name='lesson-update'),
    path('lessons/<int:pk>/delete/', LessonDestroyAPIView.as_view(), name='lesson-delete'),
] + router.urls
