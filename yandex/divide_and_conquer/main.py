count = int(input())
numbers = list(map(int, input().split()))

for i in range(count - 1):
    for j in range(i + 1, count):
        if numbers[i] > numbers[j]:
            numbers[i], numbers[j] = numbers[j], numbers[i]

print(' '.join(str(number) for number in numbers))
