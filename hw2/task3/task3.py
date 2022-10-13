number = int(input('Введите число: ')) 
mylist = []

for i in range(1, number + 1):
    mylist.append(round((1 + 1 / i) ** i, 2))        

print(mylist)
print(round(sum(mylist), 2))