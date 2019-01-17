#easy
# Все задачи текущего блока решите с помощью генераторов списков!

# Задание-1:
# Дан список, заполненный произвольными целыми числами. 
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]
#==============================================
#Вариант 1
print("="*30)
print("Задание-1 Вариант 1")
my_list = [1, 2, 4, 0]
print('Исходный список: ', my_list)
i = 0
for n in my_list:
    my_list[i] = n ** 2
    i += 1
print('Измененный список: ', my_list)
print("="*30)
print()
#Вариант 2
print("="*30)
print("Задание-1 Вариант 2")
my_list = [1, 2, 4, 0]
print('Исходный список: ', my_list)
my_list = [int(my_list[i]) ** 2 for i in range(len(my_list))]
print('Измененный список: ', my_list)
print("="*30)
print()
#Вариант 3
print("="*30)
print("Задание-1 Вариант 3")
def modify(lst):
    lst_new = []
    for n in lst:
        lst_new.append(n ** 2)
    return lst_new
my_list = [1, 2, 4, 0]
print('Исходный список: ', my_list)
my_list = modify(my_list)
print('Измененный список: ', my_list)
print("="*30)
print()

# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.
print("="*30)
print("Задание-2")
import re
lst1 = ['carot', 'apple', 'orange', 'grapes', 'mango' ]
lst2 = ['mango', 'banana', 'apple', 'peach']
lst_new = []
print('Первый список фруктов: ', lst1)
print('Второй список фруктов: ', lst2)
string = str(lst2)
'''
Вот так добавляю генератор списка, но не могу понять, как правильно задать условие,
что если после проверки списка не False, то берем этот элемент
lst_new = [(re.search(n, string) is None) for n in lst1 if ???]
'''
for n in lst1:
    if (re.search(n, string) is None) == False:
        lst_new.append(n)
print('Совпадающие фрукты: ', lst_new)
print()

# Задание-3:
# Дан список, заполненный произвольными числами.
# Получить список из элементов исходного, удовлетворяющих следующим условиям:
# + Элемент кратен 3
# + Элемент положительный
# + Элемент не кратен 4
print("="*30)
print("Задание-3")
import random
my_list = [random.randint(-20,50) for _ in range(20)]
print("Случайная последовательность: ", my_list)			
my_list_new = []
for n in my_list:
    if n > 0 and n % 3 == 0 and n % 4 != 0:
        my_list_new.append(n)
print("Список положительных элементов, кратных 3 и не кратных 4: ", my_list_new)

#Normal
# Задание-1:
# Вывести символы в нижнем регистре, которые находятся вокруг
# 1 или более символов в верхнем регистре.
# Т.е. из строки "mtMmEZUOmcq" нужно получить ['mt', 'm', 'mcq']
# Решить задачу двумя способами: с помощью re и без.
print("="*30)
print("Задание-1")
import re
line = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysmNO'\
       'GIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewVzK'\
       'TUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSAHqn'\
       'LxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIVjXa'\
       'pzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnWete'\
       'kUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfCvzQ'\
       'WrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbRuXb'\
       'JrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkmjCC'\
       'EUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOnLfB'\
       'tQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGSeuT'\
       'SkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCfKCu'\
       'UJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWHuXB'\
       'qHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQNJFa'\
       'XiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQoiQ'\
       'zTYwZAiRwycdlHfyHNGmkNqSwXUrxGc'
print("Исходная строка: ", line)
pattern ='[a-z]+'
print()
print("Символы в строке в нижнем регистре:\n", re.findall(pattern, line))
print()
print("Решение без re")
find = 'abcdefghijklmnopqrstuvwxyz'
lst = []

