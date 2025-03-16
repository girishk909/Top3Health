from rest_framework import serializers
from top3health.models import *

class healthScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myhealthscreening
        fields = '__all__'

class fitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myfitness
        fields = '__all__'

class dailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mydailylog
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    health_screening = healthScreeningSerializer(many=True, read_only=True)  # Include health screening data
    fitness = fitnessSerializer(many=True, read_only=True)
    daily_log = dailyLogSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
