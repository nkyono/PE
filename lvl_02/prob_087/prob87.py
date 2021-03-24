'''
The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. 
In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, 
prime cube, and prime fourth power?
'''
# 50000000 ** (1/2), a loose estimate of max prime size == 7071.067811865475
# 50000000 ** (1/3), a loose estimate of max prime size == 368.40314986403854
# 50000000 ** (1/4), a loose estimate of max prime size == 84.08964152537145
def calcDivisorsBool(target):
    if target < 0:
        return False
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                return False
            else:
                return False
    return True

def testIter(two, three, four):
    # used a set because I missed the fact that there could be numbers created in multiple ways
    nums = set()
    for a in two:
        for b in three:
            for c in four:
                num = a**2 + b**3 + c**4
                if (num < 50000000):
                    nums.add(num)
    return len(nums)

def main():
    primesTwo = []
    primesThree = []
    primesFour = []

    # from these loops we get the possible primes for each power
    for x in range(2,86):
        if calcDivisorsBool(x):
            primesFour.append(x)
            primesThree.append(x)
            primesTwo.append(x)
    for x in range(86,370):
        if calcDivisorsBool(x):
            primesThree.append(x)
            primesTwo.append(x)
    for x in range(370,7073):
        if calcDivisorsBool(x):
            primesTwo.append(x)
    
    print(testIter(primesTwo, primesThree, primesFour))

    return

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("test:",time.time()-start)