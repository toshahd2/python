import random
mylist = []

for i in range(random.randint(4,10)):
    mylist.append(random.randint(1,9))  
    
print(f"список:\n{mylist}")

multip = []

for i in range(0, int(len(mylist)/2)):
    multip.append(mylist[i] * mylist[len(mylist)-1-i])

print(f"произведение пар чисел списка:\n{multip}")