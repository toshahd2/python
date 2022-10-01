print('Введите значение координаты точки по оси X: ')
x = int(input())
print('Введите значение координаты точки по оси Y: ')
y = int(input())

if x==0 or y==0:
    print(' Вы ввели нулевое значение, точка лежит на оси')
elif x>0 and y>0:
    print('1 четверть')
elif x>0 and y<0:
    print('2 четверть')
elif x<0 and y<0:
    print('3 четверть')
elif x<0 and y>0:
    print('4 четверть')