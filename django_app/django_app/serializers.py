from rest_framework import serializers
from django_app.models import User
from django_app.models import Prompt
from django_app.models import Answer


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('preferred_name',
                  'user_name',
                  'pronouns',)


class PromptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prompt
        fields = ('title',
                  'life_sphere',
                  'prompt_text',)


class AnswerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Answer
        fields = ('title',
                  'life_sphere',
                  'user_answer',)
