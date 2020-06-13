from django.db import models
from django.utils.text import slugify
import time
from pytils import translit


def gen_slug(s):    # генерация уникального slug в формате: translit title + unix time
    new_slug = translit.slugify(s)
    t = str(int(time.time()))
    return (f'{new_slug}-{t}')


class Question(models.Model):
    question_text = models.TextField(max_length=2000)
    true_answer = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    admin_comment = models.CharField(max_length=255)
    option_a = models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    option_d = models.CharField(max_length=50)

    def __str__(self):
        return self.question_text

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'


class Test(models.Model):
    question = models.ManyToManyField(Question)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)  # default length = 50
    overview = models.TextField(max_length=2000)
    is_active = models.BooleanField(default=True)
    admin_comment = models.CharField(max_length=255)

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
    test = models.ManyToManyField(Test)
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    overview = models.TextField(max_length=2000)
    is_active = models.BooleanField()
    admin_comment = models.CharField(max_length=255)

    def save(self, *args, **kwargs): # переопределение метода save для генерации slug при создании опроса
        if not self.slug:
            self.slug = gen_slug(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Опрос'
        verbose_name_plural = 'Опросы'
