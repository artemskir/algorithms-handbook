rocks_my, rocks_opponent = map(int, input().split())

experience = [[0] * 10 for i in range(10)]

def rocks(n, m):
    experience[0][0] = 0
    for i in range(n):
        if experience[i-1][0] == 1:
            experience[i][0] = 0
        else:
            experience[i][0] = 1
    for j in range(m):
        if experience[0][j-1] == 1:
            experience[0][j] = 0
        else:
            experience[0][j] = 1
    for i in range(n):
        for j in range(m):
            if experience[i-1][j-1] == 1 and experience[i][j-1] == 1 and experience[i-1][j] == 1:
                experience[i][j] = 0
            else:
                experience[i][j] = 1
    return experience[n - 1 if n - 1 > 0 else 0][m - 1 if n - 1 > 0 else 0]

output = rocks(rocks_my, rocks_opponent)
if output == 1:
    print("Win")
else:
    print("Lose")