from django.urls import path
from . import apis


urlpatterns = [
    path("fib", apis.FibonacciAPIView.as_view())
]
