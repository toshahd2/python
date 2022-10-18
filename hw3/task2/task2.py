import random
mylist = []

for i in range(random.randint(4,10)):
    mylist.append(random.randint(1,9))  
    
print(f"список:\n{mylist}")

multip = []

if len(mylist)%2 != 0:
    rang = len(mylist)//2 + 1
else:
    rang = len(mylist)//2
for i in range(0, rang):
    multip.append(mylist[i] * mylist[len(mylist)-1-i])

print(f"произведение пар чисел списка:\n{multip}")