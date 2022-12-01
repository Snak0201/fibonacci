"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class FibonacciAPIViewTest(TestCase):
    """FibonacciAPIViewのテスト"""
    
    # 正常系レスポンステスト
    def test_get_n1_response_ok(self):
        """特殊1: fib?n=1 はHTTP-200を返す"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(response.status_code, 200)
    
    def test_get_n2_response_ok(self):
        """特殊2: fib?n=2 はHTTP-200を返す"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(response.status_code, 200)

    def test_get_n7_response_ok(self):
        """通常: fib?n=7 はHTTP-200を返す"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(response.status_code, 200)
    
    def test_get_n99_response_ok(self):
        """負荷: fib?n=99 はHTTP-200を返す"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(response.status_code, 200)

    # 正常系計算テスト
    def test_get_n1_result_correct(self):
        """特殊1: fib?n=1 の答えが正しい"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)

    def test_get_n2_result_correct(self):
        """特殊2: fib?n=2 の答えが正しい"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)

    def test_get_n7_result_correct(self):
        """通常: fib?n=7 の答えが正しい"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 13)

    def test_get_n99_result_correct(self):
        """負荷: fib?n=99 の答えが正しい"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 218922995834555169026)
