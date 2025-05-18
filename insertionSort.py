def iSort_desc(arr):
  
    for i in range(1, len(arr)): # Start from the second element
        key = arr[i]
        j = i - 1 #comparing with the previous element

        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]  # Shifting the smaller element to the right
            j -= 1
        
         # Inserting the key at the correct position
        arr[j + 1] = key

arr = [7,1,3,8,5,2,4,6]
print("initial array:", arr)
iSort_desc(arr)
print("Sorted array in descending order:", arr)
