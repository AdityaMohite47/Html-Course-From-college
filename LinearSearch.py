# Implementing linear search for and specific target value in an array

array = [2 , 4 , 6 , 3 , 1 , 5]
target = int(input("Enter Traget value to be searched in Array : "))

for i in range(len(array)):
    if(array[i] == target):
        print("Target Found at index no." , i)
        break
    else:
        print("Target not found at index no.", i)









