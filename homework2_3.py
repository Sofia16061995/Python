def sequenceСalculation(n):
    res = {i:round((1 + 1 / i)**i, 2) for i in range(1, n+1)}
    return res

n = int(input("Введите число N: "))

print(sequenceСalculation(n))