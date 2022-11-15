# a = {'hello', 2, (1,2,3)}
# print(a)


# a = set([1,2,3,4,3,2,1])
# print(a)


# x = set()
# print(type(x))


# a = set(['one', 'two', 'three', 'four', 'five'])
# for i in a:
#     print(a)


# a = set(['a', 'b', 'c'])
# print('a' in a)
# print('e' in a)



# a = set(['good','beauty','love'])
# a.add('lol')
# print(a)


# a = {1,2,3,4,5,6,7}
# a.pop()
# print(a)


# a = {1,2,3,4,5,6,7,8,9}
# a.clear()
# print(a)


# a = set(['a','b','c'])
# b = set(['d','e','f'])
# c = a.union(b)
# print(c)



# a = {1,2,3}
# b = {3,4,5}
# c = {5,6,7}
# # d = a.union(b,c)
# # print(d)
# print(a | b | c)



# a = [1,2,3,4,5,4]
# b = set(a)
# if len(a) == len(b):
#     print('дубликатов нет')
# else:
#     print('дубликаты есть')



# a = {1:'one', 2:'two', 3:'three'}
# print("исходный словарь: ", a)
# a['cucumber']=5
# print("добавили строчный ключ и циферное значение: ", a)
# a[('mini', 'pig')]=['cat', 'dog']
# print("добавили кортежный ключ и списковое значение: ", a)
# b = a[1]
# print("вывели значение ключа 1: ", b)
# del a[3]
# print("удалили ключ 3 и его значение: ", a)
# print("вывели названия ключей: ", a.keys())