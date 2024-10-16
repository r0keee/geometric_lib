def area(a, b):
    '''
    Возвращает площадь прямоугольника со сторонами a, b.
        Параметры:
            a (int или float): одна сторона прямоугольника
            b (int или float): другая стороная прямоугольника
        Возвращаемое значение:
            int или float: площадь прямоугольника со сторонами a, b.

    >>> area(2, 3)
    6
    '''
    return a * b

def perimeter(a, b):
    '''
    Возвращает периметр прямоугольника со сторонами a, b.
        Параметры:
            a (int или float): одна сторона прямоугольника
            b (int или float): другая стороная прямоугольника
        Возвращаемое значение:
            int или float: периметр прямоугольника со сторонами a, b.

    >>> area(2, 3)
    10
    '''
    return 2*(a + b)
