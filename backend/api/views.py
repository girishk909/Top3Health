from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from top3health.models import CustomUser
from .serializers import userSerializer

class User(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        user_instance = get_object_or_404(CustomUser, id=user_id)
        serializer = userSerializer(user_instance)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
