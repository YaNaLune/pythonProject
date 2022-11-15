#1
# x = int(input("x - "))
# y = int(input("y - "))
# print((abs(x) - abs(y)) / (1 + abs(x*y)))


#2
# import math
# print("Дан прямоугольный треугольник")
# a = int(input("a - первый катет: "))
# b = int(input("b - второй катет: "))
# print("с - гипотенуза: ", math.sqrt((a**2)+(b**2)))
# print("S - площадь: ", a*b / 2)



#3
# a = 9
# b = 17
# c = 5
# if a > b:
#     print("a", True)
# elif a != (b-c):
#     print("b", True)
# elif b == (a+c):
#     print("c", True)
# elif c <= (a+b):
#     print("d", True)
# elif a < b and a > c:
#     print("e", True)
# elif b > a or b > c:
#     print("f", True)



#4
# a = "Robin Singh"
# print(a.split(" "))
# b = "I love arrays they are my favorite"
# print(b.replace('arrays', 'lists').split(" "))




#5
# a = ['"I', 'love', 'lists', 'they', 'are', 'my', 'favorite"']
# del a[2]
# a.insert(2, "arrays")
# print(' '.join(a))



#5(проще)
# a = ['"I', 'love', 'lists', 'they', 'are', 'my', 'favorite"']
# print(' '.join(a).replace('lists', 'arrays'))




#6
# a = [-8, 1, 2, -2, 0]
# b = [1, -1, 0, -9, 4, -5]
# c = [1, 4, 0, 23, 6, 34]
# a1 = sorted(a)
# b1 = sorted(b)
# c1 = sorted(c)
# print(a1[1], b1[1], c1[1])



#7
# arr = ['red', 'green', 'white', 'black', 'pink', 'yellow']
# arr1 = [arr[0], arr[4], arr[5]]
# print(arr1)




#8
# m = int(input("введите меньшее число: "))
# n = int(input("введите большее или равное число: "))
# for i in range(m, n+1):
#     print(i, end='\t')




#9
# m = int(input("введите первое число: "))
# n = int(input("введите второе число: "))
# i = "результат: "
# if m<n:
#     for i in range(m, n+1):
#         print(i)
# if m>n:
#     for i in range(m, n-1, -1):
#         print(i)



#10
# print("Сколько будет 3+4-7 ?")
# i = 0
# while i < 3:
#     i += 1
#     a = int(input("Введите ответ: "))
#     if a != 0:
#         print("Не правильно, ещё варианты?")
#     if a == 0:
#         print("Это правильный ответ!")
#         break
# else:
#     print("Попробуйте снова.")



#11
# a = [1, 3, 10, 20, 25, 20]
# for i in a:
#     if i == 20:
#         a.remove(20)
# print(a)



# 12
# a = []
# i = 0
# a.insert(0, 1)
# while i < 100:
#     a.insert(0+1, 0)
#     i += 1
# if i == 100:
#     a.insert(101, 1)
# print(a)



#13
# a = []
# for i in range(90):
#     if i % 2 == 0:
#         a.append(i)
# print(a)
# b = len(a)
# print(b)




#14
# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = []
# for i in (a):
#     if i < 5:
#         b.append(i)
# print(a)
# print(b)


# for i in range(5):
#     if i % 2 == 0:
#         continue
#     print(i)


# i = 0
# while i < 10:
#     i += 1
# i -= 10
# print(i)


# for i in range(1,10):
#     i -= 5
# print(i)


# print(str('a' + 'x' if '123'.isdigit() else 'y' + 'b'))


# print(
#     '$100 $200 $300'.count('$'),
#     '$100 $200 $300'.count('$', 5, 10),
#     '$100 $200 $300'.count('$', 5)
# )


# s = [0, 1, 2, 3, 4, 5, 6, 7]
# print(s[::-3])