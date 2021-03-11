'''
The number, 1406357289, 
is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order,
but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

d2d3d4=406 is divisible by 2
d3d4d5=063 is divisible by 3
d4d5d6=635 is divisible by 5
d5d6d7=357 is divisible by 7
d6d7d8=572 is divisible by 11
d7d8d9=728 is divisible by 13
d8d9d10=289 is divisible by 17
Find the sum of all 0 to 9 pandigital numbers with this property
'''
def checkPan(n):
    strN = str(n)
    check = set()
    if len(strN) > 10:
        return False
    for x in strN:
        check.add(x)
    if len(check) < 10:
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

def checkDiv(n):
    i = 0
    primes = [2,3,5,7,11,13,17]
    for x in range(1,8):
            sub = [n[x], n[x+1], n[x+2]]
            sub_sum = int(''.join(map(str, sub)))
            if sub_sum % primes[i] == 0:
                i = i + 1
            else:
                return False
    return True

def main():
    assert checkPan(1406357289) == True
    assert checkPan(14063357289) == False
    assert checkPan(1463357289) == False
    assert checkPan(146357289) == False
    assert checkDiv([1,4,0,6,3,5,7,2,8,9]) == True
    assert checkDiv([1,4,0,5,3,5,7,2,8,9]) == False

    pans = []
    elems = [0,1,2,3,4,5,6,7,8,9]
    last = []
    while elems != last:
        last = elems[:]
        getPermutation(elems)
        if checkDiv(elems):
            s = ''.join(map(str, elems))
            print(s)
            pans.append(s)
    
    sum = 0
    for x in pans:
        sum = sum + int(x)
    print(sum)

if __name__ == '__main__':
    main()