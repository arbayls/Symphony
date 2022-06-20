from rest_framework import serializers
from django_app.models import User
from django_app.models import Prompt


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('preferred_name',
                  'user_name',
                  'pronouns',)


class PromptSerializer(serializers.ModelSerializer):
    class Prompt:
        model = Prompt
        fields = ('title',
                  'life_sphere',
                  'prompt_text',)
