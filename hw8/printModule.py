
def print_data(data, search = False):
    if len(data) > 0:
        print("id".ljust(5), "Фамилия".ljust(12), "Имя".ljust(12), "Отдел".ljust(12), "Должность".ljust(12), \
        "Город".ljust(12), "Улица".ljust(12), "Дом".ljust(6), "Секция".ljust(6), "Этаж".ljust(6), "Кабинет")
        if not search:
            del data[0]
        for content in data:
            print(content[0].ljust(5), content[1].ljust(12), content[2].ljust(12), content[3].ljust(12), \
                content[4].ljust(12), content[7].ljust(12), content[8].ljust(12), content[9].ljust(6), \
                    content[10].ljust(6), content[5].ljust(6), content[6])
    else:
        print("\n")