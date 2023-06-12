from django.urls import path
from .views import OrderAPIView,AddDataAPIView

urlpatterns = [
    path('',OrderAPIView.as_view()),
    path('<int:pk>/',OrderAPIView.as_view()),
    path('placeOrder/<int:pk>/',AddDataAPIView.as_view()),
]