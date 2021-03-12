'''
By replacing the 1st digit of the 2-digit number *3, 
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers, 
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, 
being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, 
by replacing part of the number (not necessarily adjacent digits) with the same digit, 
is part of an eight prime value family.
'''

# looking for primes, therefor last digit can't be 0,2,4,5,6,8 ... can only be 1,3,7
# off of this, I hypothesize that we can check x-digit nums even with 1,3,7 only
# off of the previous line, we can deduce that the singles column can never be the replaced number 
# for each possibility, we have 10 (0,1,2,...,9) different numbers

# we can do iteration and checking in a more brute force kind of way
# or we can pattern match (maybe?) after creating the primes


def calcDivisors(target):
    if target < 0:
        return False
    divisors = []
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
                return False
            else:
                divisors.append(i)
                divisors.append(target/i)
                return False
    return True

def createPrimes(low, high):
    primes = set()
    for x in range(low, high):
        if calcDivisors(x):
            primes.add(x)
    primes = sorted(primes)
    return primes

def generateAllBinaryStrings(n, arr, i, res):  
    if i == n:
        s = int(''.join(map(str, arr)))
        res.append(s)  
        return

    arr[i] = 0
    generateAllBinaryStrings(n, arr, i + 1, res)  

    arr[i] = 1
    generateAllBinaryStrings(n, arr, i + 1, res)  

def makeBins():
    n = 6
    arr = [None] * n 
    res = []
    generateAllBinaryStrings(n, arr, 0, res)

    res = sorted(res)
    for x in range(len(res)-1, -1, -1):
        if res[x] < 100000:
            res.remove(res[x])
    return res

def checkOff(primes, bins):
    count = 0
    for prime in primes:
        for off in bins:
            count = 1
            for x in range(1,10):
                offset = off * x
                newPrime = prime + offset
                if newPrime in primes:
                    count = count + 1
            if count >= 8:
                print("Maybe:",prime)
                for x in range(1,10):
                    offset = off * x
                    newPrime = prime + offset
                    if newPrime in primes:
                        print(prime, newPrime, offset)
                return

def trimPrimes(primes,lim):
    trimmed = []
    for x in primes:
        strX = str(x)
        for y in range(10):
            i = 0
            for z in strX:
                if z == str(y):
                    i = i + 1
            if i >= lim:
                trimmed.append(x)
    return trimmed

def main():
    primes = createPrimes(100000, 1000000)
    # fail(primes)
    print(len(primes))
    lim = 3
    # nums = counting(primes, lim)
    trimmed = trimPrimes(primes, lim)
    print(len(trimmed))
    '''
    for x in nums[lim]:
        print(x)
    '''
    # createGraph(nums[lim], lim)
    res = makeBins()
    checkOff(trimmed, res)



if __name__ == '__main__':
    main()

'''
create a graph
an edge is the difference between two digits where: 
diff(1234, 2345) = |1-2|+|2-3|+|3-4|+|4-5|
limit it to only creating an edge if it's less than 'lim' (ie. our arbitrary search space)
go through nodes and find shortest paths?
'''

'''
456448
556558
656668

should result in a binary # if subtract each digit from another (similar to diff above)
100110
'''

''' 
solved, probably really inefficiently
used offsets + primes to check if (8) other primes existed
'''