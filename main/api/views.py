from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.shortcuts import render
# Create your views here.

@api_view(['GET'])
def getData(request):
    person = {'name':'leonardo','age':27}
    return Response(person)