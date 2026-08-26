count = int(input())
data = list(map(int, input().split()))

def partition_lomuto(data):
    i, pivot = 0, data[0]
    for index in range(1, len(data)):
        if data[index] <= pivot:
            i += 1
            data[index], data[i] = data[i], data[index]
    data[i], data[0] = pivot, data[i]

partition_lomuto(data)
print(' '.join(str(number) for number in data))