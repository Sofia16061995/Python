from decimal import*
d = Decimal(input('Введите точность d: '))
a = 1
sum = 0
sign = 1
while 4/a >= d:
    sum += (4/a)*sign
    sign = -sign
    a += 2
print(str(sum)[:len(str(Decimal(d)))])