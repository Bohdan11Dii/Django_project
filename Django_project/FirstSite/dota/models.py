from django.db import models

# Create your models here.
from django.urls import reverse


class Dota(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to="photos/%Y/%m/%/d/")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

#
# class Category(models.Model):
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     context = models.TextField(blank=True)
#     photo = models.ImageField(upload_to="photos/%Y/%m/%/d/")

