# 1
import os
# os.mkdir('C:\\Users\\Администратор\\Desktop\\Case')
# a = open('C:\\Users\\Администратор\\Desktop\\Case\\test_1.txt', 'w')
# b = open('C:\\Users\\Администратор\\Desktop\\Case\\test_2.txt', 'w')
# c = open('C:\\Users\\Администратор\\Desktop\\Case\\test_3.txt', 'w')
# os.rename('C:\\Users\\Администратор\\Desktop\\Case\\test_1.txt', 'C:\\Users\\Администратор\\Desktop\\Case\\rename_1.txt')
# os.rename('C:\\Users\\Администратор\\Desktop\\Case\\test_2.txt', 'C:\\Users\\Администратор\\Desktop\\Case\\rename_2.txt')
# os.rename('C:\\Users\\Администратор\\Desktop\\Case\\test_3.txt', 'C:\\Users\\Администратор\\Desktop\\Case\\rename_3.txt')
# os.remove('C:\\Users\\Администратор\\Desktop\\Case\\rename_1.txt')
# os.remove('C:\\Users\\Администратор\\Desktop\\Case\\rename_2.txt')
# os.remove('C:\\Users\\Администратор\\Desktop\\Case\\rename_3.txt')
# os.rmdir('C:\\Users\\Администратор\\Desktop\\Case')


# 2
# import random
# a = [random.randint(0,999) for i in range(10)]
# print('случайные числa -',a)
# b = sum(a) / len(a)
# print('среднее арифметическое данных чисел -',b)
# c = []
# for i in a:
#     if i < b:
#         c.append(i)
# print('числа меньше среднего арифметического -',c)


# 3
# a = {'cat',1,'dog',3,'bot',5,'love',7,'hello'}
# b = {1,'hello',3,7}
# if a == b:
#     print('множества одинаковые')
# elif a.issubset(b):
#     print('первое множество состоит из второго множества')
# elif b.issubset(a):
#     print('второе множество состоит из первого множества')
# if a.intersection(b):
#     print('пересечение множеств: ', a.intersection(b))
# else:
#     print('множества не пересекаются')


# 4
# a = 'An apple a day keeps the doctor away'
# b = a.replace(' ','')
# c = {i: b.count(i) for i in b}
# print(c)


# 5
# a = set()
# for i in range(10):
#     a.add(int(input('введи целое число: ')))
# print(a, type(a))


# 6
# songs = {'World in My Eyes': 4.76, 'Sweetest Perfection': 5.43,
#          'Personal Jesus': 4.56, 'Halo': 4.30, 'Waiting for the Night': 6.07,
#          'Enjoy the Silence': 4.6, 'Policy of Truth': 4.88,
#          'Blue Dress': 4.18, 'Clean': 5.68}
# a = songs.values()
# b = sum(a)
# print('общее время звучания песен: ', b)
# c = []
# for i in a:
#     if i > 5:
#         c.append(i)
# print('песни дольше пяти минут: ', c)
# d = {}
# for s in songs:
#     e = s.split()
#     if len(e) < 2:
#         d[s] = songs.get(s)
# print('песни с названием из одного слова: ', d)


# 7
# a = input('строка: ')
# b = []
# for i in a:
#     if i == ' ':
#         continue
#     if i not in b:
#         b.append(i)
# print('первые вхождения символов в строке: ', tuple(b))


# 8
# import random
# a = [random.randint(0, 999) for i in range(10)]
# print('дан массив -', a)
# b = int(input('удалить числа от: '))
# c = int(input('удалить числа до: '))
# for i in range(b, c+1):
#     if i in a:
#         a.remove(i)
#         a.append(0)
# print('итоговый массив -', a)


# 9
# import random
# a = int(input('строки матрицы: '))
# b = int(input('столбцы матрицы: '))
# print('матрица: ')
# mat = []
# for s in range(b):
#     matt = []
#     for i in range(a):
#         print('строка: ', s + 1)
#         ii = int(input('элемент: '))
#         matt.append(ii)
#     mat.append(matt)
# print(mat)
# sum = 0
# for s in range(1, a):
#     for i in range(0, s):
#         if mat[s][i] < 0:
#             sum += 1
# print('ответ: ', sum)


# 10
# import random
# a = [random.randint(0,30) for i in range(5)]
# max = max(a)
# min = min(a)
# b = 0
# for i in a:
#         if i > min and i < max:
#             b += i
# print('\n', 'числа: ', a, '\n', 'минимальное: ', min, '\n', 'максимальное: ', max, '\n', 'cумма, не включая макс и мин: ', b)