# Implementing linear search for and specific target value in an array

array = [5 , 1 , 3 , 2 , 6 , 7]
print("This is a given array : ")
for x in array:
    print(f"{x}")
print("\n")

# target = int(input("Enter Traget value to be searched in Array : "))


# Linear Search    Best case O(1)  Worst case O(n)

# for i in range(len(array)):
#     if(array[i] == target):
#         print("Target Found at index no." , i)
#         break
#     else:
#         print("Target not found at index no.", i)


# Binary Search   Best case O(1)  Worst case O(log n)

# low = 0 
# high = len(array)

# while(low <= high):
#     mid = int((low + high) / 2)

#     if(array[mid] == target):
#         print(f"Traget found at index no {mid} in Array")
#         break

#     if(target > array[mid]):
#         low = mid + 1 
#     elif(target < array[mid]):
#         high = mid - 1
    
#     print(f"Traget found at index not found at {mid} in Array \n")



# Bubble Sort 
isSorted = 0

for i in range(len(array)-1):
    for j in range(len(array)-1-i):
        isSorted = 1
        if(array[j] > array[j+1]):
            array[j] , array[j+1] = array[j+1] , array[j]
            isSorted = 0

    if isSorted:
        break

print("Sorted Array")
print("This is a given array : ")
for x in array:
    print(f"{x}")


