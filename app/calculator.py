class Calculator:
    @staticmethod
    def add(a, b):
        return a + b
    
    @staticmethod
    def subtract(a, b):
        return a - b
    
    @staticmethod
    def multiply(a, b):
        return a * b
    
    @staticmethod
    def divide(a, b):
        if b == 0:
            raise ValueError("Нельзя делить на ноль")
        return a / b
    
    @staticmethod
    def factorial(n):
        if n < 0:
            raise ValueError("Нельзя использовать отрицательные числа для факториала")
        if n == 0:
            return 1
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result