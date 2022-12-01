from rest_framework.serializers import IntegerField, Serializer
from rest_framework.exceptions import ValidationError

class FibonacciSerializer(Serializer):
    n = IntegerField()
    
    def validate_n(self, n):
        """nについてバリデーションする"""
        if n <= 0:
            raise ValidationError("正の整数を入力してください。")
        return n
