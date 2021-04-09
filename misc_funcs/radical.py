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

def rad(num):
    prod = 1
    factors = getFactors(num)
    for y in factors:
        prod = prod * y
    # print(num, prod)
    return prod

def main():
    assert rad(19) == 19
    assert rad(504) == 42
    assert rad(1) == 1
    assert rad(20) == 10

if __name__ == '__main__':
    main()