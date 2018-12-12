def factorial(n):
    if n < 0:
        raise ValueError("Out of Range","-ve nos dont have factorials")
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(10))
print(factorial(0))
print(factorial(1))
print(factorial(-10))
