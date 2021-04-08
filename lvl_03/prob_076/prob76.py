'''
It is possible to write five as a sum in exactly six different ways:

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

How many different ways can one hundred be written as a sum of at least two positive integers?
'''
# https://en.wikipedia.org/wiki/Partition
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
# p(n) also includes n itself so we need p(n)-1 I think
import math

def calcWays(lim):
    partN = [1,1]
    for x in range(2,lim):
        sum = 0
        kLow = int((-1) * ((math.sqrt(24*x + 1) - 1) / 6))
        kHigh = int((math.sqrt(24*x + 1) + 1) / 6)
        for k in range(kLow, kHigh+1):
            if k != 0:
                check = int(x - k*(3*k - 1) / 2)
                if check >= 0:
                    sum = sum + ((-1)**(k+1) * partN[int(x - k * (3 * k - 1) / 2)])
        partN.append(int(sum))
    for x in range(len(partN)):
        print(x, partN[x]-1)

def test():
    calcWays(101)

if __name__ == '__main__':
    import time
    start = time.time()
    test()
    print("time:",time.time()-start)