#Задача 1 Вариант 1
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.
import os
print("-"*30)
print ('os.getcwd() = ', os.getcwd())

def create_dir(dir_name):
    dir_path = os.path.join(os.getcwd(), dir_name)
    print(dir_path)
    try:
        os.mkdir(dir_path)
        print("Директория {} создана".format(dir_name))
    except FileExistsError:
        print("Директория {} уже существует".format(dir_name))
        
for i in range(9):
    dir_name = "dir_" + str(i)
    print(dir_name)
    do = create_dir(dir_name)
print("-"*30)

#Задача 1 Вариант 2
import os
print("-"*30)
dir_lst = [str("\dir_" + str(i)) for i in range(9)]
print("Список создаваемых директорий:\n", dir_lst)
for i in dir_lst:
    dir_path = os.path.join(os.getcwd() + i)
    if os.path.exists(dir_path) == False:
        os.mkdir(dir_path)
        print("Директория {} создана".format(dir_path))
    else:
        print("Директория {} уже существует".format(dir_path))
print("-"*30)
#Задача 2
# Напишите скрипт, отображающий папки текущей директории.
import os
print("-"*30)
lst = os.listdir('.')
lst_dir = []
for i in lst:
    if os.path.isdir(os.getcwd() + '\\' + i) == True:
        lst_dir.append(i)
if len(lst_dir) == 0:
    print("В текуцщей директории {} других директорий не обнаружено!".format(os.getcwd()))
else:
    print("Список обнаруженных директорий:")
    for i in range(len(lst_dir)):
        print(lst_dir[i])
print("-"*30)


###Задача 3
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.
import sys
import os
import shutil
print("-"*30)
full_name = sys.argv[0]
full_name_new = full_name + '.dupl'
print(full_name_new)
if os.path.isfile(full_name_new) == True:
    print("Файл {} уже существует!".format(full_name_new))
else:
    shutil.copy(full_name, full_name_new)
    print("Создан файл {}".format(full_name_new))
print("-"*30)
