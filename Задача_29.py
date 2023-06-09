# Ваня и Петя поспорили, кто быстрее решит следующую задачу: “Задана последовательность неотрицательных целых чисел. Требуется определить
# значение наибольшего элемента последовательности, которая завершается первым встретившимся нулем (число 0 не входит в последовательность)”. 
# Однако 2 друга оказались не такими смышлеными. Никто из ребят не смог до конца сделать это задание. Они решили так: у кого будет меньше ошибок в коде, 
# тот и выиграл спор. За помощью товарищи обратились к Вам, студентам.
# Примечание: Программные коды на следующих слайдах

# Ваня:
# n = int(input())
# max_number = 1000
# while n != 0:
#  n = int(input())
#  if max_number > n:
#  max_number = n
# print(max_number)

# Петя:
# n = int(input())
# max_number = -1
# while n < 0:
#  n = int(input())
#  if max_number < n:
#  n = max_number
# print(n)

# Собственное решение
num = int( input("Введите число: "))
max_num = num
while num != 0:
    num = int(input("Введите число: "))
    if num > max_num:
        max_num = num
print (f"Максимальное число в последовательности - {max_num}")

# Второй способ (недостаток - числа хранятся в памяти)
# list = []
# number = None
# while number != 0:
#     number = int(input("Введите число: "))
#     list.append(number)
# print(max(list))

# Маржовый оператор (:=) позволяет запрашивать значения элементов в интересных местах
list = []
while (number:=int(input("Введите число: "))) != 0:
    list.append(number)
print(max(list))

# Еще один вариант:
# nMax = -1
# while (n := int(input())) != 0:
#     if n > nMax:
#         nMax = n
# print(nMax)

# P.S. кортежи занимают немного меньше памяти, потому что они неизменяемы
# my_tuple = (1, 2, 3) - кортеж
# my_list = [1, 2, 3] - список
# print(my_tuple.__sizeof__())
# print(my_list.__sizeof__())