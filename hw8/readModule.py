from pathlib import Path

p = Path('./hw8/')
staff = p / 'staff.csv'
adress = p / 'adress.csv'
office = p / 'office.csv'

def read_data():
    staffList = []
    with open(staff, 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            staffList.append(temp)
    adressList = []
    with open(adress, 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            adressList.append(temp)

    officeList = []
    with open(office, 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            officeList.append(temp)

    lst = []
    for i in range(len(staffList)):
        lst.append([staffList[i][0], staffList[i][1], staffList[i][2], staffList[i][3], staffList[i][4], \
            officeList[i][1], officeList[i][2], adressList[i][1], adressList[i][2], adressList[i][3], adressList[i][4]])
    return lst