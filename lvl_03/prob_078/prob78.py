'''
Let p(n) represent the number of different ways in which n coins can be separated into piles. 
For example, five coins can be separated into piles in exactly seven different ways, so p(5)=7.

OOOOO
OOOO   O
OOO   OO
OOO   O   O
OO   OO   O
OO   O   O   O
O   O   O   O   O
Find the least value of n for which p(n) is divisible by one million.
'''

# https://en.wikipedia.org/wiki/Partition
# https://en.wikipedia.org/wiki/Partition_function_(number_theory)
# p(n) also includes n itself so we need p(n)-1 I think
import math

# up to 10000, we would only need to keep less than the partitions for n < 100
# storing all partitions, we run into what I suspect is an overflow error
# try 1
# this try actually worked, I had initially tried to do this by converting to a string then taking the last few digits
# instead using modulo 1000000 made this function work...
# quite irritating that I forgot mod(1000000) would have worked b/c everything else is the same from when I first tried
def calcWaysI():
    partN = [1,1]
    x = 2
    while True:
        sum = 0
        kLow = int((-1) * ((math.sqrt(24*x + 1) - 1) / 6))
        kHigh = int((math.sqrt(24*x + 1) + 1) / 6)
        for k in range(kLow, kHigh+1):
            if k != 0:
                check = int(x - k*(3*k - 1) / 2)
                if check >= 0:
                    if x < 200:
                        sum = sum + ((-1)**(k+1) * partN[int(x - k * (3 * k - 1) / 2)])
                    else:
                        sum = sum + ((-1)**(k+1)*partN[int(x - k * (3 * k - 1) / 2)])%1000000
        if sum % 1000000 == 0 and sum > 0:
            print(x,sum)
            break
        # print(x,kHigh,sum)
        partN.append(sum)
        x = x + 1
    '''
    for x in range(len(partN)):
        print(x, partN[x])
    '''

def calcDivisorsListSelf(target):
    if target < 0:
        return []
    if target == 1:
        return [1]
    divisors = [1, target]
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(target/i)
    return divisors

def divisorFunc(n, k):
    divs = calcDivisorsListSelf(n)
    total = 0
    for x in divs:
        total = total + x**k
    return int(total)

# this second way uses a different way to compute p
# issue is it requires all P(0)...P(n-1) to compute P(n), this leads to issues with trying to use
# modulo to truncate the values
# other than that this function is still quite good I think, just not necessary/the right application
def calcWaysII():
    partN = [1,1]
    divs = {}
    x = 2
    while x < 100:
        sum = 0
        for k in range(x):
            div = 0
            if x-k in divs:
                div = divs[x-k]
            else:
                div = divisorFunc(x-k,1)
                divs[x-k] = div
            sum = sum + (div * partN[k])
        sum = sum / x
        partN.append(int(sum))
        x = x + 1
    while True:
        sum = 0
        for k in range(x):
            div = 0
            if x-k in divs:
                div = divs[x-k]
            else:
                div = divisorFunc(x-k,1)
                divs[x-k] = div
            sum = sum + (div * partN[k])
        sum = sum / x
        # print(x,sum)
        partN.append(sum)
        if sum % 1000000 == 0 and sum > 0:
            print(x,sum)
            break
        x = x + 1
    return partN

def test():
    #calcWaysII()
    calcWaysI()

if __name__ == '__main__':
    import time
    start = time.time()
    test()
    print("time:",time.time()-start)