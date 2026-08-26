n_number = int(input())
storage = []

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    storage.append(0)
    storage.append(1)

    for i in range(2, n + 1):
        storage.append(storage[i - 2] + storage[i - 1])

    return storage[n]

print(fibonacci(n_number))