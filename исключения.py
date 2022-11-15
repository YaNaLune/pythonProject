# try:
#     k = 1 / 0
# except ArithmeticError:
#     k = 0
# print(k)


# di = {'a':1, 'b':2, 'c':3}
# try:
#     val = di['d']
# except KeyError:
#     print('Ключа не существует!')


# di = {'a':1, 'b':2, 'c':3}
# try:
#     value = di['d']
# except IndexError:
#     print('такого индекса нет')
# except KeyError:
#     print('такого ключа нет')
# except:
#     print('другая ошибка')


# di = {'a':1, 'b':2, 'c':3}
# try:
#     val = di['d']
# except (IndexError, KeyError):
#     print('ошибка IndexError или KeyError')


# DZ
# while True:
#     num1 = input('first num ')
#     num2 = input('second num ')
#     try:
#         result = int(num1) / int(num2)
#     except ValueError:
#         print('dont use letters')
#         break
#     except ZeroDivisionError:
#         print('dont divide by zero')
#     else:
#         print(result)
#         break