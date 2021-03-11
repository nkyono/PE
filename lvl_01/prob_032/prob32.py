'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once; 
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
'''

# 1,2,3,4,5,6,7,8,9 ... 9 digits
# 99^2 == 9801
# a multiplicand/multiplier can't be more than 4 digits
# must be a 3 digit x 2 digit = 4 digit or 4 digit x 1 digit = 4 digit
# 2 digit x 2 digit = 5 digit not possible as seen in 99^2 = 9801 therefore must be a 3x2=4 or 4x1=4
# 100^2 == 10000 so can't be 3,3
# can have 1,3 = 4 as seen in 9*99 = 8991
'''
1,2 6
1,3 5
1,4 4
2,2 5
2,3 4
2,4 3
3,3 3
'''

# forgot that it was 1-9 not 0-9
# added check to see if 0 was in set and it fixed result
def checkSet(x,y,z):
    s = set()
    for c in str(x):
        s.add(c)
    for c in str(y):
        s.add(c)
    for c in str(z):
        s.add(c)
    if str(0) in s:
        return False
    if len(s) == 9:
        return True
    return False

def findPandigital():
    prods = {}
    # first loop doesn't result in anything
    for x in range (1,10):
        for y in range(100,1000):
            if str(x) not in str(y):
                prod = x * y
                if len(str(prod)) + len(str(x)) + len(str(y)) < 10:
                    if checkSet(prod,x,y):
                        print(x,y,prod)
                        if prod in prods:
                            prods[prod] = prods[prod] + 1
                        else:
                            prods[prod] = 1
    for x in range (1,10):
        for y in range(1000,9999):
            if str(x) not in str(y):
                prod = x * y
                if len(str(prod)) + len(str(x)) + len(str(y)) < 10:
                    if checkSet(prod,x,y):
                        print(x,y,prod)
                        if prod in prods:
                            prods[prod] = prods[prod] + 1
                        else:
                            prods[prod] = 1
    for x in range (100,1000):
        for y in range(10,100):
            if str(x) not in str(y):
                prod = x * y
                if len(str(prod)) + len(str(x)) + len(str(y)) < 10:
                    if checkSet(prod,x,y):
                        print(x,y,prod)
                        if prod in prods:
                            prods[prod] = prods[prod] + 1
                        else:
                            prods[prod] = 1
    # print(prods)
    sum = 0
    for x in prods:
        sum = sum + x
    print(sum)

def main():
    findPandigital()

if __name__ == '__main__':
    main()