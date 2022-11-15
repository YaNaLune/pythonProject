# num = dict(zip([1, 2, 3], ['one', 'two', 'three']))
# print(num)


# month = {1: 'jan', 2: 'feb', 3: 'mar'}
# for m in month:
#     print(m, ': ', month[m])


# person = {'name': str(input('name: ')), 'age': int(input('age: ')), 'city': str(input('city: '))}
# print('age: ', person['age'])




# DZ-1
# dict = {'apple':[2000, 5], 'samsung':[1000, 10], 'xiaomi':[500, 15], 'huawei':[500, 20]}
# for i, s in dict.items():
#     print(i, '-', s[0], '-', s[1])
# a = 0
# while True:
#     b = input('your choice: \n (n - nothing) ')
#     if b == 'n' or b not in dict.keys():
#         break
#     c = int(input('amount: '))
#     if c > dict[b][1]:
#         print("we haven't enough:(")
#         continue
#     a += dict[b][0] * c
#     dict[b][1] -= c
# print('your check: ', a, '\n', 'now we have: ')
# for i, s in dict.items():
#     print(i, '-', s[0], '-', s[1])