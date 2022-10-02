print('Введите координаты точки A: ')
a_x = float(input('x = '))
a_y = float(input('y = '))
print('Введите координаты точки B: ')
b_x = float(input('x = '))
b_y = float(input('y = '))
import math
from re import A
print('Расстояние между точками A(', a_x, ',', a_y, ') и B(', b_x, ',', b_y, ') составляет ', round(math.sqrt(pow(b_x - a_x, 2)+ pow(b_y - a_y, 2)), 2))