n_number = int(input())
storage = []

def fibonacci_numbers(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    elif n == 2:
        return 1
    if n < 7:
        return storage[n - 2] + storage[n - 1]
    return (storage[n - 2] + storage[n - 1]) % 10

for i in range(n_number + 1):
    storage.append(fibonacci_numbers(i))

if n_number == 0:
    print(0)
elif n_number == 1:
    print(1)
elif n_number == 2:
    print(1)
else:
    print(storage[n_number])
