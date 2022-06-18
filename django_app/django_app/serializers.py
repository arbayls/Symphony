from rest_framework import serializers
from django_app.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('preferred_name',
                  'user_name',
                  'pronouns',)
