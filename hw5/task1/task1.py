from pathlib import Path

p = Path('./hw5/task1/')
input = p / 'input.txt'
output = p / 'output.txt'

def textFilter(str):
    return False if 'АБВ' in str else True

with open(input, 'r') as data:
    text = data.readlines()
print(f"Изначальный текст: \n{text}")

text = text[0].replace('.', ' . ').split()
text = list(filter(textFilter, text))
space = ' '
text = [space.join(text)]
text = text[0].replace(' .', '.')
print(f"Итоговый текст: \n{text}")

with open(output, 'w') as data:
    data.write(text)