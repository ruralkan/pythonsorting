def bubbleSort(arr):
    for i in range(len(arr)-1):
        if arr[i+1]< arr[i]:
            arr[i], arr[i+1]= arr[i+1], arr[i]
    return arr

test = [1,3,2,9,4,18,45,37,63]

sorted = bubbleSort(test)
print(sorted)