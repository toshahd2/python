import random
lst = [random.randint(1,9) for i in range(random.randint(4,10))]    
print(f"список:\n{lst}")

#использование list comprehension
multip = [lst[i] * lst[len(lst)-1-i] for i in range(0, len(lst)//2 + 1 if len(lst)%2 else len(lst)//2)]

print(f"произведение пар чисел списка:\n{multip}")