'''
A googol (10100) is a massive number: one followed by one-hundred zeros; 
100100 is almost unimaginably large: one followed by two-hundred zeros. 
Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
'''
import time

def calcDigSum(n):
    strN = str(n)
    sum = 0
    for c in strN:
        sum = sum + int(c)
    return sum

def maxSumBranchless(lim):
    res = -1
    for a in range(lim):
        for b in range(lim):
            sum = calcDigSum(a**b)
            res = (sum * (sum > res)) + (res * (res >= sum))
    print(res)
    return res

def maxSum(lim):
    res = -1
    for a in range(lim):
        for b in range(lim):
            sum = calcDigSum(a**b)
            if sum > res:
                res = sum
    print(res)
    return res


if __name__ == '__main__':
    start = time.time()
    maxSum(100)
    print("time regular:", time.time()-start)
    start = time.time()
    maxSumBranchless(100)
    print("time branchless:", time.time()-start)