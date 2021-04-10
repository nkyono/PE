'''
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.
'''
# takes too long to iterate and calculate each value
# phi(n)/n == phi(rad(n))/rad(n)
# I think the algorithm for finding rad(n) is less efficient and just adds unnecessary time
# also due to the fact that the only time it was a permutation and lower ratio was when rad(n) = n

def phi(n): 
    result = n
    p = 2
    while p * p <= n : 
        if n % p == 0 : 
            while n % p == 0 : 
                n = n // p 
            result = result * (1.0 - (1.0 / float(p))) 
        p = p + 1
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n))) 
    return int(result) 

# answer is 8319823
# found by going backwards, took longer than acceptable though
# there must be some trick
# I thought that as n approached infinity, that the ratio would also approach a minimum
def main():
    minRatio = 1000
    minPhi = -1
    minIndex = -1
    phiDict = {}
    phiDict[1] = 1
    for x in range(10**7+1, -1, -1):
        '''
        if x % 2 == 0:
            k = x / 2
            phiDict[x] = phiDict[k]
            if k % 2 == 0:
                phiDict[x] = phiDict[x] * 2
            phiRes = phiDict[x]
        else:
        '''
        phiRes = phi(x)
        phiDict[x] = phiRes
        phiSorted = str(sorted(list(str(phiRes))))
        xSorted = str(sorted(list(str(x))))
        if phiRes != x and phiSorted == xSorted:
            currRatio = x/phiRes
            if minRatio > currRatio:
                minRatio = currRatio
                minPhi = phiRes
                minIndex = x
                print(x, phiRes, x/phiRes)

    return

if __name__ == '__main__':
    import time
    start = time.time()
    try:
        main()
    finally:
        print("time:",time.time()-start)