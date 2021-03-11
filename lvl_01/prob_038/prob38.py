'''
Take the number 192 and multiply it by each of 1, 2, and 3:

192 × 1 = 192
192 × 2 = 384
192 × 3 = 576
By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number that can be formed 
as the concatenated product of an integer with (1,2, ... , n) where n > 1?
'''

def checkPan(n):
    strN = str(n)
    if len(strN) > 9 or '0' in strN:
        return False
    else:
        check = set()
        for x in strN:
            check.add(x)
        if len(check) < 9:
            return False
    return True

# if min n is 2, then max value is a 4 digit # that when multiplied by 2 results in a 5 digit # resulting in 9 digits
def iter():
    for x in range(10000):
        for i in range(2,10):
            prod = ""
            for k in range(1,i+1):
                prod = prod + str(k*x)
            if checkPan(prod):
                print(x, prod)


def main():
    iter()
    '''
    print(checkPan(918273645))
    print(checkPan(192384576))
    print(checkPan(192384576234))
    print(checkPan(19234576))
    print(checkPan(192384570))
    '''


if __name__ == '__main__':
    main()