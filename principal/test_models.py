from django.test import TestCase
from .models import Post

class TestPostModel(TestCase):
    def test_post_creation(self):
        post = Post.objects.create(
            title="Meu Primeiro Post",
            content="Este é o conteúdo do meu post de teste."
        )
        self.assertEqual(post.title, "Meu Primeiro Post")
        
        self.assertIsNotNone(post.published_date)
