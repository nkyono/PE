'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
'''
def calcDivisors(target):
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

def checkPan(n):
    strN = str(n)
    if '0' in strN:
        return False
    else:
        check = set()
        for x in strN:
            check.add(x)
        for x in range(1,len(strN)+1):
            if str(x) not in check:
                return False
    return True

def getPermutation(elems):
    if len(elems) < 2:
        return elems
    i = len(elems) - 2
    while i >= 0 and elems[i] > elems[i+1]:
        i = i - 1
    if i == -1:
        return elems
    k = len(elems) - 1
    while elems[i] > elems[k]:
        k = k - 1

    temp = elems[i]
    elems[i] = elems[k]
    elems[k] = temp

    low = i + 1
    high = len(elems) - 1
    while low < high:
        temp = elems[low]
        elems[low] = elems[high]
        elems[high] = temp
        low = low + 1
        high = high - 1
    return elems

# we can check 9! + 8! + 7! + 6! + 5! + 4! + 3! + 2! + 1! = 409113 
def main():
    elems = [1,2,3,4,5,6,7,8,9]
    max = -1
    for x in range(9,1,-1):
        last = []
        while elems != last:
            last = elems[:]
            getPermutation(elems)
            s = ''.join(map(str, elems))
            # print(s)
            if calcDivisors(int(s)):
                print(s)
                if int(s) > max:
                    max = int(s)
        elems.remove(x)
        elems = sorted(elems)
    print(max)
    

if __name__ == '__main__':
    main()