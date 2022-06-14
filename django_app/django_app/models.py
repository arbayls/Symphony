from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user_name = models.Charfield(max_length=30)
    pronouns = models.TextChoices('She/Her They/Them He/Him')


class Answer(models.Model):
    name = models.CharField(max_length=30)
    life_sphere = models.CharField(max_length=30)
    user_answer = models.CharField(max_length=500)


class Prompt(models.Model):
    name = models.CharField(max_length=30)
    life_sphere = models.CharField(max_length=30)
    text = models.CharField(max_length=500)
