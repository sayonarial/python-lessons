options_list = ["Конкатенация", "Отредактировать как заголовок", "Переворот регистров","Конверировать в ASCII","Добавить нулей, да побольше", "Удалить все гласные (en/rus)","Удалить все согласные (en/rus)", "Накричать текстом","Перемешать слова", "Развернуть текст" ]
vowel_list = ['A', 'E', 'I', 'O', 'U', 'А', 'У', 'О', 'Ы', 'И', 'Э', 'Я', 'Ю', 'Ё', 'Е']
consonants_list = ['Б', 'В', 'Г', 'Д', 'Ж', 'З', 'Й', 'К', 'Л', 'М', 'Н','П', 'Р', 'С', 'Т', 'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ',  'B', 'C', 'D', 'F', 'G', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'S', 'T', 'V', 'X', 'Z','H', 'R', 'W', 'Y']
       

def show_avail_options():
    print()
    print("Доступные опции:")
    f_counter = 1
    for i in options_list:
        print(f"{f_counter}. - {i}")
        f_counter += 1 
    print()

def redact_string(action):
    print(options_list[action - 1] + ":")
    f_str = input("Введите строку: ")

    if action == 1: #Конкатенация
        return f_str + input("Введите еще одну строку: ")

    elif action == 2: # Отредактировать как заголовок
        
        return f_str.capitalize()

    elif action == 3: # Переворот регистров
        return f_str.swapcase()

    elif action == 4: # Конверировать в ASCII
        for i in range(len(f_str)):
            print(ord(f_str[i]),end = " ")
        return ""
    
    elif action == 5: # Добавить нулей, да побольше
        print(f"Размер вашей строки: {len(f_str)}")
        while True:
            new_length = input("Введите предпочитаемый размер строки: ")
            if new_length.isdigit() == True:
                try:
                    new_length = int(new_length)
                    break
                except:
                    ValueError
        return f_str.zfill(new_length)
    
    elif action == 6: # Удалить все гласные (en/rus)
        new_string = ""
        for i in range(len(f_str)):
            if f_str[i].upper() not in vowel_list:
                new_string += f_str[i]
        return new_string

    elif action == 7: # Удалить все согласные (en/rus)
        new_string = ""
        for i in range(len(f_str)):
            if f_str[i].upper() not in consonants_list:
                new_string += f_str[i]
        return new_string

    elif action == 8: # Накричать текстом
        return f_str.upper()

    elif action == 9: # Перемешать слова
        new_string = ""
        from random import shuffle
        new_words_list = f_str.split(" ")
        shuffle(new_words_list)
        for i in new_words_list:
            new_string += i + " "
        return new_string

    elif action == 10: # Развернуть текст
        new_string = ""
        string_lenght = len(f_str)
        for i in range(string_lenght):
            new_string += f_str[string_lenght - i - 1]
        return new_string
        

def main():
    
    show_avail_options()
    # wait for user to input a number of option
    option_num = input("Введите номер опции: ")
    if option_num.isdigit() == True:
        option_num = int(option_num)
        if option_num in range(1,len(options_list)+1):
            print()
            print(redact_string(option_num))
        else:
            print("Такой опции не существует")
            return
    else:
        print("Пожалуйста, вводите только цифры")
        return
    
    print()
        


if __name__ == "__main__":
    while True:
        main()
        input("Нажмине Enter чтобы начать заново...")