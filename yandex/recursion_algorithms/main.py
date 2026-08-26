count_disks = int(input())
count_iterations = 0
iterations = []

def hanoi_tower(count, fromPin, toPin):
    global count_iterations
    if count == 1:
        iterations.append(f'{fromPin} {toPin}')
        count_iterations += 1
        return
    unusedPin = 6 - fromPin - toPin
    hanoi_tower(count - 1, fromPin, unusedPin)
    iterations.append(f'{fromPin} {toPin}')
    count_iterations += 1
    hanoi_tower(count - 1, unusedPin, toPin)

hanoi_tower(count_disks, 1, 3)

print(count_iterations)
for msg in iterations:
    print(msg)