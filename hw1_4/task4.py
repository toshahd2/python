n = int(input('введите номер четверти: '))
if not (0 < n < 5):
    print('Некорректный номер четверти')
elif n==1:
    print('x>0 и y>0')
elif n==2:
    print('x>0 и y<0')
elif n==3:
    print('x<0 и y<0')
elif n==4:
    print('x<0 и y>0')  