# untested, might need touch up, but should work
# returns bool of whether or not there is a divisor
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

# returns list of divisors (not including 1 and self)
def calcDivisorsList(target):
    if target < 0:
        return []
    divisors = []
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(target/i)
    return divisors

# returns divs including 1 and self
def calcDivisorsListSelf(target):
    if target < 0:
        return []
    divisors = [1, target]
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(target/i)
    return divisors

def divisorFunc(n, k):
    divs = calcDivisorsListSelf(n)
    total = 0
    for x in divs:
        total = total + x**k
    return int(total)

def main():
    assert divisorFunc(140,1) == 336
    assert divisorFunc(140,2) == 27300
    assert divisorFunc(140,3) == 3164112
    assert divisorFunc(140,0) == 12
    return

if __name__ == '__main__':
    main()