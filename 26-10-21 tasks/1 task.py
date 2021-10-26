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
    if n == 0:
        print("Does not match")
        return
    for e in range(len(inimesed)):
        if e == d_nimi:
            t += 1
            index_list.append(int(e))
            print(f"{t}.{inimesed[e]} : {palgad}")
        while True:
            jar_no = input("Enter a number ")



while True:
    input_type = input("Enter R for random fill,\nM for manual salary input or S to show values\nS to show names and salary\nD to delete by name")
    if input_type in ["R", "M"]:
        fill_values()
    elif input_type == "S":
        show_values(inimesed,palgad)
    elif input_type == "D":
        delete_by_name()
    else:
        break #end programm










