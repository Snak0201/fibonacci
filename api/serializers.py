from rest_framework import serializers
from rest_framework.exceptions import ValidationError

class FibonacciSerializer(serializers.Serializer):
    n = serializers.CharField(max_length=10)
    
    def validate_n(self, n):
        n = int(n)
        if n <= 0:
            raise ValidationError("request n is not positive number", 400)
        return n
