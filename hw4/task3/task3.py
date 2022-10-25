mylist = list(map(int, input("Введите числа для составления списка (пробел - разделитель): \n").split()))

result = []
[result.append(i) for i in mylist if i not in result]

print(f"Изначальный список: \n{mylist}")
print(f"Список без повторов: \n{result}")