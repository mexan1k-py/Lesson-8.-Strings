#Homework 1
slv = str(input('Введите слово которе нужно проверить: '))

a = slv[::-1]

if slv == a:
    print('Yes')
else:
    print('No')

#Homework 2
string = str(input('Введите строку: '))

a = ''.join(string.split())
print(a)