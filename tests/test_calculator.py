"""
Unit tests for Calculator class
"""
import unittest
from app.calculator import Calculator

class TestCalculator(unittest.TestCase):
    
    def test_add(self):
        """Test addition method"""
        self.assertEqual(Calculator.add(2, 3), 5)
        self.assertEqual(Calculator.add(-1, 1), 0)
        self.assertEqual(Calculator.add(0, 0), 0)
    
    def test_subtract(self):
        """Test subtraction method"""
        self.assertEqual(Calculator.subtract(10, 4), 6)
        self.assertEqual(Calculator.subtract(5, 5), 0)
    
    def test_multiply(self):
        """Test multiplication method"""
        self.assertEqual(Calculator.multiply(3, 4), 12)
        self.assertEqual(Calculator.multiply(0, 5), 0)
    
    def test_divide(self):
        """Test division method"""
        self.assertEqual(Calculator.divide(10, 2), 5)
        self.assertEqual(Calculator.divide(5, 2), 2.5)
        
        # Test division by zero
        with self.assertRaises(ValueError):
            Calculator.divide(5, 0)
    
    def test_factorial(self):
        """Test factorial method"""
        self.assertEqual(Calculator.factorial(0), 1)
        self.assertEqual(Calculator.factorial(1), 1)
        self.assertEqual(Calculator.factorial(5), 120)
        
        # Test negative number
        with self.assertRaises(ValueError):
            Calculator.factorial(-1)

# Это нужно для запуска тестов через pytest
if __name__ == '__main__':
    unittest.main()