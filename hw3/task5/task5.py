def Fib(n):
    if n == 1 or n == 2:                       
        return 1
    else:
        return Fib(n-1) + Fib(n-2)

def NegFib(n):
    if n == 1:                       
        return 1
    elif n == 2:                       
        return -1
    else:
        num1 = 1
        num2 = -1
        for i in range(2, n):
            num1, num2 = num2, num1 - num2
        return num2

mylist = []
number = int(input('Введите число: '))
for i in range(1, number + 1):
    mylist.append(NegFib(i))
mylist.reverse()
mylist.append(0)
for i in range(1, number + 1):
    mylist.append(Fib(i))
print(mylist)