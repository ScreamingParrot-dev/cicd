import unittest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Тест сложения"""
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
    
    def test_subtract(self):
        """Тест вычитания"""
        self.assertEqual(Calculator.subtract(10, 4), 6)
    
    def test_multiply(self):
        """Тест умножения"""
        self.assertEqual(Calculator.multiply(3, 4), 12)
    
    def test_divide(self):
        """Тест деления"""
        self.assertEqual(Calculator.divide(10, 2), 5)
        
        # Тест деления на ноль
        with self.assertRaises(ValueError):
            Calculator.divide(5, 0)
    
    def test_factorial(self):
        """Тест факториала"""
        self.assertEqual(Calculator.factorial(0), 1)
        self.assertEqual(Calculator.factorial(5), 120)
        
        # Тест отрицательного числа
        with self.assertRaises(ValueError):
            Calculator.factorial(-1)

if __name__ == '__main__':
    unittest.main()