# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

from random import randint
from math import sqrt

print("ЗАДАЧА 1")

class Triangle:

    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        print("Координаты точек вершин треугольника:")
        print("  A: x1 = {}, y1 = {}".format(self.x1, self.y1))
        print("  B: x2 = {}, y2 = {}".format(self.x2, self.y2))
        print("  C: x3 = {}, y3 = {}".format(self.x3, self.y3))

    def s_calc(self):
        #Площадь треугольника 
        #Пусть точки A1(x1; y1), A2(x2; y2), A3(x3; y3) - вершины треугольника,
        # тогда его площадь выражается формулой:
        # S = 1/2 |(x1−x3)(y2−y3)−(x2−x3)(y1−y3)| 
        s = 0.5 * (((self.x1 - self.x3) * (self.y2 - self.y3)) - ((self.x2 - self.x3) * (self.y1 - self.y3)))
        if s < 0:
            s = s * -1
        return int(s)

    def p_calc(self):
        #для стороны АВ проекции на оси абсцисс и ординат будут иметь длины X₂-X₁ и Y₂-Y₁,
        #а длина самой стороны в соответствии с теоремой Пифагора будет равна АВ = √((X₂-X₁)² + (Y₂-Y₁)²).
        #Длины двух других сторон, рассчитанные через их проекции на оси координат,
        #можно записать так: ВС = √(( X₃-X₂)² + (Y₃-Y₂)²), СА = √((X₃-X₁)² + (Y₃-Y₁)²).
        ab = sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2)
        bc = sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2)
        ca = sqrt((self.x3 - self.x1)**2 + (self.y3 - self.y1)**2)
        p = ab + bc + ca
        return int(p)

    def info(self):
        n1 = self.s_calc()
        n2 = self.p_calc()
        print("Площадь: ", n1)
        print("Периметр: ", n2)
        print("Высота: ")
        return

print("--------------Характеристики треугольника--------------")
print()
print("Генерируем случайные координаты......")
triangle1 = Triangle(randint(0, 100), randint(-20, 100),
                     randint(0, 100), randint(-20, 100),
                     randint(0, 100), randint(-20, 100))
print()
print("Характеристики треугольника:")
triangle1.info()
print()
print("-------------------------------------------------------")
print()
print()

# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.
print("ЗАДАЧА 2")

class Trapeze:

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
        self.x3 = x3
        self.y3 = y3
        self.x4 = x4
        self.y4 = y4
        print("Координаты точек трапеции:")
        print("  A: x1 = {}, y1 = {}".format(self.x1, self.y1))
        print("  B: x2 = {}, y2 = {}".format(self.x2, self.y2))
        print("  C: x3 = {}, y3 = {}".format(self.x3, self.y3))
        print("  D: x4 = {}, y4 = {}".format(self.x4, self.y4))

    def param_calc(self):
        ab = int(sqrt((self.x2 - self.x1)**2 + (self.y2 - self.y1)**2))
        bc = int(sqrt((self.x3 - self.x2)**2 + (self.y3 - self.y2)**2))
        cd = int(sqrt((self.x4 - self.x3)**2 + (self.y4 - self.y3)**2))
        ad = int(sqrt((self.x4 - self.x1)**2 + (self.y4 - self.y1)**2))
        if ab == cd:
            p = ab + bc + cd + ad
            s = (ad+bc)/2* (sqrt(ab**2- (((ad-bc)**2)/4 )))
            print("Tрапеция равнобочная, произведем вычисления:")
            print()
            print("Длины сторон:\n  сторона AB: {}\n  сторона BC: {}\n  сторона CD: {}\n  сторона AD: {}".format(ab, bc, cd, ad))
            print("Площадь трапеци: {}\nПериметр трапеции: {}".format(int(s), int(p)))
        else:
            print("Трапеция не равнобочная! Расчеты не производятся!")

print("--------------Характеристики трапеции------------------")
print("Генерируем случайные координаты......")
trap1 = Trapeze(randint(0, 10), randint(0, 10),
                     randint(0, 10), randint(0, 10),
                     randint(0, 10), randint(0, 10),
                     randint(0, 10), randint(0, 10))
trap1.param_calc()
print()
print()
trap2 = Trapeze(1, 2, 2, 5, 6, 5, 7, 2) #Здесь специально трапеция с фиксированными,
                                        #координатами, чтобы проверить, отработает ли
                                        #проверка на равнобочую трапецию
trap2.param_calc()
print()
print("-------------------------------------------------------")
print()
