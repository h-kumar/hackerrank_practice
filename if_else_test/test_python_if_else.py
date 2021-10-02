import unittest
import python_if_else

class TestIfElse(unittest.TestCase):
    def test_if_else_func_1(self):
        result = python_if_else.if_else_func()
        self.assertEqual(result,"Weird")        
    def test_if_else_func_2(self):
        result = python_if_else.if_else_func()
        self.assertEqual(result,"Not Weird")   



