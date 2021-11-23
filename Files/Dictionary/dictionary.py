
from module import*
import os # чтобы чистить консоль

menu_list = ['Перевести слово'] # rus eng
menu_list.append('Добавить перевод')
menu_list.append('Удалить перевод')
menu_list.append('Исправить перевод')
menu_list.append('Отобразить словарь')
menu_list.append("Проверить знания")
menu_list.append('Выйти')

while True:
    os.system('cls' if os.name == 'nt' else 'clear') # clear console
    
    menu_counter = 1
    for i in menu_list:
        print(f"{menu_counter}. {i}")
        menu_counter +=1
    
    while True:
        try:
            menu_num = int(input("Выбeри операцию: "))
            break
        except ValueError:
            print("Вводи только цифры")

    print()
    menu_func = menu_list[menu_num-1]
    
    if menu_func == 'Перевести слово': 
        translate(load_dictionary())
    elif menu_func == "Добавить перевод":
        show_values(load_dictionary())
        add_translation(load_dictionary())
    elif menu_func == "Удалить перевод":
        show_values(load_dictionary())
        delete_transl(load_dictionary())
    elif menu_func == "Исправить перевод":
        show_values(load_dictionary())
        correct_data(load_dictionary())
    elif menu_func == "Отобразить словарь":
        show_values(load_dictionary())
    elif menu_func == "Проверить знания":
        training(load_dictionary())
    else:
        break
    
    print()
    input("Нажмите enter для продолжения")

