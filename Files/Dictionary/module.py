from types import new_class


def load_dictionary() -> dict:
    """
    Loads data from files rus and eng to python dictionary
    Returns Dictionary
    """
    import os.path
    alg_path = os.path.dirname(__file__) + '/'
    t_dict = {}
    rus_list = []
    eng_list = []
    # try open a files and store data to lists
    try:
        rus = open(alg_path + 'rus.txt', 'r',encoding='utf-8')
        eng = open(alg_path + 'eng.txt', 'r',encoding='utf-8')
                  
    except FileNotFoundError:
        rus = open(alg_path + 'rus.txt','w',encoding='utf-8')
        eng = open(alg_path + 'eng.txt','w',encoding='utf-8')
    
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
    import os.path
   
    rus_file = open( os.path.dirname(__file__) + '/rus.txt','w',encoding='utf-8')
    eng_file = open( os.path.dirname(__file__) + '/eng.txt','w',encoding='utf-8')
    
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
            text_to_speech(eng,"en")
            return
        elif i_word == eng:
            print(rus.capitalize())
            text_to_speech(rus,"ru")
            return

    print("Такого слова еще нет в словаре")
    if input("Добавить? Enter - да Q - нет").upper() != "Q":
        add_translation(my_dictionary,i_word)
    

def add_translation(my_dictionary : dict,new_word:str = "",new_t_word:str = "") -> dict:

    """
    Adds translation to library then appends it in file
    """
    
    rus_symbols = "абвгдежзиклмнопрстуфхцчшщъыьэюя"
    while True:
        if new_word == "":
            new_word = input("Введите новое слово для добавления: ").lower()
        # language detect 
        lang = "ENG"
        for i in new_word:
            if rus_symbols.find(i) > 0:
                lang = "RUS"
                break
        
        print(lang)

        while True:
            if new_t_word == "":
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
        
        new_word = ""
        new_t_word = ""
        if input("Enter - ввести еще. \"Q\" чтобы выйти: ").upper() == "Q":
                break

    save_dictionary(my_dictionary)



def correct_data(my_dictionary : dict):
    """
    Corrects translation of a given word
    """

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


def training(my_dictionary:dict):
    """
    Show random words and verify translate
    Prints result of right words in  %
    """
    # Print info
    print("Слова будут отображаться в случайном порядке.\nВаша задача написать перевод слова.\nРезульат будет выведен после ввода \"Q\"")
    # Lang
    while True:
        lang = input("Выбери язык:\n1.RUS -> ENG\n2.ENG -> RUS\n").upper()
        if lang == "1":
            lang = "RUS -> ENG"
            break
        elif lang == "2":
            lang = "ENG -> RUS"
            break
        elif lang == "Q":
            print("Отмена операции")
            return
        else:
            print("Введи 1 или 2!")
    print(lang)

    # Start
    if input("Нажмите Ввод для старта или Q для выхода").upper() == "Q":
        return
    
    # Start count
    import os # чтобы чистить консоль
    import time
    for i in range(3,0,-1):
        os.system('cls' if os.name == 'nt' else 'clear') # clear console
        print(f"Старт через {i}")
        # 1 sec delay
        time.sleep(1)

    #Create lists from dictionary
    eng_list = []
    rus_list = []
    for rus,eng in my_dictionary.items():
        eng_list.append(eng)
        rus_list.append(rus)
    
    # find max index of list 
    max_index = len(rus_list) - 1

    # show random word by selected language
    import random
    from colorama import Fore,Back,Style
    
    total_counter = 0
    ok_counter = 0
    while True:
        rand_index = random.randint(0,max_index)
        if lang == "RUS -> ENG":
            print(rus_list[rand_index])
            answer = input("\n").lower()
            if answer == eng_list[rand_index].lower():
                print(Fore.GREEN + "Верно!")
                print(Style.RESET_ALL)
                ok_counter += 1
            elif answer == "q":
                break # Quit
            else:
                print(Fore.RED + "Неправильно! ( " + eng_list[rand_index]+ ' )')
                print(Style.RESET_ALL)

        elif lang == "ENG -> RUS":
            print(eng_list[rand_index])
            answer = input("\n").lower()
            if answer == rus_list[rand_index].lower():
                print(Fore.GREEN + "Верно!")
                print(Style.RESET_ALL)
                ok_counter += 1
            elif answer == "q":
                break # Quit
            else:
                print(Fore.RED + "Неправильно! ( " + rus_list[rand_index]+ ' )')
                print(Style.RESET_ALL)
        
        total_counter +=1

    # print results
    print("Всего слов:", total_counter)
    print("Правильных ответов:",ok_counter, end=" ")
    round_per = round(ok_counter / (total_counter/100),2)
    print(f"( {round_per}% )")
        
# to use text to speech you need pip install gTTS
def text_to_speech(thisText:str,thisLanguage:str):
    """
    This function generates text to speech
    """
    print("Проигрывание...")
    import os.path
    mp3_path = os.path.dirname(__file__) + '/' #where mp3 file will be saved
    mp3_file = 'text_to_speech.mp3'

    from gtts import gTTS
    tts = gTTS(text = thisText, slow=False,lang = thisLanguage)
    tts.save(mp3_path + mp3_file)

    import os
    os.system("start " + mp3_path + mp3_file)

def delete_transl(my_dictionary:dict):
    """
    Delete pair value from dictionary
    """
    rus_word = ""
    eng_word = ""
    w_to_delete = input("Введите слово, которое следует удалить\n")
    for rus,eng in my_dictionary.items():
        if rus == w_to_delete or eng == w_to_delete:
            rus_word = rus
            eng_word = eng

            # delete value from dictionary
            my_dictionary.pop(rus_word)

            # save dictionary
            save_dictionary(my_dictionary)

            return
            
    print("Такого слова нет в словаре")
    



    