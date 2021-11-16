
from module import*

menu_list = ['Перевести слово'] # rus eng
menu_list.append('Добавить перевод')
menu_list.append('Исправить перевод')
menu_list.append('Показать данные')
menu_list.append('Выйти')

while True:
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
        add_translation(load_dictionary())
    elif menu_func == "Исправить перевод":
        correct_data(load_dictionary())
    elif menu_func == "Показать данные":
        show_values(load_dictionary())
    else:
        break

    input("Нажмите enter для продолжения")

