firstlist = list(map(int,input('Введите числа через запятую: ').split(',')))
sum =0
for i in range(1, len(firstlist), 2):
    sum+=firstlist[i]
print('Исходный список: ', firstlist)
print('Сумма элементов, стоящих на нечетной позиции: ', sum)