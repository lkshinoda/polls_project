from django.db import models


class Question(models.Model):
    question_text = models.TextField(max_length=2000)
    true_answer = models.CharField(max_length=255)
    is_active = models.BooleanField()
    admin_comment = models.CharField(max_length=255)
    option_a = models.CharField(max_length=50)
    option_b = models.CharField(max_length=50)
    option_c = models.CharField(max_length=50)
    option_d = models.CharField(max_length=50)


class Test(models.Model):
    question = models.ManyToManyField(Question)
    title = models.CharField(max_length=255)
    slug = models.SlugField()  # default length = 50
    overview = models.TextField(max_length=2000)
    is_active = models.BooleanField()
    admin_comment = models.CharField(max_length=255)


class Poll(models.Model):
    test = models.ManyToManyField(Test)
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    overview = models.TextField(max_length=2000)
    is_active = models.BooleanField()
    admin_comment = models.CharField(max_length=255)
