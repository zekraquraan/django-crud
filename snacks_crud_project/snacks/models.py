from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse

class Snack (models.Model):
     title =models.CharField(max_length=255 ,help_text='snack_title')
     purchaser =models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
     description =models.CharField(max_length=255)


     def __str__(self) :
          return self.title

# class Meta:
#     ordering=['-pk']

def get_absolute_url(self):
    return reverse('snacks_detail',args=[self.pk])
# Create your models here.
