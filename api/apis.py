from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class FibonacciAPIView(APIView):
    def fibonacci(self, n:int) -> int:
        """フィボナッチ数列のn番目を返す"""
        
        if n == 1:
            return n
        
        fib_prev = 1
        fib = 1
        
        for _ in range(n-2):
            fib_prev, fib = fib, fib + fib_prev
        
        return fib
    
    def get(self, request):
        """GETレスポンス"""
        
        n = int(request.query_params.get("n"))
        fibonacci = self.fibonacci(n)
        return Response({"result": fibonacci}, status=status.HTTP_200_OK)
