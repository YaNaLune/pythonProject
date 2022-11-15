# 1 создание папки
# import os
# #1 вариант
# os.chdir('C:\\Users\\Администратор\\Desktop')
# print(os.getcwd())   # это для меня, чтобы видеть, что путь верный
# os.mkdir('new python file')
# #2 вариант
# #os.mkdir('C:\\Users\\Администратор\\Desktop\\MyNewFile')



# 2 удаление папки
# import os
# os.removedirs('C:\\Users\\Администратор\\Desktop\\MyNewFile')
# os.rmdir('C:\\Users\\Администратор\\Desktop\\new python file')



# 3 создание файла
# f = open('task_1.txt', 'w')    # файл в данной директории
# import os
# os.rename('task_1.txt', 'renamefile.txt')
#
# f = open('C:\\Users\\Администратор\\Desktop\\task_1.txt', 'w')   # файл на рабочем столе
# import os
# os.rename('C:\\Users\\Администратор\\Desktop\\task_1.txt', 'C:\\Users\\Администратор\\Desktop\\renamefile.txt')



# 4 cловарь из строки
# a = 'hellomynameis'
# b = {i: a.count(i) for i in a}
# print(b)


# 5 словарь из двух списков

