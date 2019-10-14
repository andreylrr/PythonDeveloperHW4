import re
import multiset
#
#  Модуль 3 из домашнего задания для 4 вебинара.
#
#  Пользователь вводит элементы 1-го списка
#  Затем он вводит элементы 2-го списка
#  Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран

s_input = input("Введите элементы для первого списка через разделитель [,:/]: ")
l_numbers1 = map(int, re.split(",|:|/", s_input))
s_input = input("Введите элементы для второго списка через разделитель [,:/]: ")
l_numbers2 = map(int, re.split(",|:|/", s_input))
print(list(multiset.Multiset(l_numbers1)-multiset.Multiset(l_numbers2)))
