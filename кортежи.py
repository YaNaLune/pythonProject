# a = (1, 2, 3, 4, 5, 6, 7)
# print(a[0:4])
# print(a[:4])
# print(a[1:])
# print(a[2::2])
# print(a[::2])


# a = (10, 2.13, 'square', 89, 'c')
# b = [1, 2, 3]
# c = list(a)
# d = tuple(b)
# print(c,  d)


# nested = (1, 'do', ["param", 10, 20])   # изменение списка в кортеже
# nested[2][1] = 15
# print(nested)



# x = (1, 2, 3, 4)
# y = (5, 6, 7, 8)
# z = x+y
# print(z)



# x = (1, 2, 3, 4)
# z = x * 2
# print(z)



# x = 1, 2, 3, 4 # запятая позволяет создать кортеж
# print(x)


# x = ()
# print(x)


#var1
# import math
# import random
# a = []
# for i in range(11):
#     a.append(random.randint(0, 100))
# a = tuple(a)
# print(sorted(a))
# print('min - ', min(a), '\n'+'max - ', max(a))

#var2
# import random
# a = tuple([random.randint(0, 9999) for i in range(10)])
# print(a)
# print('max - ', max(a), '\n'+'min - ', min(a))



# import random
# a = tuple([random.randint(0, 5) for i in range(10)])
# b = tuple([random.randint(-5, 0) for s in range(10)])
# c = a + b
# print(c, 'zero: ', c.count(0))



# a = ('God', 'Is', 'Love')
# b = ','.join(a)
# print(b)


# import random
# a = tuple([random.randint(0, 999) for i in range(10)])
# b = tuple([random.randint(0, 999) for s in range(10)])
# print(a,'\t', b)
# a1 = sum(a)
# b1 = sum(b)
# if a1 > b1:
#     print("Сумма больше в кортеже - а")
# else:
#     print("Сумма больше в кортеже - b")
# print('min a', min(a), 'Number - ', a.index(min(a)))
# print('min b', min(b), 'Number - ', b.index(min(b)))




# a = (1,) # всегда нужно ставить запятую для создания кортежа
# print(type(a))

# a = ('hello', 'g', 'g', 'world')
# print(min(a))
# print(a.count('g'))


# import random
# a = ([random.randint(0,100) for i in range(10)])
# print(type(a))
# b = tuple(a)
# print(type(b))



# 1
# a = 'hello my friends'
# print(a)
# print(type(a))
# b = a.split()
# print(b)
# c = 0
# e = 0
# for i in b:
#     if len(b) < len(b[e]):
#         c = e
#     e += 1
# print(b[c])



# 2
# A = 'HELLO! HOW ARE YOU?'
# B = ['!', '?']
# C = A.split()
# D = 0
# E = 0
# for E in C:
#     if E[-1] in B:
#         C[D] = E[:-1]
#         E = C[D]
#     if E[0] in B:
#         C[D] = E[1:]
#     D += 1
# for E in C:
#     print(E, end=" ")
# print()