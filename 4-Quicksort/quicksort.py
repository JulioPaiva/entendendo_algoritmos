def quicksort(arr):
    if len(arr) == 0:
        return arr
    else:
        pivo = arr[0]
        menores = quicksort([i for i in arr[1:] if i <= pivo])
        maiores = quicksort([i for i in arr[1:] if i > pivo])

        return menores + [pivo] + maiores


arr = quicksort([10, 5, 2, 3])
print(arr)
