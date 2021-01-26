def fact(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
        yield factorial


for el in fact(5):
    print(el)
