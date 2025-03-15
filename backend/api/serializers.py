from top3health.models import *
from rest_framework import serializers
class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields='__all__'