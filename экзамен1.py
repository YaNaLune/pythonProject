# 1
# print(4 ** 4 ** 4)


# 2
# a
# import math
# a = 1
# print((((1 + a + a ** 2) / (2 * a + a ** 2) + 2 - (1 - a + a ** 2) / (2 * a - a ** 2)) ** (-1)) * (5 - 2 * a ** 2))
# b
# from math import sin
# a = 90
# b = 90
# y = 90
# print(1 / 4 * (sin(a + b - y) + sin(b + y - a) + sin(y + a - b) - sin(a + b + y)))


# 3
# a = ()
# print(bool(a)) # в переменной пусто или 0 - значит False, иначе - True


# 4
# m = int(input("введите меньшее число: "))
# n = int(input("введите большее или равное число: "))
# for i in range(m, n+1):
#     print(i, end='\t')


# 5
# m = int(input("введите первое число: "))
# n = int(input("введите второе число: "))
# if m<n:
#     for i in range(m, n+1):
#         print(i)
# if m>n:
#     for i in range(m, n-1, -1):
#         print(i)


# 6
# str = 'Марк Махнач'
# a = str.split(' ')
# print(a[1], a[0] )


# 7
# print(list([c for c in range(1, 51)]))


# 8
# a = [1, 5, 2, 9, 2, 9, 1]
# for i in a:
#     b = a.count(i)
#     if b < 2:
#         print(b)


# 9
# a = ['student1', 'student2', 'student3']
# b = []
# for i in a:
#     b.append(i + '_good')
# a = b
# print(b)


# 10
# for i in range(51):
#     if i == 35:
#         continue
#     print(i)

# 11
# s = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
# s1 = []
# for i in s:
#     if i.find(' ') != -1:
#         s1.append(i)
# print(s1)