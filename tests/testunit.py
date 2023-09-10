import unittest
import tkinter as tk
import sys
import os

current_dir = os.path.dirname(__file__)
code_path = os.path.join(current_dir, '..', "src")
sys.path.append(code_path)

from standard import Standard

class test(unittest.TestCase):
    def setUp(self):
        root = tk.Tk()
        self.standard = Standard(root)
        self.standard.mode = Standard.active_mode
    
    def test_no_exist_operator_no_input_no_expression(self):
        self.standard.input['text'] = ""
        self.standard.expresion['text'] = ""
        self.standard.common_operator_func(20)
        self.assertEqual(self.standard.input['text'],'')
        self.assertEqual(self.standard.expresion['text'],'')

if __name__ == "__main__":
    unittest.main()
