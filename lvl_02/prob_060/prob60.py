'''
The primes 3, 7, 109, and 673, are quite remarkable. 
By taking any two primes and concatenating them in any order the result will always be prime. 
For example, taking 7 and 109, both 7109 and 1097 are prime. 
The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
'''
def calcDivisorsBool(target):
    if target < 2:
        return False
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                return False
            else:
                return False
    return True

def testPrime(p, primes):
    strP = str(p)
    if len(strP) < 2:
        return []
    pairs = []
    for x in range(1,len(strP)):
        a = int(strP[:x])
        b = int(strP[x:])
        if strP[x] != "0":
            if a in primes and b in primes:
                pairs.append([a,b])
    return pairs

def checkRelations(curr, arr, primes):
    if len(arr) == 5:
        # print(arr)
        return True

    for x in primes[curr]:
        if x not in arr:
            arr.append(x)
            for y in arr:
                if x not in primes[y] and x != y:
                    arr.remove(x)
                    break
            if x in arr:
                if checkRelations(x, arr, primes):
                    return True
                else:
                    arr.remove(x)
    return False

# issue: we can figure out 4 primes with this method but not 5
# for this method to work we need to compute primes to a super high degree
# I think I need to reverse it and calc a smaller number of primes, concat and check if primes
def tryTwo():
    primes = {}
    for x in range(2,1000000):
        if calcDivisorsBool(x) and x not in primes:
            res = testPrime(x, primes)
            if res != []:
                for r in res:
                    rev = int(str(r[1]) + str(r[0]))
                    if calcDivisorsBool(rev):
                        if x in primes:
                            primes[x].append([r[0], r[1]])
                        else:
                            primes[x] = [[r[0], r[1]]]
                        if rev in primes:
                            primes[rev].append([r[1], r[0]])
                        else:
                            primes[rev] = [[r[1], r[0]]]
            else:
                primes[x] = []
    primeCounts = {}
    for x in primes:
        for y in primes[x]:
            '''
            if y[0] in primeCounts:
                primeCounts[y[0]].append(y[1])
            else:
                primeCounts[y[0]] = [y[1]]
            if y[1] in primeCounts:
                primeCounts[y[1]].append(y[0])
            else:
                primeCounts[y[1]] = [y[0]]
            '''
            if y[0] not in primeCounts:
                primeCounts[y[0]] = set()
            primeCounts[y[0]].add(y[1])
            if y[1] not in primeCounts:
                primeCounts[y[1]] = set()
            primeCounts[y[1]].add(y[0])


    minSum = -1
    for x in primeCounts:
        if len(primeCounts[x]) >= 4:
            arr = [x]
            if checkRelations(x, arr, primeCounts):
                sum = 0
                for z in arr:
                    sum = sum + z
                print(sum, arr)
                if minSum > sum or minSum == -1:
                    minSum = sum
            # print(x, primeCounts[x])
    print(minSum)

def main():
    tryTwo()
    return

if __name__ == '__main__':
    import time
    start = time.time()
    try:
        main()
    finally:
        print("time:", time.time()-start)