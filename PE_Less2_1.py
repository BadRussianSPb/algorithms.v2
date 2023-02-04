# Реализовать алгоритм пирамидальной сортировки (сортировка кучей).

def heapify(arr, n, el):
    largest = el
    left_leaf = el * 2 + 1
    right_leaf = el * 2 + 2

    # если лист (правый или левый больше корня - свопаем)
    if left_leaf < n and arr[el] < arr[left_leaf]:
        largest = left_leaf

    if right_leaf < n and arr[largest] < arr[right_leaf]:
        largest = right_leaf

    if largest != el:
        arr[el], arr[largest] = arr[largest], arr[el]
        heapify(arr, n, largest)


def heapsort(arr):
    n = len(arr)
    print("Размер массива: ", n)
    for el in range(n, -1, -1):
        heapify(arr, n, el)

    for el in range(n-1, 0, -1):
        arr[el], arr[0] = arr[0], arr[el]
        heapify(arr, el, 0)


if __name__ == "__main__":
    x = [9, 12, 1, -7, -6, 0, 5]
    print("Задан массив: ", x)
    heapsort(x)
    print("Результат сортировки: ", x)
