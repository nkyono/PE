'''
It is well known that if the square root of a natural number is not an integer, then it is irrational. 
The decimal expansion of such square roots is infinite without any repeating pattern at all.

The square root of two is 1.41421356237309504880..., and the digital sum of the first one hundred decimal digits is 475.

For the first one hundred natural numbers, find the total of the digital sums of the first one hundred decimal digits for all the irrational square roots.

'''
import math

def sqrtLongDiv(num, lim):
    decimalPlace = 0
    res = ""
    numStr = str(num)
    currDividend = ""
    front = -1
    back = -1
    if len(numStr) == 1 or len(numStr)%2 != 0:
        front = 0
        back = 1
        currDividend = numStr
    else:
        front = 0
        back = 2
        currDividend = numStr[front: back]
    divisor = ""

    # finds first digit
    currDivisor = 1
    while currDivisor**2 <= int(currDividend):
        currDivisor = currDivisor + 1
    currDivisor = currDivisor - 1
    res = str(currDivisor)
    remainder = int(currDividend) - currDivisor**2
    
    # find rest of the digits
    while len(res[decimalPlace:]) < lim and remainder != 0:
        currDividend = str(remainder)
        currDivisor = str(int(res) * 2)
        i = 0
        if back + 2 > len(numStr):
            if decimalPlace == 0:
                decimalPlace = len(res)
            numStr = numStr + "00"
        front = back
        back = back + 2
        currDividend = currDividend + numStr[front:back]
        while int(currDivisor + str(i)) * i <= int(currDividend):
            i = i + 1
        i = i - 1
        remainder = int(currDividend) - int(currDivisor + str(i)) * i
        # print(res, remainder, currDividend, currDivisor)
        res = res + str(i)
    if decimalPlace != 0:
        res = res[:decimalPlace] + "." + res[decimalPlace:]
    # print(res)
    return res

def main():
    totalSum = 0
    for x in range(101):
        res = sqrtLongDiv(x, 100)
        if "." in res:
            sumPlaces = 0
            decimalPlace = res.find(".")
            # print(res)
            # print(res[decimalPlace+1:])
            # weird because it includes things before decimal in sum
            for c in res[:decimalPlace]+res[decimalPlace+1:101]:
                sumPlaces = sumPlaces + int(c)
            print(x, sumPlaces)
            totalSum = totalSum + sumPlaces
    print(totalSum)
    return

if __name__ == '__main__':
    main()