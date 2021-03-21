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

# returns list of divisors
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