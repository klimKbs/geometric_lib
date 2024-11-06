import unittest


def area(a, h):
    '''
    Возвращает площадь треугольника
    
        Параметры:
            a (int): основание
            h (int): высота
    
    
        Возвращаемое значение:
            a * h / 2: площадь треугольника
    '''
    return a * h / 2
    
    
def perimeter(a, b, c):
    '''
    Возвращает периметр треугольника
    
        Параметрв:
            a (int), b (int), c (int): стороны треугольника
    
        Возвращаемое значение:
            a + b + c: периметр треугольника
    '''
    return a + b + c


class SquareTestCase(unittest.TestCase):
    def test_area_mul(self):
        res = area(10, 5)
        self.assertEqual(res, 25)
    
    def test_perimeter_mul(self):
        res = perimeter(5, 3, 4)
        self.assertEqual(res, 12)
    

