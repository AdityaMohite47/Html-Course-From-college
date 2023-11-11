# 1. No Arguments return value

# def add():
#     a = 2
#     b = 4
#     c = a+b
#     print(c)


# add()

# 2. Arguments passed return value

# def add(a , b):
#     print(a+b)


# add(2,4)


# if we are not sure how many are the args passed to the function then we use '*' before an argument :
# This are aribitary Function :

# def number(*x):
#     for i in x :
#         print(i)

# number(1,2,3,4,5)


# This is a Nested Function :

# def add():
#     x=2
#     y=3

#     c = x+y

#     def show():
#         print(c)

#     show()

# add()


# This is a Anonymous Function :
# the function which dosen't have name
# we use lambda instead of def keyword.

# def cube(x):
#     return x*x*x  This is a normal function.


# Anonymus function

# syntax :
#     lambda args : code or functions


# cube2 = lambda x: x*x*x     # defining lambda function.

# print(cube2(4))             # calling the function.

# Anonymus function with filter() function

# Keyword function
# from operator import concat // header for string functions in latest python.


# def name(name1 , name2):
#     print(concat(name1,name2))

# name(name1="sohan",name2="Pendhari")


# Examples of functions

# find odd numbers from a list using anonymus function

# from ast import List
# from logging import Filter


# array_nums = [1, 2, 3,4, 5, 7, 8, 9, 10]
# print("Original arrays:")
# print(array_nums)
# odd = list(filter(lambda x: (x%2 != 0) , array_nums))
# even = list(filter(lambda x: (x%2 == 0) , array_nums))
# print("\nNumber of even numbers in the above array: ", even)
# print("\nNumber of odd numbers in the above array: ", odd)


# find cube of a given number anonymus function using map()

# from ast import List
# a = {2 , 4 , 6 , 8 , 10}
# print(a)

# cube = List(map(lambda x:x**3,a))

# print("The list of cube of all elements of list is : ")



# using random function generate a random list and print it

    



