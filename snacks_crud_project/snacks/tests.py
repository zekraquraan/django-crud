from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import Snack

class TestSnacks(TestCase):
    def test_status_code(self):
        url = reverse('snack_list')  
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

    def test_snack_list_templates(self):
        url = reverse('snack_list')  
        response = self.client.get(url)
        self.assertTemplateUsed(response, 'snack_list.html')

class Snacktest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username = 'zekra',
            email = 'zekraquraan7@gmail.com@gmail.com',
            password = 'sub7anallah1'
        )

        self.snack = Snack.objects.create(
            title = 'test',
            purchaser = self.user,
            description = 'no description'
        )

    def test_detail_view(self):
        url = reverse('snacks_detail',args=[self.snack.id])
        res = self.client.get(url)
        self.assertEqual(res.status_code,200)
        self.assertTemplateUsed(res,'snacks_detail.html')

    def test_create_view(self):
        url = reverse('snack_create')
        data = {
            'title' :'test2',
            'purchaser' : self.user.id,
            'description' : 'no description'
        }
        res = self.client.post(path=url,data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()),2)
        self.assertTemplateUsed(res,'snacks_detail.html')
        self.assertRedirects(res,reverse('snacks_detail',args=[2]))

    def test_update_view(self):
        url = reverse('snack_update',args=[self.snack.id])
        data = {
            'title' :'test3',
            'purchaser' : self.user.id,
            'description' : 'no description'
        }
        res = self.client.post(path=url,data=data,follow=True)
        self.assertEqual(len(Snack.objects.all()),1)
        self.assertTemplateUsed(res,'snack_list.html')
        self.assertRedirects(res,reverse('snack_list'))

    def test_delete_view(self):
        url = reverse('snack_delete',args=[self.snack.id])
        res = self.client.post(path=url,follow=True)
        self.assertEqual(len(Snack.objects.all()),0)
        self.assertTemplateUsed(res,'snack_list.html')
        self.assertRedirects(res,reverse('snack_list'))

    def test_str_method(self):
        self.assertEqual(str(self.snack),'test')

    def test_fields_model(self):
        self.assertEqual(self.snack.purchaser,self.user)
        self.assertEqual(self.snack.title,'test')
        self.assertEqual(self.snack.description,'no description')