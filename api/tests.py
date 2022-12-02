from django.test import TestCase

class FibonacciAPIViewTest(TestCase):
    """FibonacciAPIViewのテスト"""
    
    # 正常系特別: n=1のとき
    def test_get_n_1_response(self):
        """GET /fib?n=1 で200を返す"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(response.status_code, 200)

    def test_get_n_1_result(self):
        """GET /fib?n=1 で答えが正しい"""
        response = self.client.get("/fib?n=1")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)
    
    # 正常系特別: n=2のとき
    def test_get_n_2_response(self):
        """GET /fib?n=2 で200を返す"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(response.status_code, 200)
    
    def test_get_n_2_result(self):
        """GET /fib?n=2 で答えが正しい"""
        response = self.client.get("/fib?n=2")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 1)

    # 正常系: n=3 のとき
    def test_get_n_3_response(self):
        """GET /fib?n=3 で200を返す"""
        response = self.client.get("/fib?n=3")
        self.assertEqual(response.status_code, 200)
        
    def test_get_n_3_result(self):
        """GET /fib?n=3 で答えが正しい"""
        response = self.client.get("/fib?n=3")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 2)

    # 正常系: n=7 のとき
    def test_get_n_7_response(self):
        """GET /fib?n=7 で200を返す"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(response.status_code, 200)
        
    def test_get_n_7_result(self):
        """GET /fib?n=7 で答えが正しい"""
        response = self.client.get("/fib?n=7")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 13)    
    
    # 正常系負荷: n=99 のとき
    def test_get_n_99_response(self):
        """GET /fib?n=99 で200を返す"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(response.status_code, 200)

    def test_get_n_99_result(self):
        """GET /fib?n=99 で答えが正しい"""
        response = self.client.get("/fib?n=99")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 218922995834555169026)
    
    # 混合系: パラメータが複数あるが、n が含まれる
    def test_get_multiple_include_n_response(self):
        """
        GET /fib?n=4&m=7 で200を返す
        m は無視される
        """
        response = self.client.get("/fib?n=4&m=7")
        self.assertEqual(response.status_code, 200)
        
    def test_get_multiple_n_result(self):
        """
        GET /fib?n=4&m=7 で答えが正しい
        ただし、m は無視される
        """
        response = self.client.get("/fib?m=7&n=4")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 3)
    
    def test_get_multiple_include_n_space_response(self):
        """GET /fib?n= &m=7 で400を返す"""
        response = self.client.get("/fib?n= &m=7")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["n"][0], "有効な整数を入力してください。")   

    # 混合系: パラメータに n が複数ある
    def test_get_multiple_n_response(self):
        """GET /fib?n=1&n=5 で200を返す"""
        response = self.client.get("/fib?n=1&n=5")
        self.assertEqual(response.status_code, 200)        

    def test_get_multiple_n_result(self):
        """
        GET /fib?n=1&n=5 で答えが正しい
        n= は本来エラーになるが無視され、n=5 の答えが正しく表示される
        """
        response = self.client.get("/fib?n= &n=5")
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data["result"], 5)
   
    # 異常系: n が負のとき
    def test_get_n_minus_response(self):
        """GET /fib?n=-2 で400を返す"""
        response = self.client.get("/fib?n=-2")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["n"][0], "正の整数を入力してください。")
    
    # 異常系: n=0 のとき
    def test_get_n_0_response(self):
        """GET /fib?n=0 で400を返す"""
        response = self.client.get("/fib?n=0")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["n"][0], "正の整数を入力してください。")
    
    # 異常系: n が小数を含むとき
    def test_get_n_float_response(self):
        """GET /fib?n=1.1 で400を返す"""
        response = self.client.get("/fib?n=1.1")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["n"][0], "有効な整数を入力してください。")        

    # 異常系: n が数字以外のとき
    def test_get_n_alphabet_response(self):
        """GET /fib?n=k で400を返す"""
        response = self.client.get("/fib?n=k")
        self.assertEqual(response.status_code, 400)        
        self.assertEqual(response.data["n"][0], "有効な整数を入力してください。")   
        
    def test_get_n_japanese_response(self):
        """GET /fib?n=あ で400を返す"""
        response = self.client.get("/fib?n=あ")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["n"][0], "有効な整数を入力してください。")   

    # 異常系: リクエストパラメータがないとき
    def test_get_none_response(self):
        """GET /fib で400を返す"""
        response = self.client.get("/fib")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["n"][0], "この項目はnullにできません。")   
        
    # 異常系: リクエストパラメータに n が含まれないとき
    def test_get_invalid_key_response(self):
        """GET /fib?m=11 で400を返す"""
        response = self.client.get("/fib?m=11")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data["n"][0], "この項目はnullにできません。")

    # 異常系: POSTリクエストが送られた
    def test_post_none_response(self):
        """POST /fib （データなし）で405を返す（POSTリクエストは許されない）"""
        response = self.client.post("/fib")
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data["detail"], 'メソッド "POST" は許されていません。')
    
    def test_post_something_response(self):
        """POST /fib （データあり）で405を返す（POSTリクエストは許されない）"""
        response = self.client.post("/fib", {"n": 6})
        self.assertEqual(response.status_code, 405)
        self.assertEqual(response.data["detail"], 'メソッド "POST" は許されていません。')    
