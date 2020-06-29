from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

# Create your tests here.
class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)

        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.title

        self.assertEqual(title.text, 'BLOG')


    def test_post_detail(self):
        post_000 = create_post(
            title = '첫 번째 포스트',
            content = '하이하이',
            author = self.author_000,
        )
        self.assertGreater(Post.objects.count(), 0)
        self.assertEqual(post_000, get_absolute_url(), '/blog/{}/'.format(post_000.pk))