number = input('Введите число: ')

def num_sum(number):
    if float(number) < 0:
        number = float(number) * (-1)

    sum = 0

    for i in str(number):
        if i != '.':
            print(i)
            sum += int(i)
            print(sum)
    return sum

print(f'Сумма чисел равна {num_sum(number)}')