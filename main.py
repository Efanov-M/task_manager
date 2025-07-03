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
user_menu = input("Выберите пункт: ")
