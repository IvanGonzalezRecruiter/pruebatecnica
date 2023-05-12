def ordenar(array):
    for i in range(len(array)):
        min_idx = i
        for j in range(i + 1, len(array)):
            if array[j] < array[min_idx]:
                min_idx = j
    array[i], array[min_idx] = array[min_idx], array[i]

array=[7, 5, 4, 9, 2]
ordenar(array)
print("El array ordenado es: ", array)
