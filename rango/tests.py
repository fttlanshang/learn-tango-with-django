from django.test import TestCase
from rango.models import Category


# Create your tests here.
class CategoryMethodTests(TestCase):
    def test_ensure_views_are_positive(self):
        """
        ensure the views of a category is equal to or above 0
        """
        cat = Category(name='test', views=1, likes=0)
        cat.save()
        self.assertEqual((cat.views >= 0), True)

    # def test_slug_line_creation(self):
    #     cat = Category(name="Random slug creation test")
    #     cat.save()
    #     self.assertEqual(cat.slug, 'random-slug-creation-test')
