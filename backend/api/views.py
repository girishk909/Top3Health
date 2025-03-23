from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from top3health.models import CustomUser, Myhealthscreening, Mydailylog, Myfitness
from .serializers import userSerializer, healthScreeningSerializer, fitnessSerializer, dailyLogSerializer

class User(APIView):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('user_id')
        
        # Get the user instance
        user_instance = get_object_or_404(CustomUser, id=user_id)
        
        # Fetch related data (health_screening, daily_log, fitness)
        health_screening_data = Myhealthscreening.objects.filter(customuser=user_instance)
        daily_log_data = Mydailylog.objects.filter(customuser=user_instance)
        fitness_data = Myfitness.objects.filter(customuser=user_instance).first()  # Only one instance per user
        
        # Serialize the user and related data
        user_data = userSerializer(user_instance).data
        health_screening_serialized = healthScreeningSerializer(health_screening_data, many=True).data
        daily_log_serialized = dailyLogSerializer(daily_log_data, many=True).data
        fitness_serialized = fitnessSerializer(fitness_data).data if fitness_data else None

        # Add related data to the user data response
        user_data['health_screening'] = health_screening_serialized
        user_data['fitness'] = fitness_serialized
        user_data['daily_log'] = daily_log_serialized

        return Response(user_data)

    def post(self, request, *args, **kwargs):
        serializer = userSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)
