from pathlib import Path
from random import randint

p = Path('./hw5/task3/')
inputFile = p / 'input.txt'
outputFile = p / 'output.txt'

with open(inputFile, 'r') as data:
    board = data.readlines()
board = board[0].split(' ')
board = list(map(int, board))

def printBoard(board):
    print(f"\n\t{board[0]} | {board[1]} | {board[2]}")
    print(f"\t---------")
    print(f"\t{board[3]} | {board[4]} | {board[5]}")
    print(f"\t---------")
    print(f"\t{board[6]} | {board[7]} | {board[8]}\n")


pl1 = input('Игрок №1, введите ваше имя: ')
pl2 = input('Игрок №2, введите ваше имя: ')
fig1 = "x"
fig2 = "o"
finish = False
count = 0
moveList = []
move = randint(0,1)
if not move:
    temp = fig1
    fig1 = fig2
    fig2 = temp

print(f"\nКрестики-нолики. Первым ходит {pl1}. Ваш знак {fig1}.") if move else print(f"Крестики-нолики. Первым ходит {pl2}. Ваш знак {fig2}.")

printBoard(board)

while count < 9:
    if move:
        i = int(input('Введите номер ячейки: '))
        while i in moveList:
            i = int(input('Ячейка занята. Введите номер ячейки: '))
        print(i)
        board[i-1] = fig1
        count += 1
        move = 0
        print(f"\n{pl2}, Ваш ход.")
        printBoard(board)
    else:
        j = int(input('Введите номер ячейки: '))
        while j in moveList:
            j = int(input('Ячейка занята. Введите номер ячейки: '))
        board[j-1] = fig2
        count += 1
        move = 1
        print(f"\n{pl1}, Ваш ход.")
        printBoard(board)

if count == 9:
    if board[0] == board[1] == board[2] \
        or board[3] == board[4] == board[5] \
        or board[6] == board[7] == board[8] \
        or board[0] == board[3] == board[6] \
        or board[1] == board[4] == board[7] \
        or board[2] == board[5] == board[8] \
        or board[0] == board[4] == board[8] \
        or board[6] == board[4] == board[2]:
        if move == 1:
            result = str(f"\nПобедил {pl1}!")
        else:
            result = str(f"\nПобедил {pl2}!")
    else:
        result = str("Никто не победил, игра закончена!")
    print(result)
    with open(outputFile, 'w') as data:
        data.write(result)
        data.write(f"\n\t{board[0]} | {board[1]} | {board[2]}")
        data.write(f"\n\t---------")
        data.write(f"\n\t{board[3]} | {board[4]} | {board[5]}")
        data.write(f"\n\t---------")
        data.write(f"\n\t{board[6]} | {board[7]} | {board[8]}")
