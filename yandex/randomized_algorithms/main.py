count = int(input())

data = list(map(int, input().split()))


def partition_lomuto(data):
    pivot = data[0]
    i = 0
    for element in range(1, len(data)):
        if data[element] <= pivot:
            i += 1
            data[i], data[element] = data[element], data[i]
    data[0], data[i] = data[i], data[0]


partition_lomuto(data)
print(' '.join(str(number) for number in data))
