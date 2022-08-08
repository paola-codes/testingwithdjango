from django.test import TestCase
from . models import Post


class ModelTesting(TestCase):

    def setUp(self):
        self.blog = Post.objects.create(
            title='chocolate', author='vanilla', slug='caramel')

    def test_post_model(self):
        muffin = self.blog
        # Checking if 'muffin' is an
        # instance of 'Post' dabatase.
        self.assertTrue(isinstance(muffin, Post))
        # Checking the string returned by a Post
        # instance, a title called 'chocolate''
        self.assertEqual(str(muffin), 'chocolate')
