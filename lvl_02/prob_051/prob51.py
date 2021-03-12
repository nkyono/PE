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

def counting(primes, lim):
    num_nums = {}
    for x in primes:
        strX = str(x)
        for y in range(10):
            i = 0
            for z in strX:
                if z == str(y):
                    i = i + 1
            if i == lim:
                if i in num_nums:
                    num_nums[i].append(x)
                else:
                    num_nums[i] = [x]
    return num_nums

def fail(primes):
    num_nums = counting(primes)
    indexes = {}
    for x in num_nums:
        for z in range(6):
            nums = 0
            appeared = False
            for y in range(10):
                a = 0
                for i in num_nums[x]:
                    if str(i)[z] == str(y):
                        appeared = True
                        a = a + 1
                if z in indexes:
                    indexes[z].append([a,y])
                else:
                    indexes[z] = [[a,y]]
                if appeared:
                    nums = nums + 1
                    appeared = False
    reduced = set()
    for x in num_nums:
        for i in num_nums[x]:
            for y in range(10):
                strX = str(i)
                if strX[1] == strX[2] == strX[4]:
                    reduced.add(i)
    reduced = sorted(reduced)
    for i in reduced:
        print(i)
    '''
    for x in indexes:
        indexes[x] = sorted(indexes[x])
        print(x, indexes[x])
    '''

def difference(x,y):
    strX = str(x)
    strY = str(y)
    res = str(abs(int(strX[0]) - int(strY[0]))) + str(abs(int(strX[1]) - int(strY[1]))) + str(abs(int(strX[2]) - int(strY[2]))) + str(abs(int(strX[3]) - int(strY[3]))) + str(abs(int(strX[4]) - int(strY[4]))) + str(abs(int(strX[5]) - int(strY[5]))) 
    res_set = set(res)
    if (res_set == {'1'} or res_set == {'0'} or res_set == {'0','1'}):
        return int(res)
    return -1

def createGraph(primes, lim):
    edges = {}
    numEdges = 0
    for x in primes:
        for y in primes:
            if x != y and abs(x-y)<111111 and str(x)[5] == str(y)[5] and str(x)[0] != str(y)[0]:
                diff = difference(x,y)
                if diff > 0:
                    numEdges = numEdges + 1
                    if diff in edges:
                        edges[diff].append([x,y])
                    else:
                        edges[diff] = [[x,y]]

    for x in edges:
        print(x, edges[x])

    print("edges:", numEdges)
    return edges


def main():
    primes = createPrimes(100000, 1000000)
    # fail(primes)

    lim = 3
    nums = counting(primes, lim)
    '''
    for x in nums[lim]:
        print(x)
    '''
    createGraph(nums[lim], lim)



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