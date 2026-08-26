m_number, n_number = map(int, input().split())

def fibonacci_mod(n):
    period = 60
    n = n % period

    if n == 0:
        return 0

    previous, current = 0, 1
    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

number_n = fibonacci_mod(n_number + 2)
number_m = fibonacci_mod(m_number + 1)
last_digit = (number_n - number_m) % 10
print(last_digit)