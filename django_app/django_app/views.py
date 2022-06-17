from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from django_app.models import User
from django_app.serializers import UserSerializer
from rest_framework.decorators import api_view


def index(request):
    return HttpResponse("Hello, world. You're at the symphony index.")


@api_view(['GET', 'POST', 'DELETE'])
def user_list(request):
    if request.method == 'GET':
        users = User.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            users = User.filter(title__icontains=title)

        users_serializer = UserSerializer(users, many=True)
        return JsonResponse(users_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    # @api_view(['GET', 'PUT', 'DELETE'])
    # def tutorial_detail(request, pk):
    #     # find tutorial by pk (id)
    #     try:
    #         tutorial = Tutorial.objects.get(pk=pk)
    #     except Tutorial.DoesNotExist:
    #         return JsonResponse({'message': 'The tutorial does not exist'}, status=status.HTTP_404_NOT_FOUND)
    #
    #     # GET / PUT / DELETE tutorial
    #
    #
    # @api_view(['GET'])
    # def tutorial_list_published(request):
    #     # GET all published tutorials
