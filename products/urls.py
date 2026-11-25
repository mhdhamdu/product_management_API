
from django.urls import path
from .views import (
    RegisterAPIView,
    ProductListCreateAPIView,
    ProductDetailAPIView
)
from rest_framework.authtoken.views import obtain_auth_token


urlpatterns = [
    path('register/', RegisterAPIView.as_view()),
    path('login/', obtain_auth_token),
    path('products/', ProductListCreateAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
]
