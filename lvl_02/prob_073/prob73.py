'''
Consider the fraction, n/d, where n and d are positive integers. 
If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 3 fractions between 1/3 and 1/2.

How many fractions lie between 1/3 and 1/2 in the sorted set of reduced proper fractions for d ≤ 12,000?
'''

'''
farey sequence 
|Fn| = |Fn-1| + phi(n)
assumption(?) phi(n)/2 will be less than 1/2 and the other half will be greater than 1/2
since we are looking at 1/3 - 1/2 now have to determine, which of these half will be greater/less than 1/3
1/3 == 4000/12000
1 - 4000, 4000 - 6000
technically we could just test values range(4000,6001)/12000 and see which can't reduce
'''

# Python 3 program to calculate 
# Euler's Totient Function 
# using Euler's product formula 
def phi(n) : 
    result = n
    p = 2
    while p * p <= n : 
        if n % p == 0 : 
            while n % p == 0 : 
                n = n // p 
            result = result * (1.0 - (1.0 / float(p))) 
        p = p + 1
    # If n has a prime factor 
    # greater than sqrt(n) 
    # (There can be at-most one 
    # such prime factor) 
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n))) 
   
    return int(result) 

def sumFarey(lim):
    lengths = [0,2]
    for i in range(2,lim+1):
        lengths.append(lengths[i-1] + phi(i))
    
    return lengths

# farey neighbors next neighbor has denominator a+b
def firstNeighbor(a,b,lim):
    if a + b > lim:
        return 0
    return firstNeighbor(a, b + a, lim) + firstNeighbor(a + b, b, lim) + 1
    
def main():
    print(firstNeighbor(1,2,8))
    # print(farey([0,1],[1,1],2))
    # print(farey([0,1],[1,1],3))
    # print(farey([1,3],[1,2],12000))

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:",time.time()-start)