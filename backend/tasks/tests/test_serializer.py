from django.test import TestCase
from tasks.models import Category
from tasks.serializer import CategorySerializer
from users.models import CustomUser


class CategorySerializerTestCase(TestCase):
    def create_data(self):
        self.user = CustomUser.objects.create_user("test_user", 'mail@mail.ru', 'my_test_password123')
        category_1 = Category.objects.create(title='Category 1', creator=self.user)
        category_2 = Category.objects.create(title='Category 2', creator=self.user)
        self.categories = [category_1, category_2]

    def test_ok(self):
        self.create_data()
        data = CategorySerializer(self.categories, many=True).data
        expected_data = [
            {
                'id': self.categories[0].id,
                'title': 'Category 1',
            },
            {
                'id': self.categories[1].id,
                'title': 'Category 2',
            }
        ]

        self.assertEqual(expected_data, data)
