'''
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, 
it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d ≤ 1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.
'''

# let's shrink search space
# we want left of 3/7
# 3/7 ~ 428571/999999 ~ 0.42857142857
# 428570/999999 ~ 0.42857042857
# 428571/1000000 == 0.428571
# look to left of this
# 400000/1000000 == .4 == 2/5
# look to right of this

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

def inefficientMethod():
    fracs = {}
    for y in range(1000000,0,-1):
        for x in range(428570, 0, -1):
            frac = x/y
            if frac < (3/7) and frac > (2/5):
                if frac in fracs:
                    fracs[frac].append([x,y])
                else:
                    fracs[frac] = [[x,y]]
            else:
                break
    guess = 0
    frac = []
    for x in fracs:
        if guess < x:
            guess = x
            frac = fracs[x]
    print(guess, frac)
    print(getFactors(frac[0][0]))
    print(getFactors(frac[0][1]))

# trick in this one was to use farey sequence
# reminds me of a binary search kind of
def farey():
    aNum = 2
    aDem = 5
    while aDem <= 1000000:
        aNum = aNum + 3
        aDem = aDem + 7
    aNum = aNum - 3
    aDem = aDem - 7
    print(aNum,aDem,aNum/aDem)

def main():
    # inefficientMethod()
    farey()

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:",time.time()-start)