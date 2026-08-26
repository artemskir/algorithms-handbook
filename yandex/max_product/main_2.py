count = int(input())

def checker(count):
    if count > 6:
        print("Yes")
        data_output = [count] + [i for i in range(1, count)]
        print(*data_output)
    else:
        print("No")

checker(count)