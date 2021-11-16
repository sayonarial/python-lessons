def load_dictionary() -> dict:
    """
    Loads data from files rus and eng to python dictionary
    Returns Dictionary
    """
    t_dict = {}
    rus_list = []
    eng_list = []
    # try open a files and store data to lists
    try:
        rus = open('Files/Dictionary/rus.txt', 'r',encoding='utf-8')
        eng = open('Files/Dictionary/eng.txt', 'r',encoding='utf-8')
                  
    except FileNotFoundError:
        rus = open('Files/Dictionary/rus.txt','w',encoding='utf-8')
        eng = open('Files/Dictionary/eng.txt','w',encoding='utf-8')
    
    rus_list = rus.readlines()
    eng_list = eng.readlines()  
    rus.close()
    eng.close()

    # record to dictionary clear "\n"s
    for c in range(len(rus_list)):
        t_dict.update({rus_list[c].strip():eng_list[c].strip()})

    return t_dict

def save_dictionary(my_dictionary : dict):
    """
    Saves a dictionary to separate files eng.txt and rus.txt
    """
    
    rus_file = open('Files/Dictionary/rus.txt','w',encoding='utf-8')
    eng_file = open('Files/Dictionary/eng.txt','w',encoding='utf-8')
    
    for rus,eng in my_dictionary.items():
        rus_file.write(rus + '\n')
        eng_file.write(eng + '\n')

    rus_file.close()
    eng_file.close()

    print("Данные обновлены")


def show_values(dict_to_show:dict):
    """
    Shows all dictionary values
    """
    print("RUS | ENG")
    for rus,eng in dict_to_show.items():
        print(str(rus).capitalize() + " - " + str(eng).capitalize())
    


def translate(my_dictionary : dict):
    """
    Translates a word from a dictionary
    """
    # input a word to translate
    i_word = input ("Введите слово для перевода: ").lower()

    # find this word in a dictionary and print translated value
    for rus,eng in my_dictionary.items():
        if i_word == rus:
            print(eng.capitalize())
            return
        elif i_word == eng:
            print(rus.capitalize())
            return

    print("Такого слова еще нет в словаре")

def add_translation(my_dictionary : dict) -> dict:

    """
    Adds translation to library then appends it in file
    """
    show_values(my_dictionary)
    rus_symbols = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
    while True:
        new_word = input("Введите новое слово для добавления: ").lower()
        # language detect 
        lang = "ENG"
        for i in new_word:
            if rus_symbols.find(i) > 0:
                lang = "RUS"
                break
        
        print(lang)

        while True:
            new_t_word = input(f"Введите  перевод для слова {new_word.capitalize()}: ").lower()
            # check one more time for opposite language
            t_lang = "ENG"
            for i in new_t_word:
                if rus_symbols.find(i) > 0:
                    t_lang = "RUS"
                    break
            if lang == t_lang:
                print("Язык должен отличаться!")
            else:
                break
        
        if lang == "RUS":
            my_dictionary.update({new_word:new_t_word})
        else:
            my_dictionary.update({new_t_word:new_word})
        
        if input("Enter - ввести еще. \"Q\" чтобы выйти: ").upper() == "Q":
                break

    save_dictionary(my_dictionary)



def correct_data(my_dictionary : dict):
    """
    Corrects translation of a given word
    """
    show_values(my_dictionary)

    # input value to change
    while True:
        c_text = input('Введите слово чтобы изменить его перевод: ').lower()
        rus_word = ""
        eng_word = ""
        for rus,eng in my_dictionary.items():
            if rus == c_text:
                rus_word = c_text
                eng_word = input("Введите новый перевод для " + rus_word.capitalize()+ ': ').lower()
                w_to_delete = rus_word
                break
                
            elif eng == c_text:
                eng_word = c_text
                rus_word = input("Введите новый перевод для " + eng_word.capitalize() + ': ').lower()
                w_to_delete = rus
                break
        if eng_word == "" or rus_word == "":
            print("Такого слова нет в словаре")
            if input("Enter - заново. \"Q\" чтобы выйти: ").upper() == "Q":
                break
        else:
            break

    # double check for language
    rus_symbols = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
    rus_s_counter = 0
    for i in rus_word:
        rus_s_counter += rus_symbols.find(i)
    if rus_s_counter == 0:
        print("В русском слове нет русских букв!")
        return
    for i in eng_word:
        if rus_symbols.find(i) > 0:
            print("Английское слово содержит российские буквы!")
            return

    # delete value from dictionary
    my_dictionary.pop(w_to_delete)

    # update dictionary with new value
    my_dictionary.update({rus_word:eng_word})

    # save dictionary
    save_dictionary(my_dictionary)



