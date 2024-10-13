from django.http import HttpResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Event, Table
from .serializers import UserSerializer, EventSerializer, TableSerializer


def index(request):
    return HttpResponse("Hello, you're at the tavolo index.")


class UserView(APIView):
    def get(self, request):
        uuid = request.data.get('uuid')
        try:
            user = User.objects.get(uuid=uuid)
            serializer = UserSerializer(user)
            return Response(serializer.data)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request):
        uuid = request.data.get('uuid')
        try:
            user = User.objects.get(uuid=uuid)
            user.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

class AllUsersView(APIView):
    def get(self, request):
        users = User.objects.all()
        for user in users:
            print(user.interests)
            print(type(user.interests))
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        User.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventView(APIView):
    def get(self, request):
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
    
    
class TableView(APIView):
    def get(self, request):
        event_key = request.data.get('event_key')
        table_number = request.data.get('table_number')
        try:
            table = Table.objects.get(event_key=event_key, table_number=table_number)
            serializer = TableSerializer(table)
            return Response(serializer.data)
        except Table.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request):
        serializer = TableSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    
    def delete(self, request):
        event_key = request.data.get('event_key')
        table_number = request.data.get('table_number')
        try:
            table = Table.objects.get(event_key=event_key, table_number=table_number)
            table.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Table.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)


class AllTablesView(APIView):
    def get(self, request):
        tables = Table.objects.all()
        serializer = TableSerializer(tables, many=True)
        return Response(serializer.data)
    
    def delete(self, request):
        Table.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class AddIntrestsView(APIView):
    def post(self, request):
        uuid = request.data.get('uuid')
        interests = request.data.get('interests')
        try:
            user = User.objects.get(uuid=uuid)
            user.interests = interests
            user.save()
            return Response(status=status.HTTP_200_OK)
        except User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)