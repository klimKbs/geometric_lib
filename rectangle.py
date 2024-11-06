import unittest


def area(a, b):
    '''
    Возвращает площадь прямоугольника

        Параметры:
            a(int): длина прямоугольника
            b(int): ширина прямоугольника

        Возвращаемое значение:
            a * b: площадь прямоугольника
    '''
    return a * b


def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника

        Параметры:
            a(int): длина прямоугольника
            b(int): ширина прямоугольника

        Возвращаемое значение
            2 * (a + b): периметр прямоугольника
    '''
    return 2 * (a + b)


class RectangleTestCase(unittest.TestCase):
    def test_zero_mul(self):
        res = area(10, 0)
        self.assertEqual(res, 0)

    def test_square_mul(self):
        res = area(10, 10)
        self.assertEqual(res, 100)
    
    def test_perimeter_mul(self):
        res = perimeter(2, 5)
        self.assertEqual(res, 14)
    
    


