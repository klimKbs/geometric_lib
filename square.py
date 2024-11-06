import unittest


def area(a):
    '''
    Возвращает площадь квадрата
    
        Параметры:
            a(int): длина и ширина квадрата
        
        Возвращаемое значение:
            a * a: площадь квадрата
    '''
    return a * a
    
    
def perimeter(a):
    '''
    Возвращает периметр квадрата
    
        Параметры:
            a(int): длина и ширина квадрата
    
        Возвращаемое значение:
            4 * a: периметр квадрата
    '''
    return 4 * a


class SquareTestCase(unittest.TestCase):
    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 100)
    
    def test_perimeter_mul(self):
        res = perimeter(5)
        self.assertEqual(res, 20)
    
