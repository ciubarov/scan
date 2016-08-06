from django.contrib.auth.models import User
from django.db import models
from django.conf import settings
# from tinymce.models import HTMLField
import datetime
import string
import random

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

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Company._meta.fields]

class Promotion(models.Model):
    background = models.ImageField(upload_to = 'static/uploads/', default = '/uploads/None/no-img.jpg')
    image = models.ImageField(upload_to = 'static/uploads/', default = '/uploads/None/no-img.jpg')
    title = models.CharField(max_length=200)
    description = models.TextField()
    help_text = models.CharField(max_length=200)
    post_text = models.TextField()
    allowed_providers = models.CharField(max_length=200, default = 'vk,fb,ok,ig,tw', verbose_name = 'Allowed providers (Comma separate (vk,fb,ok,ig,tw))')
    company = models.ForeignKey(Company)

    def get_fields(self):
        return [(field.name, field.value_to_string(self)) for field in Promotion._meta.fields]

class Guest(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    email = models.EmailField(max_length=50)
    company = models.ForeignKey(Company)

    @classmethod
    def create(cls, user, phone, email, Company):
        guest = cls(user = user, phone = phone, email = email, company = Company)
        return guest

class Visit(models.Model):
    guest = models.ForeignKey(Guest)
    company = models.ForeignKey(Company)
    datetime_of_visit = datetime
    
class PromoCode(models.Model):
    promocode = models.CharField(max_length=10, unique = 1)
    guest = models.ForeignKey(Guest)

    @staticmethod
    def promo_gen():
        chars=string.ascii_uppercase + string.digits;
        size = 6
        code = ''.join(random.choice(chars) for _ in range(size))
        return code

    @classmethod
    def create(cls, Guest, code):
        promocode = cls(promocode = code, guest = Guest)
        return promocode