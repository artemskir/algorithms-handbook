count = int(input())
data = list(map(int, input().split()))

def quick_sort(data, low, high):
    if low < high:
        part = partition_lomuto(data, low, high)
        quick_sort(data, low, part - 1)
        quick_sort(data, part + 1, high)

def partition_lomuto(data, low, high):
    i = low - 1
    pivot_index = (low + high) // 2
    data[pivot_index], data[high] = data[high], data[pivot_index]
    pivot = data[high]
    for element in range(low, high):
        if data[element] <= pivot:
            i += 1
            data[element], data[i] = data[i], data[element]
    data[i + 1], data[high] = data[high], data[i + 1]
    return i + 1

quick_sort(data, 0, len(data) - 1)
print(' '.join(str(number) for number in data))