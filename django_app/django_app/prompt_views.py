from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from django_app.models import Prompt
from django_app.serializers import PromptSerializer
from rest_framework.decorators import api_view
from django.core.signals import request_finished


def index(request):
    return HttpResponse("Hello, world. You're at the symphony index.")


# many
@api_view(['GET', 'POST', 'DELETE'])
def prompt_list(request):
    if request.method == 'GET':
        prompts = Prompt.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            prompts = Prompt.filter(title__icontains=title)

        prompts_serializer = PromptSerializer(prompts, many=True)
        return JsonResponse(prompts_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        prompt_data = JSONParser().parse(request)
        prompt_serializer = PromptSerializer(data=prompt_data)
        if prompt_serializer.is_valid():
            prompt_serializer.save()
            return JsonResponse(prompt_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(prompt_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        title = request.GET.get('title', None)
        if title is not None:
            filtered_prompts = Prompt.filter(title__icontains=title)
            filtered_prompts.delete()
            return JsonResponse({'message': 'Prompts were deleted successfully.'},
                                status=status.HTTP_204_NO_CONTENT)


# one
@api_view(['GET', 'DELETE'])
def prompt(request, pk):
    if request.method == 'GET':
        prompt = Prompt.objects.get(pk=pk)

        prompt_serializer = PromptSerializer(prompt)
        return JsonResponse(prompt_serializer.data)

    elif request.method == 'DELETE':
        prompt = Prompt.objects.get(pk=pk)
        prompt.delete()
        return JsonResponse({'message': 'Prompt was deleted successfully.'},
                            status=status.HTTP_204_NO_CONTENT)
