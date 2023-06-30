from datetime import datetime
import csv
import os
import shutil

# создание класса "Заметки"
class Note_pad:

    def __init__(self):
# счетчик для определения номера строки 
        self.number_line = None 

# создание функции новой заметки
    def add_note(self):
# проверка на то, существует ли файл .csv если нет, создаст файл с заголовками столбцов
        if os.path.isfile("arhive_note/file.csv") == False: 
            headerlist = ({"name_note": [], "date_time_last_save": [], "text_note": []})
            with open("arhive_note/file.csv", "w", newline="", encoding="utf-8") as file_note:
                d_writer = csv.DictWriter(file_note, delimiter=";",fieldnames=headerlist)
                d_writer.writeheader()
# создание новой заметки
        print('Введите имя новой заметки:')
        new_name_note = input()
        date_current = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
        print('Введите текст заметки:')
        text_note = input()

        with open("arhive_note/file.csv", "a", newline="", encoding="utf-8") as note:
            writer = csv.writer(note, delimiter=";")
            writer.writerow([new_name_note, date_current, text_note])
            print("Заметка успешно создана!")

# создание функции выводящей в консоль список всех заметок
    def list_note(self):
        print('Список заметок:')
        with open("arhive_note/file.csv", encoding="utf-8") as note_list:
            reader = csv.DictReader(note_list, delimiter=";")
            for row in reader:
                print(row["name_note"])

# создание функции "выбор действия над выбранной заметкой" (чтение,редактирование, удаление)
    def select_note(self):
        print("Введите имя заметки:")
        name = input()

        with open("arhive_note/file.csv", encoding="utf-8") as line:
            reader = csv.DictReader(line, delimiter=";")
            for i, row in enumerate(reader):
# нахождение номера строки по названию заметки и присвоить значение для self.number_line
                if row["name_note"] == name:
                    self.number_line = i
                    print("Выберете действие с заметкой:\n1) Посмотреть заметку\n2) Изменить заметку\n3) Удалить заметку")
                    count = input()
# действие если пользователь выберет "чтение заметки" 
                    if count == "1":
                        with open("arhive_note/file.csv", encoding="utf-8") as csv_file:
                            csv_reader = csv.reader(csv_file)
                            rows = list(csv_reader)
                            print(rows[self.number_line + 1])
# действие если пользователь выберет "Редактирование заметки"
                    if count == "2":
                        with open("arhive_note/file.csv", encoding="utf-8", newline='') as source, open("arhive_note/new_file.csv", "w", encoding="utf-8", newline='') as dest:
                            reader = csv.reader(source, delimiter=';')
                            writer = csv.writer(dest,delimiter=';')
                            for line,rows in enumerate(reader):
                                if line != self.number_line + 1:
                                    writer.writerow(rows)
                                if line == self.number_line + 1:
                                    date_current = str(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                                    print("Введите новый текст:")
                                    new_text = input()
                                    writer.writerow([row["name_note"], date_current, new_text])
                        shutil.copy2(r"arhive_note/new_file.csv", r"arhive_note/file.csv")
                        os.remove('arhive_note/new_file.csv')
# действие если пользователь выберет "Удаление заметки"
                    if count == "3":
                        with open("arhive_note/file.csv", newline='') as source, open("arhive_note/new_file.csv", "w", newline='') as dest:
                            reader = csv.reader(source, delimiter=';')
                            writer = csv.writer(dest,delimiter=';')
                            for line,row in enumerate(reader):
                                if line != self.number_line + 1:
                                    writer.writerow(row)
                        shutil.copy2(r"arhive_note/new_file.csv", r"arhive_note/file.csv")
                        os.remove('arhive_note/new_file.csv')
                        print("Заметка успешно удалена!!!")
# действие если нет пользователь ввёл не существующую заметку
            if self.number_line == None:
                    print("такой заметки нет!!!")