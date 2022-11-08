from pathlib import Path

p = Path('./hw8/')
staff = p / 'staff.csv'
adress = p / 'adress.csv'
office = p / 'office.csv'

def input_data():
    item = dict()
    Id = count_data(staff) 
    item["id"] = Id
    item["surname"] = input('Введите Фамилию сотрудника: ')
    item["name"] = input('Введите Имя сотрудника: ')
    item["department"] = input('Введите Отдел сотрудника: ')
    item["position"] = input('Введите Должность сотрудника: ')
    item["city"] = input('Введите Город расположения офиса: ')
    item["street"] = input('Введите Улицу расположения офиса: ')
    item["house"] = input('Введите Номер дома расположения офиса: ')
    item["section"] = input('Введите Секцию расположения офиса: ')
    item["floor"] = input('Введите Этаж, на котором работает сотрудник: ')
    item["room"] = input('Введите Кабинет, в котором работает сотрудник: ')
    return item

def write_data(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")

def count_data(name):
    with open(name, 'r') as file:
        data = file.read()
    return data.count('\n')

def push_data():
    item = input_data()
    write_data([item.get("id"), item.get("surname"), item.get("name"), item.get("department"), item.get("position")], staff)
    write_data([item["id"], item["city"], item["street"], item["house"], item["section"]], adress)
    write_data([item["id"], item["floor"], item["room"]], office)