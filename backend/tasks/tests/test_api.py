from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token
from tasks.models import Category
from tasks.serializers.main_serializers import CategorySerializer
from users.models import CustomUser


class CategoryAPITestCase(APITestCase):
    def create_data(self):
        self.user = CustomUser.objects.create_user("test_user", 'mail@mail.ru', 'my_test_password123')
        category_1 = Category.objects.create(title='Category 1', creator=self.user)
        category_2 = Category.objects.create(title='Category 2', creator=self.user)
        self.categories = [category_1, category_2]

    def set_token(self):
        token = Token.objects.create(user=self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_get_category(self):
        url = reverse('category-list')
        self.create_data()

        # проверка недоступности без авторизации
        response = self.client.get(url)
        self.assertEqual(status.HTTP_401_UNAUTHORIZED, response.status_code)

        # проверка правильного результата
        self.set_token()
        received_data = self.client.get(url).data
        expected_data = CategorySerializer(self.categories, many=True).data
        self.assertEqual(expected_data, received_data)
