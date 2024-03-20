<<<<<<< HEAD
def sumOfN(n):
    if n == 1:
        return 1
    return n + sumOfN(n-1)
def fact(n):
    if n == 0:
        return 1
    return n * fact(n-1)

print(fact(5))
=======
def sumN(n):
     if n == 1:
          return 1
     return n + sumN(n-1)

def sumNOdd(n):
     if n == 1:
          return 1
     return 2*n-1 + sumNOdd(n-1)
def sumNEven(n):
     if n == 2:
          return 2
     return 2*n-1 + sumNEven(n-1)
def fact(n):
     if n==0:
          return 1
     return n* fact(n-1)
def sumSquareN(n):
     if n == 1:
          return 1
     return n*n + sumSquareN(n-1)
print(sumSquareN(5))
>>>>>>> 18b7b1b105fa595d6539b0b8c6a8e88dcc85ddb2
