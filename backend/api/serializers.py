from rest_framework import serializers
from top3health.models import *

# Serializer for Myhealthscreening model
class healthScreeningSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myhealthscreening
        fields = '__all__'

# Serializer for Myfitness model
class fitnessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Myfitness
        fields = '__all__'

# Serializer for Mydailylog model
class dailyLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mydailylog
        fields = '__all__'

# Serializer for CustomUser model, including nested related models
class userSerializer(serializers.ModelSerializer):
    # Nested serializers for health screening, fitness, and daily log
    health_screening = healthScreeningSerializer(many=True, read_only=True)
    fitness = fitnessSerializer(many=True, read_only=True)
    daily_log = dailyLogSerializer(many=True, read_only=True)

    class Meta:
        model = CustomUser
        fields = '__all__'
