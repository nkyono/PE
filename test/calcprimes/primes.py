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

def main():
    numPrimes = 0
    primes = []
    for x in range(10000000):
        if calcDivisorsBool(x):
            primes.append(x)
            numPrimes = numPrimes + 1
    return

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:",time.time()-start)