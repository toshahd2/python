import random
mylist = []

for i in range(random.randint(4,10)):
    mylist.append(random.randint(1,9))  
    
print(f"список:\n{mylist}")

sum = 0

for i in range(0, len(mylist)):
    if i%2>0:
        sum+=mylist[i]
        i += 1

print('Сумма элементов списка, стоящих на нечётной позиции равна', sum)