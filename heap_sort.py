def heap_sort(arr):
    n = len(arr)

    # построение кучи
    for i in range(n // 2):
        heapify(arr, n, i)

    # извлечение элементов из кучи и сортировка
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0] # поменять максимум с последним элементом
        heapify(arr, i, 0) # перестроить кучу

# перестройка кучи
def heapify(arr, n, i):
    largest = i # инициализация наибольшего элемента как корневой(первый)
    left = 2 * i + 1 # левый дочерний элемент
    right = 2 * i + 2 # правый дочерний элемент

    if left < n and arr[left] > arr[largest]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i] # поменять местами с корневым узлом
        heapify(arr, n, largest)

# Тестирование работы алгоритма
arr = [12, -11, 13, 5, 0, 7, 8]
print(arr)
heap_sort(arr)
n = len(arr)
print(f"Отсортированный массив: {arr}")