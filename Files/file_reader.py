

file_path = 'Files/file.txt'
while True:
    try:
        with open(file_path, 'r',encoding='UTF-8') as reader:
            print(reader.read())# читаем содержимое файла и выводим на экран
    except FileNotFoundError:
        f = open(file_path,'w',encoding='UTF-8')
        f.close()

    new_file = open(file_path,'a',encoding='UTF-8')
    text = input("Введите текст для сохранения: ")
    new_file.write('\n' + text)
    new_file.close()

    new_file = open(file_path,'w',encoding='UTF-8')
   
    for i in range(5):
        text = input(f"Введите строку {i+1} для повторения: ")
        new_file.write('\n' + text)

    new_file.close()