result = ""
number = int(input("Введите число: "))
while number != 0:
    result = str(number%2) + result
    number //=2
print(f"Число в двоичной форме: {result}")