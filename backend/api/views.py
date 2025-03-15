from django.shortcuts import render
from .serializers import *
from top3health.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
# Create your views here.
class user(APIView):
    def get(self, request, *args, **kwargs):
        qs=CustomUser.objects.filter(id = 1)
        print(qs)
        serializer= userSerializer(data=qs, many=True)
        if serializer.is_valid():
            print(daserializerta.data)
            return(serializer.data)
        print(f"error {serializer.errors}")
        return Response(serializer.errors)
    def post(self, request, *args, **kwargs):
        qs=CustomUser.objects.filter(pk = 1)
        serializer= userSerializer(data=qs, many=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)