from django.db import models


class User(models.Model):
    preferred_name = models.CharField(max_length=30)
    user_name = models.CharField(max_length=30)
    pronouns = (
        ('She', 'She/Her/Hers'),
        ('They', 'They/Them/Theirs'),
        ('He', 'He/Him/His'),
        (preferred_name, 'I don\'t use gender pronouns.')
    )
    pronouns = models.CharField(max_length=30, choices=pronouns)


class Answer(models.Model):
    title = models.CharField(max_length=30)
    life_sphere = models.CharField(max_length=30)
    user_answer = models.CharField(max_length=500)


class Prompt(models.Model):
    title = models.CharField(max_length=30)
    life_sphere = models.CharField(max_length=30)
    prompt_text = models.CharField(max_length=500)


class Relationship(models.Model):
    relationship_type = (
        ('Romantic', 'Romantic Partner'),
        ('Friend', 'Friendship'),
        ('Roommate', 'Roommates'),
        ('Other', 'Something Else')
    )
    type = models.CharField(max_length=30, choices=relationship_type)
