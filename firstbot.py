import sqlite3
import os
import time
from colorama import init
from colorama import Fore, Back, Style
init()
print(Fore.WHITE)
print(Back.BLACK)

youtube = ["https://youtu.be/bWNmJqgri4Q", "https://youtu.be/iPV5GKeHyV4", "https://youtu.be/fp5-XQFr_nk", "https://youtu.be/CxgOKJh4zWE"]
rick_roll = "https://youtu.be/xm3YgoEiEDc"
conn = sqlite3.connect('users.db')
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

def register():
    global username
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result:
        print("Это имя пользователя уже зарегистрировано.")
    else:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        print("Регистрация прошла успешно.")

def login():
    global username
    username = input("Введите имя пользователя: ")
    password = input("Введите пароль: ")

    c.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    result = c.fetchone()
    if result:
        print("Вход выполнен успешно.")
    else:
        print("Неверное имя пользователя или пароль.")
        exit()

def main():
    action = input("Введите 'r', чтобы зарегистрироваться, или 'l', чтобы войти в аккаунт: ")
    if action == 'r':
        register()
    elif action == 'l':
        login()
    else:
        print("Неверная команда.")
    time.sleep(2)
    print('''Добро пожаловать в школу IT ''', username)
    time.sleep(1)
    print('''Выбери язык программирования:
1) HTML
2) CSS
3) PYTHON
4) JavaScript''')
    it = int(input("Введи цифру:"))
    if it == 1:
        os.system(f"start {youtube[0]}")
    elif it == 2:
        os.system(f"start {youtube[1]}")
    elif it == 3:
        os.system(f"start {youtube[2]}")
    elif it == 4:
        os.system(f"start {youtube[3]}")
    else:
        os.system(f"start {rick_roll}")
        print("Ошибка!")
    print("Приятного просмотра!")


if __name__ == '__main__':
    main()


input()
