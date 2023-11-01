# take a list of even numbers in between 1 to 20
# if you find no. 16 continue and if you find out 18 then break the list.


# range (5) it will display 0 to 4

# for displaying 1 to 10

# for i in range(1,11,0): // range(start , stop , step) // by default the step increments to +1 for every iteration.
# print(i)

# a = []

# for i in range(2,22,2):
#        print(i)
#        if(i == 16):
#                break

# b = []

# for i in range(2,22,2):
#        print(i)
#        if(i == 16):
#                continue

# take a list of fruits select any fruits and break the loop at it.

# fruits = ["apple" , "mango" , "cherry" , "pineapple" ]

# for i in fruits:
#        if ( i == "mango"):
#                continue
#        print(i)

import random
a = 1
r = int(input("Enter Columns for matrix : "))
c = int(input("Enter Columns for matrix : "))

for i in range(r):
    for j in range(c):
        print( a , end="  ")
        a = a + 1
    print("\n")
