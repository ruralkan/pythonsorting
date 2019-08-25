def selectionSort(arr):
    for i in range(len(arr)):
        minIndex = i
        for j in range((i + 1), len(arr)):
            if arr[minIndex]> arr[j]:
                minIndex = j
        arr[i], arr[minIndex] = arr[minIndex], arr[i]
    return arr

test = [1,3,2,9,4,18,45,37,63]

sorted = selectionSort(test)
print(sorted)