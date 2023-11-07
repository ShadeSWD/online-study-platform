from rest_framework.test import APITestCase
from rest_framework import status

from course.models import Course, Lesson, Subscription


class CourseTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_course(self):
        data = {
            'title': "Test",
            'description': 'Test desc'
        }
        response = self.client.post(
            '/courses/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json(),
            {'id': 1, 'title': 'Test', 'description': 'Test desc', 'lessons_count': 0, 'lessons': [],
             'subscription_status': False, }
        )

        self.assertTrue(Course.objects.all().exists())


class LessonTestCase(APITestCase):
    def setUp(self):
        pass

    def test_create_lesson(self):
        data = {
            'title': "Test",
            'description': 'Test desc'
        }
        response = self.client.post(
            '/lessons/create/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertEqual(
            response.json()['description'], 'Test desc')

        self.assertTrue(Lesson.objects.all().exists())

    def test_list_lesson(self):
        response = self.client.get(
            '/lessons/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED
        )

    def test_retrieve_lesson(self):
        response = self.client.get(
            '/lessons/1/'
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND
        )


class TestSubscription(APITestCase):
    def setUp(self):
        data = {
            'title': "Test",
            'description': 'Test desc'
        }
        self.client.post(
            '/courses/',
            data=data
        )

    def test_create_subscription(self):
        data = {
            "is_active": True,
            "course": 0
        }

        response = self.client.post(
            '/subscriptions/',
            data=data
        )

        self.assertEqual(
            response.status_code,
            status.HTTP_201_CREATED
        )

        self.assertTrue(Course.objects.all().exists())
