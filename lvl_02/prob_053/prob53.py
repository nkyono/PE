'''
There are exactly ten ways of selecting three from five, 12345:
123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

combinations ... in format (n r) ... is equal to n!/(r!(n-r)!) where r <= n
It is not until , that a value exceeds one-million: 
(23 10) = 1144066

How many, not necessarily distinct, values of (n r) for 1 <= n <= 100, are greater than one-million?

'''
import time

def calcFact(num):
    fact = 1
    while num > 0:
        fact = fact * num
        num = num - 1
    return fact

def calcCombs(n, r):
    if r > n:
        print("r must be less than n")
        return

    comb = calcFact(n) / (calcFact(r) * calcFact(n-r))
    return comb

def test():
    count = 0
    for n in range(1, 101):
        for r in range(n + 1):
            comb = calcCombs(n, r)
            if comb > 1000000:
                print(n, r, comb)
                count = count + 1
    print(count)

if __name__ == '__main__':
    assert calcCombs(23, 10) == 1144066
    assert calcFact(0) == 1
    assert calcFact(10) == 3628800
    start_time = time.time()
    test()
    print("--- %s seconds ---" % (time.time() - start_time))