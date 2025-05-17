def iSort_desc(arr):
  
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

arr = [7,1,3,8,5,2,4,6]
print("initial array:", arr)
iSort_desc(arr)
print("Sorted array in descending order:", arr)
