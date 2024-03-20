def sumOfN(n):
    if n == 1:
        return 1
    return n + sumOfN(n-1)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))