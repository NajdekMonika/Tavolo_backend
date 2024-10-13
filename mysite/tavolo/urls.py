from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name="index"),
    path('event/', EventView.as_view()),
    path('user/', UserView.as_view()),
    path('table/', TableView.as_view()),
    path('allUsers/', AllUsersView.as_view()),
    path('allTables/', AllTablesView.as_view()),
    path('addInterests/', AddIntrestsView.as_view()),
]