from django.test import TestCase
from django.contrib.auth import get_user_model
from .models import Snack
from django.urls import reverse

class SnackTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='random', email='random@random.com',
            password='random@12345'
        )
        self.snack = Snack.objects.create(
            title='test',
            purchaser=self.user,
            description='test'
        )

    def test_str_method(self):
        self.assertEqual(str(self.snack), 'test')

    def test_detail_view(self):
        url = reverse('snacks_detail', args=[self.snack.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'snacks_detail.html')

    def test_create_view(self):
        url = reverse('snack_create')
        data = {
            "title": "test_2",
            "purchaser": self.user,
            "description": "test_2"
        }
        response = self.client.post(path=url, data=data, follow=True)
        self.assertTemplateUsed(response, 'snacks_detail.html')
        self.assertEqual(len(Snack.objects.all()), 2)
        self.assertRedirects(response, reverse('snacks_detail', args=[2]))
