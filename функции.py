# def a_function():
#     print('You just created a function')
# a_function()
# a_function()
# a_function()

# def empty_function():
#     pass
# empty_function()

# def summ_in_massiv():
#     a = [1,2,3,4,5]
#     b = sum(a)
#     print(b)
# summ_in_massiv()

# def add(a, b):
#     return a + b
# #print(add(1, 2))
# print(add(a=2, b=3))
# print(add(b=4, a=5))

# def mix_fun(a, b=1, c=3):
#     return a + b + c
# print(mix_fun(1,b=2,c=4))
# print(mix_fun(1))

# def many(*args, **kwargs):
#     print(args)
#     print(kwargs)
# many(1, 2, 'a', hello=1, name='Bob', job='programmer')

# def fun_a():
#     global a
#     a = 1
#     b = 2
#     return a + b
# def fun_b():
#     c = 3
#     return a + c
# print(fun_a())
# print(fun_b())

# def func1(a, b):
#     def inner_func(x):
#         return x * x * x
#     return inner_func(a) + inner_func(b)
# print(func1(4, 5))

def sum(a, b): return a + b
print(sum(1, 5))
