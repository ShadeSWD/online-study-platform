from rest_framework import viewsets, generics, filters
from django_filters.rest_framework import DjangoFilterBackend
from course.permissions import IsOwner, IsStaff, IsNotStaff, IsOwnerOrStaff
from course.models import Course, Lesson, Payment, Subscription
from course.serializers import CourseSerializer, LessonSerializer, PaymentSerializer, SubscriptionSerializer
from course.paginators import CoursePaginator


class SubscriptionViewSet(viewsets.ModelViewSet):
    serializer_class = SubscriptionSerializer
    queryset = Subscription.objects.all()

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new_subscription = serializer.save()
        new_subscription.owner = self.request.user
        new_subscription.save()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['create', ]:
            permission_classes = [IsNotStaff]
        if self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsOwnerOrStaff]
        if self.action in ['destroy', ]:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]


class CourseViewSet(viewsets.ModelViewSet):
    serializer_class = CourseSerializer
    queryset = Course.objects.all()
    pagination_class = CoursePaginator

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new_course = serializer.save()
        try:
            new_course.owner = self.request.user
        except ValueError:
            pass
        new_course.save()

    def get_permissions(self):
        permission_classes = []
        if self.action in ['create', ]:
            permission_classes = [IsNotStaff]
        if self.action in ['retrieve', 'update', 'partial_update']:
            permission_classes = [IsOwnerOrStaff]
        if self.action in ['destroy', ]:
            permission_classes = [IsOwner]
        return [permission() for permission in permission_classes]


class PaymentViewSet(viewsets.ModelViewSet):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [filters.SearchFilter, DjangoFilterBackend]
    ordering_fields = ['created_at', ]
    filterset_fields = ['course', 'payment_method']


class LessonCreateAPIView(generics.CreateAPIView):
    serializer_class = LessonSerializer
    permission_classes = [IsNotStaff]

    def perform_create(self, serializer):
        super().perform_create(serializer)
        new_lesson = serializer.save()
        try:
            new_lesson.owner = self.request.user
        except ValueError:
            pass
        new_lesson.save()


class LessonListAPIView(generics.ListAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    pagination_class = CoursePaginator


class LessonRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonUpdateAPIView(generics.UpdateAPIView):
    serializer_class = LessonSerializer
    queryset = Lesson.objects.all()
    permission_classes = [IsOwnerOrStaff]


class LessonDestroyAPIView(generics.DestroyAPIView):
    queryset = Lesson.objects.all()
    permission_classes = [IsOwner]
