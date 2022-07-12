# from django.contrib.auth.models import User
from account.models import UserBase
from django.test import TestCase
from django.urls import reverse

from store.models import Category, Product


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        """
        Test Category model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'django')

    def test_category_url(self):
        """
        Test category model slug and URL reverse
        """
        data = self.data1
        response = self.client.post(
            reverse('store:category_list', args=[data.slug]))
        self.assertEqual(response.status_code, 200)


class TestProductsModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        UserBase.objects.create(email='a@a.com')
        self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
                                            slug='django-beginners', price='20.00', image='django')
        self.data2 = Product.objects.create(category_id=1, title='django advanced', created_by_id=1,
                                             slug='django-advanced', price='20.00', image='django', is_active=False)

    def test_products_model_entry(self):
        """
        Test product model data insertion/types/field attributes
        """
        data = self.data1
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django beginners')

    def test_products_url(self):
        """
        Test product model slug and URL reverse
        """
        data = self.data1
        url = reverse('store:product_detail', args=[data.slug])
        self.assertEqual(url, '/django-beginners')
        response = self.client.post(
            reverse('store:product_detail', args=[data.slug]))
        self.assertEqual(response.status_code, 200)

    def test_products_custom_manager_basic(self):
        """
        Test product model custom manager returns only active products
        """
        data = Product.objects.all()
        self.assertEqual(data.count(), 2)

















# from django.contrib.auth.models import User
# from django.test import TestCase
# from django.urls import reverse

# from store.models import Category, Product


# class TestCategoriesModel(TestCase):

#     def setUp(self):                                    # creating a category 
#         self.data1 = Category.objects.create(name='django', slug='django')

#     def test_category_model_entry(self):
#         """
#         Test Category model data insertion/types/field attributes
#         """
#         data = self.data1
#         self.assertTrue(isinstance(data, Category))    # testing the category feilds are true
#         self.assertEqual(str(data), 'django')          # testing the __str__ method for returning title 
        

#     # def test_category_title_entry(self):
#     #     """
#     #     Test Category model data insertion/types/field attributes
#     #     """
#     #     data = self.data1
#     #     self.assertEqual(str(data), 'django')

# class TestProductsModel(TestCase):                     # creating products model 
#     def setUp(self):
#         Category.objects.create(name='django', slug='django')
#         User.objects.create(username='admin')
#         self.data1 = Product.objects.create(category_id=1, title='django beginners', created_by_id=1,
#                                             slug='django-beginners', price='20.00', image='django')

#     def test_products_model_entry(self):
#         """
#         Test product model data insertion/types/field attributes
#         """
#         data = self.data1
#         self.assertTrue(isinstance(data, Product))      # testing product feilds are true
#         self.assertEqual(str(data), 'django beginners') # tsting the __str__ method for returning the string 
