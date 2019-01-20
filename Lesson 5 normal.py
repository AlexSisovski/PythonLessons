
# Задача-1:
# Напишите небольшую консольную утилиту,
# позволяющую работать с папками текущей директории.
# Утилита должна иметь меню выбора действия, в котором будут пункты:
# 1. Перейти в папку
# 2. Просмотреть содержимое текущей папки
# 3. Удалить папку
# 4. Создать папку
# При выборе пунктов 1, 3, 4 программа запрашивает название папки
# и выводит результат действия: "Успешно создано/удалено/перешел",
# "Невозможно создать/удалить/перейти"

# Для решения данной задачи используйте алгоритмы из задания easy,
# оформленные в виде соответствующих функций,
# и импортированные в данный файл из easy.py

import os
import sys

print('sys.argv = ' , sys.argv)
def print_help():
    print("-"*65)
    print("1 - перейти в папку")
    print("2 - просмотреть содержимое текущей папки")
    print("3 - удалить папку")
    print("4 - создать папку")
    print("5 - информация об операционной системе")
    print("help - справка")
    print("-"*65)

def make_dir():
    dir_name = str(input("Введите имя директории: "))
    if not dir_name:
        print("Необходимо указать имя директории вторым параметром")
    else:
        dir_path = os.path.join(os.getcwd(), dir_name)
        print(dir_path)
        try:
            os.mkdir(dir_path)
            print('Директория {} создана'.format(dir_name))
        except FileExistsError:
            print('Директория {} уже существует'.format(dir_name))

def go_dir():
    print("-"*65)
    new_dir = input("Введите путь директории, в которую нужно перейти:")
    if os.path.isdir(new_dir) == True:
        os.chdir(new_dir)
        print("Переход в директорию {} произведен успешно!".format(new_dir))
    else:
        print("Директория {} не существует!".format(new_dir))
    print("-"*65)
    
def del_dir():
    print("-"*65)
    d_dir = input("Введите путь директории, которую нужно удалить:")
    if os.path.isdir(d_dir) == True:
        os.remove(d_dir)
        print("Директория {} удалена успешно!".format(d_dir))
    else:
        print("Директория {} не существует!".format(d_dir))
    print("-"*65)
    
def cur_dir():
    print("-"*65)
    lst = os.listdir('.')
    lst_dir = []
    for i in lst:
        if os.path.isdir(os.getcwd() + '\\' + i) == True:
            lst_dir.append(i)
    if len(lst_dir) == 0:
        print("В текуцщей директории {} других директорий не обнаружено!".format(os.getcwd()))
    else:
        print("Список обнаруженных директорий:")
        print("-"*45)
        for i in range(len(lst_dir)):
            print(lst_dir[i])
        print("-"*45)
    print("-"*65)
do = {
    "1":go_dir,
    "2":cur_dir,
    "3":del_dir,
    "4":make_dir,
    "help":print_help
    }

try:
    key = sys.argv[1]
except IndexError:
    key = None

if key:
    if do.get(key):
        do[key]()
    else:
        print("Задан неверный ключ")
        print("Укажите ключ help для получения справки")

