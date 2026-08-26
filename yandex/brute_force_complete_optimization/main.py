value = int(input())
output = 1
if value == 0:
    print(value)
else:
    for i in range(value + 1):
        if i == 0:
            continue
        output *= i

    print(output)
