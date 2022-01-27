from unicodedata import name
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('', ListTodoAPIView.as_view(), name='todo'),
    path('detail/<str:pk>/', TodoDetailAPIView.as_view(), name='detail'),
    path('create/', CreateTodoAPIView.as_view(), name='create'),
    path('update/<str:pk>/', UpdateTodoAPIView.as_view(), name='update'),
    path('delete/<str:pk>/', DeleteTodoAPIView.as_view(), name='delete'),
    path('token-auth/', obtain_auth_token, name='api_token_auth'), 
]
