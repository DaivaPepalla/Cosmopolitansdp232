from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import *

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Menu.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Menu))
        self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):
    def setUp(self):
        Menu.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Items.objects.create(menu_id=1, item_name='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Items))
        self.assertEqual(str(data), 'django beginners')


    