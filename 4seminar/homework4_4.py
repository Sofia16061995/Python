import random
k = int(input('Введите степень многочлена: '))
result = ''
for i in range(k,0,-1):
    a = '*x^'+ str(i)
    result +=(str(random.randint(0,100)) + a+ ' + ')
polinomial = result + str(random.randint(0,100)) + '= 0'
data = open('polinomial.txt', 'w')
data.writelines(polinomial)
data.close()