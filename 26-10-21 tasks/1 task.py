# Создать два списка Люди и Запрлаты
# ЗАполнить списки значениями, введенными пользователями или случайным образом
# 
# 
r_names_list = ["Vasya", "Gena", "Lesha", "Jevgeniy","Dima","Mihail","Nikita","Lolita","Kolyan","Artem","Gosha"]
max_rand_salary = 15000
global inimesed
inimesed = []
global palgad
palgad = []
import random
import string
l_counter = 0
from module1 import*
global input_type

def fill_values():

    if input_type == "R":
        while True: # amount for random 
            total_inimesed = input("Specify number of random values: ")
            if total_inimesed.isdigit() == True:
                total_inimesed = int(total_inimesed)
                break
            
        for i in range(total_inimesed):
            inimesed.append(r_names_list[random.randint(0,len(r_names_list)-1)])
            palgad.append(random.randint(0,max_rand_salary))                                 #
        
        show_values(inimesed,palgad)
        print()

    elif input_type == "M":
        while True:
            new_name = input("Enter a name: (or press enter for exit)")
            if  new_name == "":
                print("Input process ended by user")
                break
            inimesed.append(new_name)

            new_salary = input("Enter " + new_name + "`s salary: ")
            if new_salary.isdigit() == True:
                palgad.append(int(new_salary))
            else:
                palgad.append(0)
def delete_by_name(): #delete a position with name and salary
    d_nimi = input("Enter a name to delete: ")
    n = inimesed.count(d_nimi)
    index_list = []
    t = 0

    for e in range(len(inimesed)):
        if inimesed[e] == d_nimi:
            t += 1
            index_list.append(int(e))
            print(f"{t}.{inimesed[e]} : {palgad[e]}")
    while True:
        jar_no = input("Line number to delete: ")
        if jar_no.isdigit() == True:
            jar_no = int(jar_no)

            break
    index_to_delete = index_list[jar_no - 1]
    print(f"{inimesed[index_to_delete]} with salary {palgad[index_to_delete]} deleted")
    inimesed.pop(index_to_delete)
    palgad.pop(index_to_delete)        
    print()
def sort_by_salary():
    # идем по каждому значению из несортированного списка
    # добавляем значение в конец сортированного буфера
    # сравниваем с соседним значением
    # пока это значение меньше предидущего в листе - меняем эти значения 
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



    return buf_names_list, buf_salary_list
            
            




while True:
    print("Menu: (press enter for exit)")
    print("R for random fill")
    print("M for manual salary input")
    print("S to show names and salary")
    print("D to delete by name")
    print("R for random fill")
    print("Sort for sorting by salary")

    input_type = input("Enter a option : ").upper()
    if input_type in ["R", "M"]:
        fill_values()
    elif input_type == "S":
        show_values(inimesed,palgad)
    elif input_type == "D":
        delete_by_name()
    elif input_type == "SORT":
        inimesed, palgad = sort_by_salary()
        show_values(inimesed,palgad)
    else:
        break #end programm










