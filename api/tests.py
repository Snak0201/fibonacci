"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase

class FibonacciAPIViewTest(TestCase):
    """FibonacciAPIViewのテスト"""
    
    # 正常系特別: n=1のとき
    def test_get_n_1_response_ok(self):
        """GET /fib?n=1 で200を返す"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(response.status_code, 200)
        
    def test_get_n_1_result_correct(self):
        """GET /fib?n=1 で答えが正しい"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)
    
    # 正常系特別: n=2のとき
    def test_get_n_2_response_ok(self):
        """GET /fib?n=2 で200を返す"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(response.status_code, 200)
    
    def test_get_n_2_result_correct(self):
        """GET /fib?n=2 で答えが正しい"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)

    # 正常系: n=3 のとき
    def test_get_n_3_response_ok(self):
        """GET /fib?n=3 で200を返す"""
        response = self.client.get("/fib?n=3")
        self.assertEqual(response.status_code, 200)
        
    def test_get_n_3_result_correct(self):
        """GET /fib?n=3 で答えが正しい"""
        response = self.client.get("/fib?n=3")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 2)

    # 正常系: n=7 のとき
    def test_get_n_7_response_ok(self):
        """GET /fib?n=7 で200を返す"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(response.status_code, 200)
        
    def test_get_n_7_result_correct(self):
        """GET /fib?n=7 で答えが正しい"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 13)    
    
    # 正常系負荷: n=99 のとき
    def test_get_n_99_response_ok(self):
        """GET /fib?n=99 で200を返す"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(response.status_code, 200)

    def test_get_n_99_result_correct(self):
        """GET /fib?n=99 で答えが正しい"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 218922995834555169026)
    
    # 混合系: パラメータが複数あるが、n が含まれる
    # 混合系: パラメータに n が複数ある
    
    # 異常系: n が負のとき
    def test_get_n_minus_validation(self):
        response = self.client.get("/fib?n=-5")
        self.assertEqual(response.status_code, 400)
    
    # 異常系: n=0 のとき
    def test_get_n_0_validation(self):
        response = self.client.get("/fib?n=0")
        self.assertEqual(response.status_code, 400)
    
    # 異常系: n が小数を含むとき
    def test_get_n_float_validation(self):
        response = self.client.get("/fib?n=1.1")
        self.assertEqual(response.status_code, 400)
    
    # 異常系: n が数字以外のとき
    def test_get_n_str_validation(self):
        response = self.client.get("/fib?n=k")
        self.assertEqual(response.status_code, 400)        

    # 異常系: リクエストパラメータがないとき
    def test_get_none_validation(self):
        response = self.client.get("/fib")
        self.assertEqual(response.status_code, 400)

    # 異常系: リクエストパラメータに n が含まれないとき
    def test_get_invalid_key_validation(self):
        response = self.client.get("/fib?m=7")
        self.assertEqual(response.status_code, 400)
    
    # 異常系: POSTリクエストが送られた
    def test_post_response_method_not_allowed(self):
        """POST /fib?n=7 で405を返す（POSTリクエストは許されない）"""
        response = self.client.post("/fib?n=7")
        self.assertEqual(response.status_code, 405)
