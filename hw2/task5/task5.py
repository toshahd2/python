import random
mylist = []

for i in range(random.randint(4,10)):
    mylist.append(random.randint(1,9))  
    
print(f"список:\n{mylist}")
random.shuffle(mylist)
print(f"перемешивание списка:\n{mylist}")