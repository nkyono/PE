def getFactors(target):
    factors = set()
    if target == 1:
        factors.add(1)
        return factors
    div = 2
    while(target != 0):
        if(target % div != 0):
            div = div + 1
        else:
            fact = target
            target = target/div
            factors.add(div)
            if(target==1):
                factors.add(1)
                break
    return factors

def getFactorsPowers(target):
    factors = {}
    if target == 1:
        return factors
    div = 2
    while(target != 0):
        if(target % div != 0):
            div = div + 1
        else:
            fact = target
            target = target/div
            if div in factors:
                factors[div] = factors[div] + 1
            else:
                factors[div] = 1
            if(target==1):
                break
    return factors