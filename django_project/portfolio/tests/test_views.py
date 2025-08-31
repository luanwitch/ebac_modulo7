from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from portfolio.models import Post  


class PostViewSetTest(APITestCase):
    def setUp(self):
        self.post = Post.objects.create(title="Teste", content="Conteúdo de teste")

    def test_list_posts(self):
        url = reverse('post-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_post(self):
        url = reverse('post-list')
        data = {"title": "Novo Post", "content": "Conteúdo"}
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
