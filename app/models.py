from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# from tinymce.models import HTMLField
import datetime

SHORT_TEXT_LEN = 1000


# class Article(models.Model):
#     logo = models.ImageField(upload_to = '/uploads/', default = '/uploads/None/no-img.jpg')
#     title = models.CharField(max_length=200)
#     text = models.TextField()
#     user = models.ForeignKey(User)

#     def __str__(self):
#         return self.title

#     def get_short_text(self):
#         if len(self.text) > SHORT_TEXT_LEN:
#             return self.text[:SHORT_TEXT_LEN]
#         else:
#             return self.text

class Company(models.Model):
    name = models.CharField(max_length=200, default = '')
    logo = models.ImageField(upload_to = 'static/uploads/', default = '/uploads/None/no-img.jpg')
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=200)
    website = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name


class Promotion(models.Model):
    background = models.ImageField(upload_to = 'static/uploads/', default = '/uploads/None/no-img.jpg')
    image = models.ImageField(upload_to = 'static/uploads/', default = '/uploads/None/no-img.jpg')
    title = models.CharField(max_length=200)
    description = models.TextField()
    help_text = models.CharField(max_length=200)
    post_text = models.TextField()
    allowed_providers = models.CharField(max_length=200, default = 'vk,fb,ok,ig,tw', verbose_name = 'Allowed providers (Comma separate (vk,fb,ok,ig,tw))')
    company = models.ForeignKey(Company)

    def __str__(self):
        return self.title

class Guest(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    company = models.ForeignKey(Company)

class Visit(models.Model):
    guest = models.ForeignKey(Guest)
    datetime_of_visit = datetime