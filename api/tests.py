"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class FibonacciAPIViewTest(TestCase):
    """
    FibonacciAPIViewのテスト
    
    n=1, n=2の場合が特殊で、resultは1となる
    n=3, n=7の場合を通常のデータとして考える
    n=99の場合を計算量の多いデータとして考える
    
    """
    
    # 正常系レスポンステスト
    def test_get_n_1_response_ok(self):
        """特殊1: fib?n=1 はHTTP-200を返す"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(response.status_code, 200)
    
    def test_get_n_2_response_ok(self):
        """特殊2: fib?n=2 はHTTP-200を返す"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(response.status_code, 200)

    def test_get_n_3_response_ok(self):
        """通常1: fib?n=3 はHTTP-200を返す"""
        response = self.client.get("/fib?n=3")
        self.assertEqual(response.status_code, 200)

    def test_get_n_7_response_ok(self):
        """通常2: fib?n=7 はHTTP-200を返す"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(response.status_code, 200)
    
    def test_get_n_99_response_ok(self):
        """負荷: fib?n=99 はHTTP-200を返す"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(response.status_code, 200)

    # 正常系計算テスト
    def test_get_n_1_result_correct(self):
        """特殊1: fib?n=1 の答えが正しい"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)

    def test_get_n_2_result_correct(self):
        """特殊2: fib?n=2 の答えが正しい"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)
    
    def test_get_n_3_result_correct(self):
        """通常1: fib?n=3 の答えが正しい"""
        response = self.client.get("/fib?n=3")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 2)

    def test_get_n_7_result_correct(self):
        """通常2: fib?n=7 の答えが正しい"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 13)

    def test_get_n_99_result_correct(self):
        """負荷: fib?n=99 の答えが正しい"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 218922995834555169026)
    
    # 異常系レスポンステスト
    def test_post_response_method_not_allowed(self):
        """POSTリクエストはHTTP-405を返す"""
        response = self.client.post("/fib?n=7")
        self.assertEqual(response.status_code, 405)
        
    def test_get_n_none_validation(self):
        response = self.client.get("/fib")
        self.assertEqual(response.status_code, 400)
    
    def test_get_n_minus_validation(self):
        response = self.client.get("/fib?n=-5")
        self.assertEqual(response.status_code, 400)
    
    def test_get_n_0_validation(self):
        response = self.client.get("/fib?n=0")
        self.assertEqual(response.status_code, 400)
    
    def test_get_n_float_validation(self):
        response = self.client.get("/fib?n=1.1")
        self.assertEqual(response.status_code, 400)
    
    def test_get_n_str_validation(self):
        response = self.client.get("/fib?n=k")
        self.assertEqual(response.status_code, 400)        

    def test_get_invalid_key_validation(self):
        response = self.client.get("/fib?m=7")
        self.assertEqual(response.status_code, 400)
