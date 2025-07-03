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


while True:

    user_menu = input("Выберите пункт: ")

    if user_menu == "1":
        show_all_tasks()
    elif user_menu == "5":
        print("До свидания!!!")
        break
