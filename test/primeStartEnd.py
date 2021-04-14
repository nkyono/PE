def calcDivisorsBool(target):
    if target < 2:
        return False
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                return False
            else:
                return False
    return True

def main():
    primes = []
    for x in range(1000000):
        if calcDivisorsBool(x):
            primes.append(x)
    primeStarts = {}
    primeEnds = {}
    for x in primes:
        strX = str(x)
        if int(strX[0]) in primeStarts:
            primeStarts[int(strX[0])] = primeStarts[int(strX[0])] + 1
        else:
            primeStarts[int(strX[0])] = 1
        if int(strX[-1]) in primeEnds:
            primeEnds[int(strX[-1])] = primeEnds[int(strX[-1])] + 1
        else:
            primeEnds[int(strX[-1])] = 1
    print("starts:")
    for x in primeStarts:
        print(x, primeStarts[x])
    print("\nends:")
    for x in primeEnds:
        print(x, primeEnds[x])
    return

if __name__ == '__main__':
    main()