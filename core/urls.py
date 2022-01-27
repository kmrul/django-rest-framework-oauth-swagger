from unicodedata import name
from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from .views import *

urlpatterns = [
    path('api/v1/todo/list/', ListTodoAPIView.as_view(), name='list'),
    path('api/v1/todo/detail/<str:pk>/', TodoDetailAPIView.as_view(), name='detail'),
    path('api/v1/todo/create/', CreateTodoAPIView.as_view(), name='create'),
    path('api/v1/todo/update/<str:pk>/', UpdateTodoAPIView.as_view(), name='update'),
    path('api/v1/todo/delete/<str:pk>/', DeleteTodoAPIView.as_view(), name='delete'),
    path('api/v1/token-auth/', obtain_auth_token, name='api_token_auth'), 
]
