
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

# This is Anonymus function

# syntax :
#     lambda args : code or functions


# cube2 = lambda x: x*x*x     # defining lambda function.

# print(cube2(4))             # calling the function.


