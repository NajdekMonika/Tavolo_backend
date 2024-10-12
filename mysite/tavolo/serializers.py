from rest_framework import serializers
from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'
      
        
class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('name', 'description', 'logo', 'start_time', 'end_time')


class TableSerializer(serializers.ModelSerializer):
    class Meta:
        model = Table
        fields = '__all__'
        