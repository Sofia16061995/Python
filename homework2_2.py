def getMultiplicationOfNumbers(n):
    res = [factorial(i) for i in range(1, n+1)]
    return res

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

n = int(input("Введите число N: "))

print(getMultiplicationOfNumbers(n))