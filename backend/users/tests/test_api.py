from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser


class TestRegister(APITestCase):
    url = reverse('register')

    def test_good_create_student(self):
        data = {
            "first_name": "Test 1",
            "last_name": "Test 2",
            "username": "test_user",
            "password": "qwerty123",
            "email": "test@test.ru",
            "is_creator": "false"
        }
        response = self.client.post(self.url, data)

        self.assertEqual(status.HTTP_201_CREATED, response.status_code)

    def test_exist_student(self):
        student_1 = {
            "first_name": "Test 1",
            "last_name": "Test 2",
            "username": "test_user",
            "password": "qwerty123",
            "email": "test2@test.ru",
            "is_creator": "false"
        }

        self.client.post(self.url, student_1)

        student_2 = {
            "first_name": "Test 1",
            "last_name": "Test 2",
            "username": "test_user",
            "password": "qwerty123",
            "email": "test2@test.ru",
            "is_creator": "false"
        }

        response = self.client.post(self.url, student_2)

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_exist_email_student(self):
        student_1 = {
            "first_name": "Test 1",
            "last_name": "Test 2",
            "username": "test_user_1",
            "password": "qwerty123",
            "email": "test2@test.ru",
            "is_creator": "false"
        }

        self.client.post(self.url, student_1)

        student_2 = {
            "first_name": "Test 1",
            "last_name": "Test 2",
            "username": "test_user_2",
            "password": "qwerty123",
            "email": "test2@test.ru",
            "is_creator": "false"
        }

        response = self.client.post(self.url, student_2)

        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_without_field(self):
        # без имени
        student = {
            "last_name": "Test",
            "username": "test_user_1",
            "password": "qwerty123",
            "email": "test2@test.ru",
            "is_creator": "false"
        }
        response = self.client.post(self.url, student)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        # без фамилии
        student = {
            "first_name": "Test",
            "username": "test_user_1",
            "password": "qwerty123",
            "email": "test2@test.ru",
            "is_creator": "false"
        }
        response = self.client.post(self.url, student)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        # без логина
        student = {
            "first_name": "Test",
            "last_name": "Test",
            "password": "qwerty123",
            "email": "test2@test.ru",
            "is_creator": "false"
        }
        response = self.client.post(self.url, student)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        # без пароля
        student = {
            "first_name": "Test",
            "last_name": "Test",
            "username": "test_user_1",
            "email": "test2@test.ru",
            "is_creator": "false"
        }
        response = self.client.post(self.url, student)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        # без группы
        student = {
            "first_name": "Test",
            "last_name": "Test",
            "username": "test_user_1",
            "email": "test2@test.ru",
            "password": "qwerty123",
        }
        response = self.client.post(self.url, student)
        self.assertEqual(status.HTTP_201_CREATED, response.status_code)


class TestLogin(APITestCase):
    url = reverse('login')
    username = "test_user"
    password = "qwerty123"
    email = "test@test.ru"

    def create_user(self):
        data = {
            "first_name": "Test 1",
            "last_name": "Test 2",
            "username": self.username,
            "password": self.password,
            "email": self.email,
            "is_creator": "false"
        }
        self.client.post(reverse("register"), data)

    def test_success_login(self):
        self.create_user()

        data = {
            "username": self.username,
            "password": self.password
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

        data = {
            "email": self.email,
            "password": self.password,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_200_OK, response.status_code)

    def test_bad_login(self):
        self.create_user()
        data = {
            "username":  self.username,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        data = {
            "email":  self.username,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        data = {
            "email":  self.email,
            "username":  self.username,
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

    def test_bad_password(self):
        self.create_user()

        data = {
            "username": self.username,
            "password": self.password + "test",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)

        data = {
            "email": self.username,
            "password": self.password + "test",
        }
        response = self.client.post(self.url, data)
        self.assertEqual(status.HTTP_400_BAD_REQUEST, response.status_code)
