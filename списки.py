# Создание списка - []
# a = list()
# print(a)


# Создадим список С и заполнение его десятью элементами от 0 до 100
# import random
# c = [random.randint(0,100) for i in range(10)]
# print(c)





# a = []  # создание списка
# a.append('hello')  # добавление в список
# print(a)




# a = [1, 2, 3, 'g']
# a.insert(1, 4)  # 1-элемент, который добавить     4-на какую позицию добавить (индекс)
# print(a)




# a = [1, 3, 5, 7, 'a', 'c']
# a[1] = 2      # 1 - индекс, куда добавить     2 - элемент, который добавить
# print(a)




# a = [1, 3, 5, 7, 'a', 'c']
# a.remove(1)     # удаляет элемент по его названию
# print(a)







# a = [1, 3, 5, 7, 'a', 'c']
# del a[0]     # удаляет элемент по индексу
# print(a)



# my_list = ['hello', 'world']
# elements = [1, 3, my_list, 6, 'a', 'b']
# del elements[2][1]    # 2-индекс в списке    1-индекс в элементе
# print(elements)





# a = [123, 456, 7, 'a', 'b']
# if 123 in a:
#     print('good')
# else:
#     print('bad')





# a = [1, 2, 3]
# b = [4, 5, 6, 7]
# print(a+b)
#
# c = ['abd', 'defg', 'higk']
# d = ['a', 'b', 'c']
#
# c.extend(d)
# print(c)






# a = [1, 2, 3, 'meow']
# for i in a:
#     print(i)
#
#
#
# a = [1, 2, 3, 'meow']
# a1 = len(a)
# i = 0
# while i < a1:
#     print(a[i])
#     i += 1




# clear
# a = [1, 2, 3]
# a.clear()
# print(a)


# copy
# a = [1, 2, 3]
# b = a.copy()
# print(id(a), id(b), a, b)


# count
# a = ['one', 'two,', 'three']
# print(a.count('one'))


# index
# a = ['one', 'two,', 'three']
# print(a.index('three'))



# a = [1, 2, 3, 4]
# a.reverse()  # в обратном порядке
# print(a)



# a = [10, 20, 30, 40, 50]
# a[a.index(20)] = 200
# print(a)


# a = [0, 1, 2, 3, 4, 5, 6]
# b = 0
# c = 0
# for i in a:
#     if i % 2 == 0




# Задание по спискам перед экзаменом
# list = [15,48,'hello',6,19,'world']
# a = 0
# b = 0
# c = 0
# for i in list:
#     if type(i) is int:
#         if i % 2 == 0:
#             i = str(i)
#             for s in i:
#                 s = int(s)
#                 a += s
#             print(i,'summ: ',a,'\n')
#         else:
#             x = list.index(i) #ищем нечётные цифры
#             list[x] = 1 #заменяем на единицу
#     elif type(i) is str:
#         for n in i:
#             if n in 'a,e,i,o,u,y':
#                 b += 1
#             else:
#                 c += 1
#         print(i,'glasn: ',b)
#         print(i,'soglasn: ',c,'\n')
#         b = 0
#         c = 0
# print(list)