print("="*30)
# Задание-2:
# Вывести символы в верхнем регистре, слева от которых находятся
# два символа в нижнем регистре, а справа - два символа в верхнем регистре.
# Т.е. из строки 
# "GAMkgAYEOmHBSQsSUHKvSfbmxULaysmNOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLec"
# нужно получить список строк: ['AY', 'NOGI', 'P']
# Решить задачу двумя способами: с помощью re и без.
print("Задание-2")
line_2 = 'mtMmEZUOmcqWiryMQhhTxqKdSTKCYEJlEZCsGAMkgAYEOmHBSQsSUHKvSfbmxULaysm'\
       'NOGIPHpEMujalpPLNzRWXfwHQqwksrFeipEUlTLeclMwAoktKlfUBJHPsnawvjPhfgewV'\
       'fzKTUfSYtBydXaVIpxWjNKgXANvIoumesCSSvjEGRJosUfuhRRDUuTQwLlJJJDdkVjfSA'\
       'HqnLxooisBDWuxIhyjJaXDYwdoVPnsllMngNlmkpYOlqXEFIxPqqqgAWdJsOvqppOfyIV'\
       'jXapzGOrfinzzsNMtBIOclwbfRzytmDgEFUzxvZGkdOaQYLVBfsGSAfJMchgBWAsGnBnW'\
       'etekUTVuPluKRMQsdelzBgLzuwiimqkFKpyQRzOUyHkXRkdyIEBvTjdByCfkVIAQaAbfC'\
       'vzQWrMMsYpLtdqRltXPqcSMXJIvlBzKoQnSwPFkapxGqnZCVFfKRLUIGBLOwhchWCdJbR'\
       'uXbJrwTRNyAxDctszKjSnndaFkcBZmJZWjUeYMdevHhBJMBSShDqbjAuDGTTrSXZywYkm'\
       'jCCEUZShGofaFpuespaZWLFNIsOqsIRLexWqTXsOaScgnsUKsJxiihwsCdBViEQBHQaOn'\
       'LfBtQQShTYHFqrvpVFiiEFMcIFTrTkIBpGUflwTvAzMUtmSQQZGHlmQKJndiAXbIzVkGS'\
       'euTSkyjIGsiWLALHUCsnQtiOtrbQOQunurZgHFiZjWtZCEXZCnZjLeMiFlxnPkqfJFbCf'\
       'KCuUJmGYJZPpRBFNLkqigxFkrRAppYRXeSCBxbGvqHmlsSZMWSVQyzenWoGxyGPvbnhWH'\
       'uXBqHFjvihuNGEEFsfnMXTfptvIOlhKhyYwxLnqOsBdGvnuyEZIheApQGOXWeXoLWiDQN'\
       'JFaXiUWgsKQrDOeZoNlZNRvHnLgCmysUeKnVJXPFIzvdDyleXylnKBfLCjLHntltignbQ'\
       'oiQzTYwZAiRwycdlHfyHNGmkNqSwXUrxGC'
print("Исходная строка: ", line_2)
pattern ='[a-z][a-z]([A-Z]+)[A-Z][A-Z]'
print()
print("Символы в строке:\n", re.findall(pattern, line_2))
print("="*30)
print()

# Задание-3:
print("="*30)
print("Задание-3")
import os
import re
import random
path = os.path.join('Base.txt.')
with open(path, 'w', encoding='UTF-8') as f:
    for i in range(2500):
        f.write(str(random.randint(0, 9)))
print("Произведена запись последовательности в файл!")
with open(path, 'r', encoding='UTF-8') as f:
    str_num = f.read()
print("Числовая последовательность из фалйа:\n", str_num)
pattern = re.compile('1{2,}|2{2,}|3{2,}|4{2,}|5{2,}|6{2,}|7{2,}|8{2,}|9{2,}|0{2,}^\D)'
lst_num = pattern.findall(str_num)
lst_num_len = 1
for i in lst_num:
    if len(i) > lst_num_len
	max_num_len = lst_num(i)
print("Максимальная последовательность одинакоывых чисел: ", max_num_len)
print("="*30)