import os

if not os.path.isfile("task.txt"):

    while True:
        user_choise = input(
            "Файл не найден, вы хотите создать новыый ? (введите y-да, n-нет):  "
        )
        if user_choise.lower() == "y":
            with open("task.txt", "w", encoding="utf-8") as f:
                f.write("имя | задача | приоритет\n")
                print("Файл task.txt создан и записан")
                break
        elif user_choise.lower() == "n":
            print("Выход из программы.")
            exit()
        else:
            print("Вы ввели не правильную команду")
print(
    """📌 Главное меню: 
    Пункт 1 — Показать все задачи
    Пункт 2 — Добавить задачу
    Пункт 3 — Показать задачи по имени
    Пункт 4 — Удалить задачу по номеру
    Пункт 5 — Выход"""
)


# Чтение и нумерация строк
def show_all_tasks():
    with open("task.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # собираем файл в один текст
        print(f"[0] {lines[0].strip()}")
        # выводим шапку так что бы ее нельзя было удалить
        for idx, line in enumerate(lines[1:], start=1):
            print(f"[{idx}] {line.strip()}")


# Добавляем задачу
def add_task():
    with open("task.txt", "a", encoding="utf-8") as f:
        try:
            str_task = []
            user_name = input("Введите имя:  ")
            if "|" not in user_name:
                str_task.append(user_name.strip())
            else:
                raise ValueError
            user_task = input("Введите задачу: ")
            if "|" not in user_task:
                str_task.append(user_task.strip())
            else:
                raise ValueError
            user_priority = input("Введите приоритетность от 1 до 5: ")
            # проверяем что бы приоритет был цифрой в диапазоне от 1 до 5 без "|"
            if "|" in user_priority:
                raise ValueError("Запрещённый символ")
            if not user_priority.isdigit():
                raise ValueError("Приоритет должен быть числом")
            if not 1 <= int(user_priority) <= 5:
                raise ValueError("Приоритет должен быть от 1 до 5")

            str_task.append(user_priority.strip())

            line_task = "| ".join(str_task)
            # добавление новой строки в конец файла.
            f.write(f"{line_task}\n")
            print(f"{line_task}добавлено в файл")
        except ValueError as ve:
            print("Нельзя импользовать символ '|'", ve)


# Поиск по имени
def find_task_on_name():
    with open("task.txt", "r", encoding="utf-8") as f:
        lines = f.readlines()
        # собираем в один список
        user_find = input("Введите имя для поиска: ")
        user_find = user_find.strip()
        for idx, line in enumerate(lines[1:], start=1):

            task_line = line.split("|")
            if user_find in task_line[0].strip().lower():
                print(f"Для {user_find}доступна следующая задача{task_line[1:]}")


while True:

    user_menu = input("Выберите пункт: ")

    if user_menu == "1":
        show_all_tasks()

    elif user_menu == "2":
        add_task()
    elif user_menu == "5":
        print("До свидания!!!")
        break
