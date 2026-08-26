n_number, m_number = map(int, input().split())

def pisano_period(m):
    previous, current = 0, 1
    period = 0
    while True:
        next_number = (previous + current) % m
        previous = current
        current = next_number
        period += 1
        if previous == 0 and current == 1:
            return period

def fibonacci_mod(n, m):
    period = pisano_period(m)
    n = n % period

    if n == 0:
        return 0

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % m

    return current

print(fibonacci_mod(n_number, m_number))