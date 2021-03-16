'''
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than the denominator?
'''

import fractions
# long division?, gives different expansions
def calcIterLong(lim):
    exp = 1
    strRes = "1"
    remain = 100
    num = 0
    denom = 0
    for x in range(lim):
        curr = str(int(strRes) * 2)
        i = 1
        print("Exp: ", x)
        print("Numerator: ", remain)
        num = remain
        while(i < 10):
            prod = int(curr+str(i)) * i
            if prod < remain:
                i = i + 1
            else:
                i = i - 1
                prod = int(curr+str(i)) * i
                print("Denominator: ", prod)
                denom = prod
                remain = int(str(remain - prod) + "00")
                strRes = strRes + str(i)
                break
        i = 1
        print("Decimal: ", num/denom)
        print("Fraction: ", float.as_integer_ratio(num/denom))
        print("---------")

# recursive hits depth limit
def recurv(n):
    if (n == 0):
        return (1.0/(2 + 1/2))
    else:
        return (1.0/(2 + recurv(n-1)))

# noticed pattern of (n-1)*2 + (n-2)
def calcIterFracs(lim):
    total = 0
    res = 1.0
    base = 1.0/(2 + 1/2)
    fracs = {}
    fracs[1] = [3,2]
    fracs[2] = [7,5]
    for x in range(3,lim):
        fracs[x] = [(fracs[x-1][0] * 2 + fracs[x-2][0]), (fracs[x-1][1] * 2 + fracs[x-2][1])]
        if len(str(fracs[x][0])) > len(str(fracs[x][1])):
            total = total + 1
        
    for x in fracs:
        print("Expansion:",x)
        print("Fraction:",fracs[x])

    print("total:", total)
            
def test():
    # calcIterLong(10)
    calcIterFracs(1000)

if __name__ == '__main__':
    import time
    start = time.time()
    test()
    print("time recursive:",time.time()-start)