from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    # Event
    path('events/<str:event_key>/', EventView.as_view()),

    # Create user
    path('users/create/', UserCreateView.as_view(), name='user-create'),
    # Retrieve user by UUID
    path('users/<uuid:uuid>/', UserRetrieveView.as_view(), name='user-retrieve'),
    # Retrieve all users
    path('users/', UserListView.as_view(), name='user-list'),
]