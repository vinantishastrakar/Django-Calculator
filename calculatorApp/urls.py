from .views import Add, Subtract, Multiply, Divide, index
from django.urls import path, include

urlpatterns = [
    path("add/", Add.as_view()),
    path("subtract/", Subtract.as_view()),
    path("multiply/", Multiply.as_view()),
    path("divide/", Divide.as_view()),
    path("", index)
]

