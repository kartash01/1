from decimal import Decimal, getcontext
from math import ceil, factorial

n = int(input())
num = n + 2

def pi(num):
    if num < 1:
        print('Вы ввели недействительное число')
    else:
        getcontext().prec = num
        num_iter = ceil(num / 14)
        constant = 426880 * Decimal(10005).sqrt()
        exp = 1
        numbr = 13591409
        part = Decimal(numbr)
        
        for k in range(1, num_iter):
            a = factorial(6 * k) // (factorial(3 * k) * factorial(k) ** 3)
            numbr = numbr + 545140134
            exp = exp * -262537412640768000
            part += Decimal(a * numbr) / exp
        return str(constant / part)[:-1]

print(pi(num))
