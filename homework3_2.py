import math
firstlist = list(map(int,input('Введите числа через запятую: ').split(',')))
newlist = []
for i in range(math.ceil(len(firstlist)/2)):
    newlist.append(firstlist[i]*firstlist[len(firstlist)-i-1])
print('Произведение пар чисел списка: ', newlist)