from django.db import models
import time
from pytils import translit
from django.urls import reverse


def gen_slug(s):    # генерация уникального slug в формате: translit title + unix time
    new_slug = translit.slugify(s)
    t = str(int(time.time()))
    return (f'{new_slug}-{t}')


class Question(models.Model):
    title = models.TextField(max_length=2000, verbose_name='Текст вопроса')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    admin_comment = models.CharField(max_length=255, blank=True, verbose_name='Коментарий администратора')


    def get_absolute_url(self):
        return reverse('detail_question', kwargs={'pk': self.id})

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answer')
    title = models.CharField(max_length=50, verbose_name='Вариант ответа')
    is_true = models.BooleanField(default=False, verbose_name='Правильный ответ')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'


class Test(models.Model):
    question = models.ManyToManyField(Question, related_name='tests', verbose_name='Вопросы')
    title = models.CharField(max_length=255, verbose_name='Название теста')
    slug = models.SlugField(max_length=255, verbose_name='Slug')  # default length = 50
    description = models.TextField(max_length=2000, verbose_name='Подробное описание')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    admin_comment = models.CharField(max_length=255, blank=True, verbose_name='Коментарий администратора')

    def get_absolute_url(self):
        return reverse('detail_test', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # переопределение метода save для генерации slug только при создании теста
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Тест'
        verbose_name_plural = 'Тесты'


class Poll(models.Model):
    test = models.ManyToManyField(Test, related_name='poll', verbose_name='Тесты')
    title = models.CharField(max_length=255, verbose_name='Название')
    slug = models.SlugField(max_length=255, unique=True, verbose_name='Slug')
    description = models.TextField(max_length=2000, verbose_name='Описание')
    is_active = models.BooleanField(default=True, verbose_name='Активный')
    admin_comment = models.CharField(max_length=255, blank=True, verbose_name='Коментарий администратора')

    def get_absolute_url(self):
        return reverse('detail_poll', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # переопределение метода save для генерации slug при создании опроса
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
