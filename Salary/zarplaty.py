# Created by Onufrak Yevgeniy
# TARgv21

# Создать два списка Люди и Запрлаты
# ЗАполнить списки значениями, введенными пользователями или случайным образом
# Добавить еще несколько человек и зарплат(кол-во говорит пользователь),
# Удалить человека и его зарплату(вводим имя),
# Самую большую зарплату и кто ее получает,
# Кто получает самую маленькую зарплату и какую именно,
# Упорядочить зарплаты в порядке возрастания и убывания вместе с именами,
# Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран.
# Сделать поиск зарплаты по имени человека. Учесть, что имена могут повторяться,
# Вывести список тех людей(с зарплатами), кто получает больше/меньше чем указанная сумма.
# Top3() - 3 самых бедных и самых богатых человека
# Keskmine() - Среднюю зарплату и имя человека ее получающего
# Tulumaks() - Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.
# Sort_nimi_jargi() - Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я или от Я до А)
# Kustutamine() - Находить тех кто получает зарплату ниже средней и удалить их из списков.
# Придумай свою функцию

import os # чтобы чистить консоль


r_names_list = ["Vasya", "Gena", "Lesha", "Jevgeniy","Dima","Mihail","Nikita","Lolita","Kolyan","Artem","Gosha"]
max_rand_salary = 15000
global inimesed
inimesed = ["A","B","C","D","E"]
global palgad
palgad = [1200,2500,750,395,1200]
import random
import string
l_counter = 0

def show_values(): #shows global names and salary
    for i in range(len(inimesed)):
        print(f"{inimesed[i]} : {palgad[i]}")
def fill_values(input_type): # Fill lines with manual or random values 

    if input_type == "R":
        while True: # amount for random 
            total_inimesed = input("Specify number of random values: ")
            if total_inimesed.isdigit() == True:
                total_inimesed = int(total_inimesed)
                break
            
        for i in range(total_inimesed):
            inimesed.append(r_names_list[random.randint(0,len(r_names_list)-1)])
            palgad.append(random.randint(0,max_rand_salary))                                 #
        
        show_values()
        print()

    elif input_type == "M":
        while True:
            new_name = input("Введите имя (Enter для выхода): ")
            if  new_name == "":
                print("Input process ended by user")
                break
            inimesed.append(new_name)

            new_salary = input("Введите зарплату у " + new_name + ": ")
            if new_salary.isdigit() == True:
                palgad.append(int(new_salary))
            else:
                palgad.append(0)
def delete_by_name(): #delete a position with name and salary
    
    
    d_nimi = input("Enter a name to delete: ")
    n = inimesed.count(d_nimi)
    if n <= 0:
        print("Такого имени нет в списке")
        return
    index_list = list()
    t = 0

    for e in range(len(inimesed)):
        if inimesed[e] == d_nimi:
            t += 1
            index_list.append(int(e))
            print(f"{t}. {inimesed[e]} : {palgad[e]}")
    if n > 1:
        while True:
            jar_no = input("Какой номер удалить?: ")
            if jar_no.isdigit() == True:
                jar_no = int(jar_no)
                break
        index_to_delete = index_list[jar_no - 1]
    else:
        index_to_delete = inimesed.index(d_nimi)

    print(f"{inimesed[index_to_delete]} с зарплатой {palgad[index_to_delete]} успешно удален.")
    inimesed.pop(index_to_delete)
    palgad.pop(index_to_delete) 
    
           
    print()
def sort_by_salary(sorting_order): 
    # sorting order 1 - возростание
    # sorting order 2 - убывание

    # идем по каждому значению из несортированного списка
    # добавляем значение в конец сортированного буфера
    # сравниваем с соседним значением
    # пока это значение меньше предидущего в листе - меняем эти значения 
    buf_names_list = []
    buf_salary_list = []
    for i in range(len(palgad)):
        #добавляем значение к листу
        buf_salary_list.append(palgad[i])
        buf_names_list.append(inimesed[i])

        for j in range(len(buf_salary_list)-1,0,-1):
            
            if buf_salary_list[j] < buf_salary_list[j-1]:
                # перемещаем в случае если новое (последнее) значение меньше предидущего
                sss = buf_salary_list[j-1]
                buf_salary_list[j-1] = buf_salary_list[j]
                buf_salary_list[j] = sss

                nnn = buf_names_list[j-1]
                buf_names_list[j-1] = buf_names_list[j]
                buf_names_list[j] = nnn
            
    if sorting_order == 2:
        buf_names_list.reverse()
        buf_salary_list.reverse()
        return buf_names_list, buf_salary_list
    elif sorting_order == 1:
        return buf_names_list, buf_salary_list
    else:
        return inimesed, palgad

