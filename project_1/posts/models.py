from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()
class Group(models.Model):
    """Шаблон сообществ: 
        название,
        описание,
        дата создания,
        дата последнего изменения.
    """

    name = models.CharField(blank=False, max_length=200)
    description = models.TextField(blank=True)
    created = models.DateTimeField(blank=False, auto_now_add=True)
    changed = models.DateTimeField(blank=False, auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'


class Post(models.Model):
    """Шаблон постов: 
        название,
        содержание,
        факт публикации,
        дата публикации,
        дата создания,
        дата последнего изменения,
        принадлежнасть в группам.
    """

    name = models.CharField(blank=False, max_length=200)
    text = models.TextField(blank=True)
    published = models.BooleanField(default=False, blank=False)
    date = models.DateTimeField(blank=False)
    created = models.DateTimeField(blank=False, auto_now_add=True)
    changed = models.DateTimeField(blank=False, auto_now=True)
    group = models.ForeignKey(Group, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

