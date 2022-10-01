from pyexpat import model
from statistics import mode
from tabnanny import verbose
from django.db import models

# Create your models here.

class Post(models.Model):
    nickname = models.CharField(max_length=16, verbose_name='Ник')
    content = models.TextField(null=False, blank=False, verbose_name="Новость")
    published = models.DateTimeField(auto_now_add=True, db_index=True, 
    verbose_name="Опубликовано")
    rubric = models.ForeignKey('Rubric', null=True, on_delete=models.PROTECT,
    verbose_name='Рубрика')

    class Meta:
        verbose_name_plural = "Посты"
        verbose_name = "Пост"
        ordering = ['-published']


class Rubric(models.Model):
    name = models.CharField(max_length=20, db_index=True,
    verbose_name='Название')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Рубрики'
        verbose_name = 'Рубрика'
        ordering = ['name']