def input_digit(show_string):
    while True:
        d = input(show_string)
        if d.isdigit() == True:
            return int(d)           
def minmax_salary(minormax):

    min_v = 2348234394
    max_v = 0
    min_i = 0
    max_i = 0

    for i in range(len(palgad)-1):
        if palgad[i] < min_v: # store min value and its address
            min_v = palgad[i]
            min_i = i
        if palgad[i] > max_v:
            max_v = palgad[i]
            max_i = i
    if minormax == "MIN":
        print(f"Самая маленькая зарплата у {inimesed[min_i]}. Он/она получает {palgad[min_i]}")
    elif minormax == "MAX":
        print(f"Самая большая зарплата у {inimesed[max_i]}. Он/она получает {palgad[max_i]}")
def dublicatedSalary():
    dublicatedIndexList = []
    for i in range(len(palgad)):
        if palgad.count(palgad[i]) > 1 and i not in dublicatedIndexList:
            
            for b in range(len(palgad)):
                if palgad[i] == palgad[b]:
                    dublicatedIndexList.append(b)
    if len(dublicatedIndexList) > 0:
        for c in dublicatedIndexList:
            print(f"{inimesed[int(c)]} : {palgad[int(c)]}")
    else:
        print("Нет повторяющихся значений")        
def findByName():
    name = input("Введите имя человека: ")
    indexBufferList = []

    for i in range(len(inimesed)):
        if inimesed[i] == name:
            indexBufferList.append(int(i))
    
    if len(indexBufferList) > 0:
        for c in indexBufferList:
            print(f"{inimesed[int(c)]} : {palgad[int(c)]}")
    else:
        print("Нет таких людей") 
def showMoreThen():

    key_value = input_digit("Введите число: ")
    order = input_digit("1 - показать меньшие значения\n2 - показать большие значения: ")
    
    if order == 1:
        for i in range(len(palgad)):
            if palgad[i] <  key_value:
                print(f"{inimesed[i]} : {palgad[i]}")
    elif order == 2:
        for i in range(len(palgad)):
            if palgad[i] >=  key_value:
                print(f"{inimesed[i]} : {palgad[i]}")
    else:
        return

def top3Salary():
    # алгоритм сортировки
    buf_names_list = []
    buf_salary_list = []
    for i in range(len(palgad)-1):
        #добавляем значение к листу
        buf_salary_list.append(palgad[i])
        buf_names_list.append(inimesed[i])

        for j in range(len(buf_salary_list)-1,0,-1):
            
            if buf_salary_list[j] < buf_salary_list[j-1]:
                # перемещаем в случае если новое (последнее) значение меньше предидущего
                sss = buf_salary_list[j-1]
                buf_salary_list[j-1] = buf_salary_list[j]
                buf_salary_list[j] = sss

                nnn = buf_names_list[j-1]
                buf_names_list[j-1] = buf_names_list[j]
                buf_names_list[j] = nnn
    
    if(len(buf_salary_list) >= 3):
        num = 3
    else: 
        num = len(buf_salary_list)
    print(f"{num} самых бедных: ")
    for i in range(3):
        print(f"{buf_names_list[i]} с зарплатой {buf_salary_list[i]}")
    print(f"{num} самых богатых: ")
    buf_names_list.reverse()
    buf_salary_list.reverse()
    for i in range(3):
        print(f"{buf_names_list[i]} с зарплатой {buf_salary_list[i]}")
def averSalary():
    suma = 0
    for i in palgad:
        suma += i
    averValue = suma/len(palgad)
    print(f"Средняя зарплата {averValue}")
    for palk in palgad:
        if palk == averValue:
            n = palgad.index(palk)
            print(f"{inimesed[n]} получает среднюю зарплату")
    if palgad.count(averValue) <= 0:
        print("Нет тех кто получает точно среднюю зарплату")  
def calculateTax():
    name = input("Введите имя получающего зарплату: ")
    # Поиск имен 
    index_buf = []
    for i in range(len(inimesed)):
        if inimesed[i] == name:
            index_buf.append(int(i))
    
    for j in index_buf:
        
        thisSalary = palgad[j]
        if thisSalary <= 1200:
            excludeTax = 500
        elif thisSalary < 2100:
            excludeTax = 500 - 0.55556*(thisSalary - 1200) 
        elif thisSalary >= 2100:
            excludeTax = 0  

        calculated_tax = (thisSalary - excludeTax) * 0.2
        
        print(f"{inimesed[j]} получит {thisSalary - calculated_tax} после вычета налогов")    
    
