'''
Euler's Totient function, φ(n) [sometimes called the phi function], 
is used to determine the number of numbers less than n which are relatively prime to n. 
For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.

It can be seen that n=6 produces a maximum n/φ(n) for n ≤ 10.

Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
'''

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


def main():
    n = -1
    ans = 0.0
    for x in range(1,1000001):
        ratio = float(x/phi(x))
        if ratio > ans:
            n = x
            ans = ratio
        # print(x,x/phi(x))
    print(n, ans)
    return

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:",time.time()-start)