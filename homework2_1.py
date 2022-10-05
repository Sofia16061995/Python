def getSumDigital(n):
    sum = 0
    for i in number:
        sum += int(i)
    return sum

number = input("Введите вещественное число: ").replace(".", "").replace(",", "")

print(getSumDigital(number))