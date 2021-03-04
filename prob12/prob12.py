'''
The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
36: 1,2,4,6,9,18,36
45: 1,3,5,9,15,45
55: 1,5,11,55
66: 1,2,3,6,11,22,33,66
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?
'''

# from problem 3, finding prime factorization
# using the Tau function
# https://mathschallenge.net/library/number/number_of_divisors
def findFactors(target):
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

    divisors = 1
    for x in factors.values():
        divisors = divisors * (x + 1)
    
    return divisors


# using this method to figure out how many divisors is too slow
def getNumDiv(tri):
    numDivs = 0
    for x in range(1, tri+1):
        if tri % x == 0:
            numDivs = numDivs + 1
    return numDivs 

def getTriNums():
    minDivs = 500
    currTri = 3
    numTris = 2
    while(True):
        divs = findFactors(currTri)
        if divs > minDivs:
            return currTri
        numTris = numTris + 1
        currTri = currTri + numTris

def main():
    print(getTriNums())
    # print(findFactors(28))

if __name__ == '__main__':
    main()