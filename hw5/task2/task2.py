from pathlib import Path
from random import randint

p = Path('./hw5/task2/')
inputFile = p / 'input.txt'
outputFile = p / 'output.txt'

with open(inputFile, 'r') as data:
    candies = data.readlines()
candies = int(candies[0])

def suminput():
    sum = int(input('Сколько конфет возьмете? \n'))
    while not 0 < sum < 29:
        sum = int(input('Введите количество от 1 до 28 конфет: \n'))
    return sum

mode = int(input('Выбырите режим игры: \n1. 2 игрока \n2. С компьютером \nВведите цифру режима: '))

print(f"На столе {candies} конфет(-а).")

pl1 = "Игрок №1"
pl2 = "Игрок №2"

move = randint(0,2)
print(f"Первым ходит {pl1}.") if move else print(f"Первым ходит {pl2}.")

result1 = 0
result2 = 0

while candies > 28:
    if move:
        print(f"\nХодит {pl1}.") 
        sum1 = suminput()
        result1 += sum1
        candies -= sum1
        move = 0
        print(f"{pl1} взял {sum1} конфет(-ы), всего у игрока {result1} конфет(-ы).") 
    else:
        print(f"\nХодит {pl2}.") 
        sum2 = suminput() if mode == 1 else randint(1,29)
        result2 += sum2
        candies -= sum2
        move = 1
        print(f"{pl2} взял {sum2} конфет(-ы), всего у игрока {result2} конфет(-ы).") 
    print(f"На столе отсталось {candies} конфет(-а).")

if move:
    result = str(f"Выиграл {pl1}")
    print(result)
else:
    result = str(f"Выиграл {pl2}")
    print(result)

with open(outputFile, 'w') as data:
    data.write(result)