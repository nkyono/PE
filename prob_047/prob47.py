'''
The first two consecutive numbers to have two distinct prime factors are:

14 = 2 × 7
15 = 3 × 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2² × 7 × 23
645 = 3 × 5 × 43
646 = 2 × 17 × 19.

Find the first four consecutive integers to have four distinct prime factors each. 
What is the first of these numbers?
'''

# this one might have taken too long

def getFactors(target):
    # note: this function doesn't work for 1, loops infinitely
    div = 2
    fact = 0
    factors = {}
    while(target != 0):
        if(target % div != 0):
            div = div + 1
        else:
            fact = target
            target = target/div
            if div in factors:
                factors[div] = factors[div]+1
            else:
                factors[div] = 1
            if(target==1):
                break
    return factors

def distinct(target, n):
    facts = getFactors(target)
    # print(divs)
    if len(facts) == n:
        # print(target, facts)
        return True
    return False

# increased i to start with b/c of other runs
# maybe I could have changed search strategy, maybe i + 3 then if distinct(i,4) found then search around
# doesnt really change complexity thou
def iter(lim):
    n = 0
    i = 100000
    while(True):
        if distinct(i, lim):
            n = n + 1
        else:
            n = 0
        i = i + 1
        if n == lim:
            print(i-lim)
            return

def main():
    assert distinct(14, 2) == True
    assert distinct(15, 2) == True
    assert distinct(644, 3) == True
    assert distinct(645, 3) == True
    assert distinct(646, 3) == True
    assert distinct(8, 2) == False

    iter(4)


if __name__ == '__main__':
    main()