from django.http import HttpResponse
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Event
from .serializers import UserSerializer, EventSerializer


def index(request):
    return HttpResponse("Hello, you're at the tavolo index.")

# User views
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    lookup_field = 'uuid'

class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Event view
class EventView(APIView):
    def get(self, request, event_key):
        event_key = request.data.get('event_key')
        if not event_key:
            return Response({"error": "event_key is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            event = Event.objects.get(event_key=event_key)
            serializer = EventSerializer(event)
            return Response(serializer.data)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request, event_key):
        event_key = request.data.get('event_key')
        if not event_key:
            return Response({"error": "event_key is required"}, status=status.HTTP_400_BAD_REQUEST)
        try:
            event = Event.objects.get(event_key=event_key)
            event.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
# Table views
