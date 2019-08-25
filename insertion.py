def insertionSort(arr):
    for i in range(1, len(arr)):
        store = arr[i]
        j = i -1
        while j >= 0 and store < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = store
    return arr

test = [1,3,2,9,4,18,45,37,63]
sorted = insertionSort(test)
print(sorted)
