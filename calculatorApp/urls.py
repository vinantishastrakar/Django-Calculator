from .views import calculatorNum
from django.urls import path, include

urlpatterns = [
    path("", calculatorNum)
]