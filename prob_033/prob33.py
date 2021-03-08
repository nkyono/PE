'''
The fraction 49/98 is a curious fraction, 
as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, 
less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.
'''

# got carried away, don't need/didn't use factors/gcd 
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

def gcd(a,b):
    greatest = 1
    for x in a:
        if x in b and x > greatest:
            greatest = x
    return greatest

def checkCommon(a,b):
    for x in str(a):
        for y in str(b):
            if x == y and x != '0':
                return True
    return False

# all logic is here
def checkCurious(a,b):
    reg = a/b

    strA = str(a)
    strB = str(b)
    for x in range(len(strA)):
        for y in range(len(strB)):
            if strA[x] != '0' and strB[y] != '0' and strA[1-x] == strB[1-y] and strA[1-x] != '0':
                new = int(strA[x])/int(strB[y])
                if reg == new:
                    print(a,"/", b, " | ", strA[x], "/", strB[y])
                    return {int(strA[x]), int(strB[y])}


def findCurious():
    for a in range(10,100):
        for b in range(a+1, 100):
            '''
            a_fact = getFactors(a)
            b_fact = getFactors(b)
            greatest = gcd(a_fact, b_fact)
            if greatest > 1:
                print(a, b, a/b, (a/greatest)/(b/greatest))
                if checkCommon(a,b):
                    checkCurious(a,b,greatest)
            '''
            checkCurious(a,b)


def main():
    findCurious()

if __name__ == '__main__':
    main()