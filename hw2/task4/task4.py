from pathlib import Path
import random

number = int(input('Введите число: ')) 
mylist = []

for i in range(-number, number + 1):
    mylist.append(i)        

print(mylist)


p = Path('./hw2/task4/')
file = p / 'file.txt'
with open(file, 'w') as data:
    data.write(f'{random.randrange(0, len(mylist)-1)}\n')
    data.write(f'{random.randrange(0, len(mylist)-1)}')

index = []
with open(file) as f:
    index = list(map(int,f.readlines()))

print('Произведение элементов на позициях', index[0],'(число',mylist[index[0]],') и', index[1],'(число',mylist[index[1]],') =', mylist[index[0]]*mylist[index[1]])