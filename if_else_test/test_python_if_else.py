import unittest
import python_if_else

class TestIfElse(unittest.TestCase):
    def test_if_else_func_case1(self):
        result = python_if_else.if_else_func()
        self.assertEqual(result,"Weird")        
    def test_if_else_func_case2(self):
        result = python_if_else.if_else_func()
        self.assertEqual(result,"Not Weird") 
    def test_if_else_func_case3(self):
        result = python_if_else.if_else_func()
        self.assertEqual(result,"Weird")
    def test_if_else_func_case4(self):
        result = python_if_else.if_else_func()
        self.assertEqual(result,"Not Weird")



