from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from django_app.models import User
from django_app.serializers import UserSerializer
from rest_framework.decorators import api_view
from django.core.signals import request_finished


def index(request):
    return HttpResponse("Hello, world. You're at the symphony index.")


# many
@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        user_name = request.GET.get('user_name', None)
        if user_name is not None:
            users = User.filter(user_name__icontains=user_name)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        user_name = request.GET.get('user_name', None)
        if user_name is not None:
            filtered_users = User.filter(user_name__icontains=user_name)
            filtered_users.delete()
            return JsonResponse({'message': 'Users were deleted successfully.'},
                                status=status.HTTP_204_NO_CONTENT)



# one
@api_view(['GET', 'DELETE'])
def user(request, pk):
    if request.method == 'GET':
        user = User.objects.get(pk=pk)

        user_serializer = UserSerializer(user)
        return JsonResponse(user_serializer.data)

    elif request.method == 'DELETE':
        user = User.objects.get(pk=pk)
        user.delete()
        return JsonResponse({'message': 'User was deleted successfully.'},
                            status=status.HTTP_204_NO_CONTENT)
