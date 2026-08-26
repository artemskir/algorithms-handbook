count_disks = int(input())
moves = []
def hanoi3(ndisks, start=1, end=3):
    if ndisks:
        hanoi3(ndisks - 1, start, 6 - start - end)
        moves.append((start, end))
        hanoi3(ndisks - 1, 6 - start - end, end)
    else:
        return moves

def FrameStewart_Count(ndisks, nrods):
    if ndisks == 1 and nrods > 1:
        return (1, 1)
    if nrods == 3:
        return (2**ndisks - 1, 1)
    if nrods >= 3 and ndisks > 0:
        solutions = []
        for kdisks in range(1, ndisks):
            solutions.append((2 * FrameStewart_Count(kdisks, nrods)[0] + 
                              FrameStewart_Count(ndisks - kdisks, nrods - 1)[0], 
                              kdisks))
        return min(solutions, key=lambda x: x[0])

print(FrameStewart_Count(count_disks, 4)[0])
