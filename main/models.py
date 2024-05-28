from django.contrib.auth.models import User
from django.db import models
from django.utils.text import slugify


class Employee(models.Model):
    name1 = models.CharField('Имя',max_length=100)
    name2 = models.CharField('Фамилия',max_length=100)
    status = models.CharField('Должность',max_length=50)
    slug = models.SlugField(null=False, unique=True)
    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерация слага на основе заголовка статьи
            self.slug = slugify(self.name1)
        super().save(*args, **kwargs)
    def __str__(self):
        return self.name2


class Inventar(models.Model):
    name = models.CharField('Название',max_length=100)
    category = models.CharField('Категория',max_length=100)
    kod = models.IntegerField('Код')
    price = models.FloatField('Цена')
    image = models.ImageField(upload_to='images/')
    slug = models.SlugField(null=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            # Генерация слага на основе заголовка статьи
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
