from pathlib import Path

p = Path('./hw5/task4/')
dec = p / 'decoded.txt'
cod = p / 'coded.txt'

def coding(text):
    count = 1
    result = ''
    for i in range(len(text)-1):
        if text[i] == text[i+1]:
            count += 1
        else:
            result = result + str(count) + text[i]
            count = 1
    if count > 1 or (text[len(text)-2] != text[-1]):
        result = result + str(count) + text[-1]
    return result

def decoding(text):
    number = ''
    result = ''
    for i in range(len(text)):
        if not text[i].isalpha():
            number += text[i]
        else:
            result = result + text[i] * int(number)
            number = ''
    return result

print(f"Если вам требуется шифровка, то положите данные в файл decoded и нажмите 1")
print(f"Если вам требуется дешифровка, то положите данные в файл decoded и нажмите 2")
mode = int(input("Введите режим: "))
while not 0 < mode < 3:
        mode = int(input('Некорректный режим, повторите ввод: '))

if mode == 1:
    with open(dec, 'r') as data:
        text = data.readlines()
    newtext = str(coding(text[0]))
    print(newtext)
    with open(cod, 'w') as data:
        data.write(newtext)
else:
    with open(cod, 'r') as data:
        text = data.readlines()
    newtext = str(decoding(text[0]))
    print(newtext)
    with open(dec, 'w') as data:
        data.write(newtext)