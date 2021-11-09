
def show_values(usernames: list,passwords: list):
    """
    Отображает все записанные имена пользователей и их пароли
    """
    for i in range(len(usernames)):
        print(f"{usernames[i]} : {passwords[i]}")
        
def generate_password() -> str:
    """
    Генерирует и возвращает пароль используя рандомную выборку
    """
    import random
    str0=".,:;!_*-+()/#¤%&"
    str1 = '0123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    print(str3) # 'QWERTYUIOPASDFGHJKLZXCVBNM'
    str4 = str0+str1+str2+str3
    print(str4)
    ls = list(str4)
    print(ls)
    random.shuffle(ls)
    print(ls)
    # Извлекаем из списка 12 произвольных значений
    psword = ''.join([random.choice(ls) for x in range(12)])
    # Пароль готов
    print(psword)
    return psword
    
def show_menu() -> str:
    """
    Отображает главное меню и возвращает название выбранной функции
    """
    menu_list = ["Авторизироваться", "Зарегестрироваться","Закончить работу"]
    m_counter = 1

    for i in menu_list:
        print(f"{m_counter}.{i}")
        m_counter += 1

    while True:
        choise = input_int("Выберите действие: ")
        if choise not in range(len(menu_list)) or choise == 3:
            return "Закончить работу"
        else:
            return menu_list[choise-1]
  
def input_int(message: str) -> int:
    """
    Проверяет введенное значение и возвращает int если значение введено верно
    Отображает сообщение данное в первом агрументе функции
    """
    while True:
        dig = input(message)
        try:
            dig = int(dig)
            return dig
        except:
            print("Not a digit! Press \'Q\' to exit")
def autorization(usernames: list,passwords: list) -> bool:
    """
    Авторизация пользователя, возвращает True если пользователь есть и пароль верен
    """
    while True:
        # Спросить логин
        username_input = input("Введите имя пользователя: ")
        # найти пользователя
        if usernames.count(username_input) < 1:
            print("Такого пользовтеля не существует")
            if input_int("1.Попробовать еще раз\n2.Выйти в главное меню\n") == 2:
                return False
        else:
            username_index = usernames.index(username_input) 
            break
    
    while True:
        # Спросить пароль
        pass_input = input(f"Введите пароль для {usernames[username_index]}: ")
        # сверить Пароль  с паролем из базы
        if pass_input == password_list[username_index]:
            print("Пароль правильный. Вход выполнен успешно")
            return True
        else:
            print("Неправильный пароль!")
            if input_int("1.Попробовать еще раз\n2.Выйти в главное меню\n") == 2:
                return False
def check_new_password(password:str) -> bool:
    """
    Проверяет пароль на наличие цифры, маленькой буквы, заглавной буквы, спец символа
    Возвращает true или false
    """
    # Пробегаемся по каждому символу один раз проверяя условия
    special_chars=".,:;!_*-+()/#¤%&"
    digits = 0
    s_letter = 0
    l_letter = 0
    s_char = 0

    for i in password:
        if i.isdigit():
            digits += 1
        elif i.islower():
            s_letter +=1
        elif i.isupper():
            l_letter += 1
        else:
            for c in special_chars:
                if i == c:
                    s_char += 1
    
    conf = True
    if digits < 1:
        print("Пароль должен содержать хотя бы одну цифру!")
        conf = False
    if s_letter < 1:
        print("Пароль должен содержать хотя бы одну маленькую букву!")
        conf = False
    if l_letter < 1:
        print("Пароль должен содержать хотя бы одну заглавную букву!")
        conf = False
    if s_char < 1:
        print("Пароль должен содержать хотя бы один специальный символ! (.,:;!_*-+()/#¤%&)")
        conf = False

    return conf # Если все хорошо возврат true

def registration(usernames: list,passwords: list) -> list:
    """
    Регистрация пользователя, функция возвращает пустой лист если ввод данных был прекращен
    или лист с новым логином и паролем
    """
    new_username = ""
    new_password = ""
    while True:
        # Ввести имя нового пользователя
        new_username = input("Введите новое имя пользовтеля: ")
        # Проверка на наличие такого пользовтеля в базе
        if usernames.count(new_username) > 0:
            print("Такой пользователь уже существует")
            if input_int("1.Попробовать еще раз\n2.Выйти в главное меню\n") == 2:
                return ["",""]
        else:
            print(f"Привет, {new_username}!")
            break
    # Предложить сгенерировать пароль, ввести самостоятельно или отменить
    x = input_int("1.Сгенерировать пароль автоматически\n2.Ввести пароль вручную\n3.Выйти в главное меню\n")
    if x == 3: # quit
        return ["",""]
    elif x == 1: # auto pass
        new_password = generate_password()
    elif x == 2: # manual pass
        while True:
            print("Придумай пароль, содержащий как минимум по одному из перечистленных:\nцифра\nмаленькая буква\nзаглавная буква\nспец. символ(.,:;!_*-+()/#¤%&)")
            new_password = input()
            if check_new_password(new_password) == False:
                if input_int("1.Попробовать еще раз\n2.Выйти в главное меню\n") == 2:
                    return ["",""]
            else:
                break

    return [new_username,new_password]

username_list = ["admin"]
password_list = ["admin1"]

while True: # Основной цикл обработки

    # отобразить меню и ждать ответа
    menu = show_menu() 
    # функция в зависимости от выбора пункта меню
    if menu == "Авторизироваться":
        logged_in = autorization(username_list,password_list)
        if logged_in:
            show_values(username_list,password_list)
    elif menu == "Зарегестрироваться":
        new_user = registration(username_list,password_list)
        new_user_name = new_user[0]
        new_user_pass = new_user[1]
        if new_user_name != "":  # Добавить пользователя  если данные верны
            username_list.append(new_user_name)
            password_list.append(new_user_pass)
            print(f"Пользователь {username_list[-1]} успешно добавлен.")
        else:
            print("Добавление пользовтаеля отменено")

    elif menu == "Закончить работу":
        break

