# 作者：Alex
# 2024/10/18 02:57
def fibonacci_sequence(n):
    a, b, c = 1, 1, 0
    if n == 1 or n == 2:
        return 1
    else:
        for times in range(n-2):
            c = a + b
            a, b = b, c
        return c

"""def fibonacci_sequence(n):
    if n == 1 or n == 2:
        return 1
    result = fibonacci_sequence(n-1) +fibonacci_sequence(n-2)
    return result"""


print(fibonacci_sequence(100))