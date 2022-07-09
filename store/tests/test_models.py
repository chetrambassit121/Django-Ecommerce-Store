from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):                                    # creating a category 
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))    # testing the category feilds are true
        self.assertEqual(str(data), 'django')          # testing the __str__ method for returning title 
        

    # def test_category_title_entry(self):
    #     """
    #     Test Category model data insertion/types/field attributes
    #     """
    #     data = self.data1
    #     self.assertEqual(str(data), 'django')

class TestProductsModel(TestCase):                     # creating products model 
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))      # testing product feilds are true
        self.assertEqual(str(data), 'django beginners') # tsting the __str__ method for returning the string 
