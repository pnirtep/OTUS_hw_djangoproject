import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "courses_site.settings.settings_local")
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework import status, request
from rest_framework.test import APITestCase, APISimpleTestCase, APITransactionTestCase, force_authenticate, APIClient
from rest_framework.test import APIRequestFactory

from courses_api.factories import CourseFactory, LessonFactory
from courses_api.views import CoursesApiListView
from courses.models import Lesson

'''
Тесты Courses/ endpoint через RequestFactory
'''


class TestCaseForCourses(APITestCase):
    def test_get_course_all_authenticated(self):
        """
            Проверяем статус-код 200 ОК на авторизованный GET запрос к списку записей
        """
        factory = APIRequestFactory()
        request = factory.get("/api/courses/")
        user = User.objects.get(username='pnirtep')
        force_authenticate(request, user=user, token=user.auth_token)
        courses = CoursesApiListView.as_view({"get": "list"})
        response = courses(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_course_all_non_authenticated(self):
        """
            Проверяем статус-код 401 «не авторизован (не представился)» на НЕавторизованный GET запрос к списку записей
        """
        factory = APIRequestFactory()
        request = factory.get("/api/courses/")
        courses = CoursesApiListView.as_view({"get": "list"})
        response = courses(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_course(self):
        """
           Проверяем статус-код 201 «создано» на авторизованный POST запрос к списку записей
        """
        factory = APIRequestFactory()
        request = factory.post("/api/courses/", {'title': 'New Course Test', 'description': 'test test'}, format='json')
        user = User.objects.get(username='pnirtep')
        force_authenticate(request, user=user, token=user.auth_token)
        courses = CoursesApiListView.as_view({"post": "create"})
        response = courses(request)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


'''
Тесты Teachers/ endpoint через APIClient
'''


class TestCaseForTeacher(APITestCase):
    def setUp(self):
        """
        Задаем первоначальные параметры авторизованного пользователя для TokenAuth
        """
        self.user = User.objects.get(username="pnirtep")
        self.token = Token.objects.get(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_teacher_list_authenticated(self):
        """
            Проверяем статус-код 200 ОК на авторизованный GET запрос к списку записей
        """
        response = self.client.get("/api/teachers/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_teacher_list_non_authenticated(self):
        """
           Проверяем статус-код 401 «не авторизован (не представился)» на НЕавторизованный GET запрос к списку записей
        """
        self.client.force_authenticate(user=None)
        response = self.client.get("/api/teachers/")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_teacher_create(self):
        """
           Проверяем статус-код 201 «создано» на авторизованный POST запрос к списку записей
        """
        response = self.client.post("/api/teachers/", data={'first_name': 'Ben', 'last_name': 'Kenobi'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)


class TestCaseForLesson(APITestCase):
    def setUp(self):
        """
        Задаем первоначальные параметры авторизованного пользователя для TokenAuth
        """
        self.user = User.objects.get(username="pnirtep")
        self.token = Token.objects.get(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_update_lesson(self):
        """
        Тестируем корректность исполнения PUT запроса на изменение объекта Lesson при его наличии
        """
        lesson = Lesson.objects.all().first()
        if lesson:
            response = self.client.put("/api/lessons/1/", data={'title': 'New Title', 'description': 'New Description'})
            self.assertEqual(response.status_code, status.HTTP_200_OK)
        else:
            response = self.client.put("/api/lessons/1/", data={'title': 'New Title', 'description': 'New Description'})
            self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class TestCaseForStudent(APITestCase):
    def setUp(self):
        """
        Задаем первоначальные параметры авторизованного пользователя для TokenAuth
        """
        self.user = User.objects.get(username="pnirtep")
        self.token = Token.objects.get(user=self.user)
        self.api_authentication()

    def api_authentication(self):
        self.client.credentials(HTTP_AUTHORIZATION="Token " + self.token.key)

    def test_student_create(self):
        """
        Создаем тестового студента, через обращение к модели User, от которой через O2O наследуется модель Student
        """
        response = self.client.post("/api/users/", data={'username': 'benbenben', 'password': '123', 'user.student.bio':'Testbio'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)




