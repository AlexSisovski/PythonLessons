#Easy
# Задание-1:
# Напишите функцию, округляющую полученное произвольное десятичное число
# до кол-ва знаков (кол-во знаков передается вторым аргументом).
# Округление должно происходить по математическим правилам (0.6 --> 1, 0.4 --> 0).
# Для решения задачи не используйте встроенные функции и функции из модуля math.
print("Задание 1")
def my_round(number, ndigits):
    num = number * (10 ** (ndigits + 1))
    if num % 10 >= 5:
        num += 10
    num = int(num / 10) / (10 ** ndigits)
    return num

print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))
print("="*70)

# Задание-2:
# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.
# !!!P.S.: функция не должна НИЧЕГО print'ить
print("Задание 2")
def lucky_ticket(ticket_number):
    begin = []
    end = []
    n = []
    for i in str(ticket_number):
        n.append(int(i))
    if len(n) != 6:
        return False    
    begin = sum(n[:3])
    end = sum(n[3:])
    if begin == end:
        return True
    else:
        return False              
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
print("="*70)


#Normal
# Задание-1:
# Напишите функцию, возвращающую ряд Фибоначчи с n-элемента до m-элемента.
# Первыми элементами ряда считать цифры 1 1
print("Задание 1")
def fibonacci(n, m):
    arr = [1, 1]
    i = 0
    while len(arr) < m:
        arr.append(arr[i] + arr[i+1])
        i += 1
    return arr[(n-1):m]
mylist = fibonacci(5, 25)
print(mylist)
print("="*70)

# Задача-2:
# Напишите функцию, сортирующую принимаемый список по возрастанию.
# Для сортировки используйте любой алгоритм (например пузырьковый).
# Для решения данной задачи нельзя использовать встроенную функцию и метод sort()
print("Задание 2")
def sort_to_max(origin_list):
    n = 1
    while n < len(origin_list):
        for i in range(len(origin_list)-n):
            if origin_list[i] > origin_list[i+1]:
                origin_list[i],origin_list[i+1] = origin_list[i+1],origin_list[i]
        n += 1
    return origin_list
mylist = sort_to_max([2, 10, -12, 2.5, 20, -11, 4, 4, 0])
print(mylist)
print("="*70)

# Задача-3:
# Напишите собственную реализацию стандартной функции filter.
# Разумеется, внутри нельзя использовать саму функцию filter.


# Задача-4:
# Даны четыре точки А1(х1, у1), А2(x2 ,у2), А3(x3 , у3), А4(х4, у4).
# Определить, будут ли они вершинами параллелограмма.


