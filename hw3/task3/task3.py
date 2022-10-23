import random
mylist = []

for i in range(random.randint(4,10)):
    mylist.append(round(random.uniform(1,9), 2))  
    
print(f"список:\n{mylist}")

min = mylist[0]
max = mylist[0]

for i in range(0,len(mylist)):
    if min > mylist[i]:
        min = mylist[i]
    if max < mylist[i]:
        max = mylist[i]

print(f"min: {min}")
print(f"max: {max}")

result = round((max % 1) - (min % 1),2)
print(f"Разница между максимальным и минимальным значением дробной части элементов:\n{result}")