import unittest
import math


def area(r):
    '''
    Возвращает площадь круга
    
        Параметры:
            r (int): радиус
            
        Возвращаемое значение:
            math.pi * r * r: площадь круга
    '''
    return math.pi * r * r
    
    
def perimeter(r):
    '''
    Возвращает периметр круга
    
        Параметры:
            r(int): радиус
            
        Возвращаемое значение:
            2 * math.pi * r: периметр круга
    '''
    return 2 * math.pi * r


class SquareTestCase(unittest.TestCase):
    def test_square_mul(self):
        res = area(10)
        self.assertEqual(res, 314.1592653589793)
    
    def test_perimeter_mul(self):
        res = perimeter(5)
        self.assertEqual(res, 31.41592653589793)
    