def sortByName():
    sorting_order = input_digit("1 для сортировки от A до Я\n2 для сортировки Я - А")
    if sorting_order not in [1,2]:
        return inimesed, palgad

    buf_names_list = []
    buf_salary_list = []
    for i in range(len(inimesed)):
        #добавляем значение к листу
        buf_salary_list.append(palgad[i])
        buf_names_list.append(inimesed[i])

        for j in range(len(buf_names_list)-1,0,-1):
            
            if buf_names_list[j] < buf_names_list[j-1]:
                # перемещаем в случае если новое (последнее) значение меньше предидущего
                sss = buf_salary_list[j-1]
                buf_salary_list[j-1] = buf_salary_list[j]
                buf_salary_list[j] = sss

                nnn = buf_names_list[j-1]
                buf_names_list[j-1] = buf_names_list[j]
                buf_names_list[j] = nnn
            
    if sorting_order == 2:
        buf_names_list.reverse()
        buf_salary_list.reverse()
        return buf_names_list, buf_salary_list
    elif sorting_order == 1:
        return buf_names_list, buf_salary_list
    else:
        return inimesed, palgad



def menu():
    
    functionsList = []
    functionsList.append("Заполнить рандомными значениями")
    functionsList.append("Ввести имена и зарплаты вручную")
    functionsList.append("Показать зарплаты")
    functionsList.append("Удалить человека и его зарплату(вводим имя)")
    functionsList.append("Самую большую зарплату и кто ее получает")
    functionsList.append("Кто получает самую маленькую зарплату и какую именно")
    functionsList.append("Упорядочить зарплаты в порядке возрастания и убывания вместе с именами")
    functionsList.append("Узнать, кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран")
    functionsList.append("Поиск зарплаты по имени человека")
    functionsList.append("Вывести список тех людей(с зарплатами), кто получает больше/меньше чем указанная сумма")
    functionsList.append("3 самых бедных и самых богатых человека")
    functionsList.append("Среднюю зарплату и имя человека ее получающего")
    functionsList.append("Вычислить зарплату, которую человек получит на руки после вычисления подоходного налога.")
    functionsList.append("Осуществить сортировку по имени (можно предостваит пользователю выбор от А до Я или от Я до А)")
    functionsList.append("Находить тех кто получает зарплату ниже средней и удалить их из списков.")
    
    print("Выбери функцию: ")
    for i in range(len(functionsList)-1):       
        print(f"{i + 1}. {functionsList[i]}")

    while True:
        b = input("Выбери функцию: ").upper()
        try:
            b = int(b)
            if b in range(len(functionsList)):
                os.system('cls' if os.name == 'nt' else 'clear')
                print(functionsList[b-1])
                return b
        except:
            ValueError
            
        

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    input_type = menu()
    
    if input_type == 1:
        fill_values("R")
    elif input_type == 2:
        fill_values("M")
    elif input_type == 3: # показать значения
        show_values()
    elif input_type == 4: # удалить по имени пержде показать значения
        show_values()
        delete_by_name()
    elif input_type == 5: # самая большая зарплата
        minmax_salary("MAX")
    elif input_type == 6: # самая маленькая зарплата
        minmax_salary("MIN")
    elif input_type == 7: # сортировка
        inimesed, palgad = sort_by_salary(input_digit("1 для сортировки по возростанию или 2 для сортировки по убыванию: "))
        show_values()
    elif input_type == 8: # кто получает одинаковую зарплату, найти сколько таких людей вывести их данные на экран
        dublicatedSalary()
    elif input_type == 9: # Поиск зарплаты по имени человека
        findByName()
    elif input_type == 10: # Вывести список тех людей(с зарплатами), кто получает больше/меньше чем указанная сумма
        showMoreThen()
    elif input_type == 11:# 3 самых бедных и самых богатых человека
        top3Salary()
    elif input_type == 12: # средняя зарплата
        averSalary()
    elif input_type == 13: # вычислить нетто зарплату
        calculateTax()
    elif input_type == 14: # сортировка по имени
        inimesed, palgad = sortByName()
        show_values()
    else:
        break #end programm
    print()
    input("Press enter to show menu")










