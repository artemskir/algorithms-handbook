n, m = map(int, input().split())

experience = [[0] * (m + 1) for _ in range(n + 1)]

"""
Взять один камень из любого набора.
Взять два камня из какого-то одного набора
Взять два камня из одного и один из другого.
"""
def rocks(n, m):
    if m >= 1:
        experience[0][1] = 1
    if n >= 1:
        experience[1][0] = 1
    if n >= 1 and m >= 1:
        experience[1][1] = 0
    experience[0][0] = 0
    if n > 0:
        for i in range(1, n + 1):
            if experience[i - 2][0] == 1 and experience[i - 1][0] == 1:
                experience[i][0] = 0
            else:
                experience[i][0] = 1
    if m > 0:
        for j in range(1, m + 1):
            if experience[0][j - 2] == 1 and experience[0][j - 1] == 1:
                experience[0][j] = 0
            else:
                experience[0][j] = 1
    if n > 0 and m > 0:
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if experience[i - 1][j - 1] == 0 and experience[i - 1][j] == 1 and experience[i][j - 1] == 1:
                    experience[i][j] = 0
                else:
                    experience[i][j] = 1
    return experience[n][m]

output = rocks(n, m)
if output == 1:
    print("Win")
else:
    print("Lose")