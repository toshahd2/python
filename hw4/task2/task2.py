number = int(input("Введите натуральное число: "))
while number < 1:
    number = int(input("Вы ввели не натуральное число, повторите ввод: "))

mylist = []

if number == 1:
    print(f"Простые множители числа {number} составляют: [1]")
else:
    for i in range (2, number+1):
        if number % i == 0:
            mylist.append(i)

    if len(mylist)%2 != 0:
        rang = int(len(mylist)//2 + 1)
    else:
        rang = int(len(mylist)//2)
    
    result = mylist.copy()
    
    for j in reversed(range(len(mylist))):
        for k in range (0, rang):
            if mylist[j] % mylist[k] == 0 and mylist[j] / mylist[k] != 1:
                result.remove(mylist[j])
                break
        
    print(f"Простые множители числа {number} составляют: {result}")