from django.http import HttpResponse
from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status

from django_app.serializers import AnswerSerializer
from django_app.models import Answer
from rest_framework.decorators import api_view
from django.core.signals import request_finished


def index(request):
    return HttpResponse("Hello, world. You're at the symphony index.")


# many
@api_view(['GET', 'POST', 'DELETE'])
def answer_list(request):
    if request.method == 'GET':
        answers = Answer.objects.all()

        title = request.GET.get('title', None)
        if title is not None:
            answers = Answer.filter(title__icontains=title)

        answers_serializer = AnswerSerializer(answers, many=True)
        return JsonResponse(answers_serializer.data, safe=False)
        # 'safe=False' for objects serialization

    elif request.method == 'POST':
        answer_data = JSONParser().parse(request)
        answer_serializer = AnswerSerializer(data=answer_data)
        if answer_serializer.is_valid():
            answer_serializer.save()
            return JsonResponse(answer_serializer.data,
                                status=status.HTTP_201_CREATED)
        return JsonResponse(answer_serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        title = request.GET.get('title', None)
        if title is not None:
            filtered_answers = Answer.filter(title__icontains=title)
            filtered_answers.delete()
            return JsonResponse({'message': 'Answers were deleted successfully.'},
                                status=status.HTTP_204_NO_CONTENT)


# one
@api_view(['GET', 'DELETE'])
def prompt(request, pk):
    if request.method == 'GET':
        answer = Answer.objects.get(pk=pk)

        answer_serializer = AnswerSerializer(answer)
        return JsonResponse(answer_serializer.data)

    elif request.method == 'DELETE':
        answer = Answer.objects.get(pk=pk)
        answer.delete()
        return JsonResponse({'message': 'Answer was deleted successfully.'},
                            status=status.HTTP_204_NO_CONTENT)
