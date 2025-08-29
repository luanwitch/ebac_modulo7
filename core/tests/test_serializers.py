from django.test import TestCase
from core.models import Post
from core.serializers import PostSerializer

class PostSerializerTest(TestCase):

    def test_serialization(self):
        post = Post.objects.create(title="Teste", content="Conteúdo do teste")
        serializer = PostSerializer(post)
        self.assertEqual(serializer.data['title'], "Teste")

    def test_deserialization(self):
        data = {'title': 'Novo Post', 'content': 'Conteúdo'}
        serializer = PostSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        post = serializer.save()
        self.assertEqual(post.title, "Novo Post")
