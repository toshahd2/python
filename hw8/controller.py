from readModule import *
from printModule import *
from searchModule import *
from inputModule import *

def start():
    print("\nВыберите действие информационной системы:\n\
    1. получить всю информацию о сотрудниках\n\
    2. добавить сотрудника\n\
    3. поиск сотрудника")
    mode = input("Введите цифру: ")
    while True:
        if mode == '1':
            data = read_data()
            print_data(data)
            start()
        elif mode == '2':
            push_data()
            start()
        elif mode == '3':
            info = input("Введите данные для поиска: ")
            data = read_data()
            item = search_data(info, data)
            if item != None:
                print_data(item, True)
            else:
                print("Информация не найдена")                
            start()
        else:
            print("Вы ввели некорректную цифру, повторите ввод:")
            start()