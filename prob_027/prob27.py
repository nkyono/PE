'''
Euler discovered the remarkable quadratic formula:
n^2 + n + 41

It turns out that the formula will produce 40 primes for the consecutive integer values . 
However, when  is divisible by 41, and certainly when  is clearly divisible by 41.

The incredible formula n^2 - 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values 0 <= n <= 79. 
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n^2 + an + b, where |a| < 1000 and |b| <= 1000
where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes for consecutive values of n, 
starting with n = 0.
'''

def calcDivisors(target):
    if target < 0:
        return False
    divisors = []
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
                return False
            else:
                divisors.append(i)
                divisors.append(target/i)
                return False
    return True

def testFormula():
    top = {}
    n = 0
    i = 0

    for x in range(-1000, 1000):
        for y in range(-1001, 1001):
            num = (i**2) + (x*i) + y
            while calcDivisors(num):
                n = n + 1
                i = i + 1
                num = (i**2) + (x*i) + y
            if x*y in top:
                if top[x*y] < n:
                    top[x*y] = n
            else:
                top[x*y] = n
            #if n > 20:
            #    print(x, y, x*y, n)
            n = 0
            i = 0

    ans = 0
    index = 0
    for z in top:
        if top[z] > ans:
            # print(index, ans)
            ans = top[z]
            index = z
    print(index, ans)

def main():
    testFormula()

if __name__ == '__main__':
    main()