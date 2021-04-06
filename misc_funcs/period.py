def phi(n): 
    result = n
    p = 2
    while p * p <= n : 
        if n % p == 0 : 
            while n % p == 0 : 
                n = n // p 
            result = result * (1.0 - (1.0 / float(p))) 
        p = p + 1
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n))) 
    return int(result) 

def calcDivisorsList(target):
    if target < 0:
        return []
    divisors = []
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(target/i)
    return divisors

# the period is always a factor of the totient of the denominator
# such that 10^k == 1 % denominator
# with 10**x % denominator == 1, we get a overflow error
def calcPeriodFrac(numerator, denominator):
    totient = phi(denominator)
    divs = calcDivisorsList(totient)
    print(divs)
    for x in divs:
        if 10**x % denominator == 1:
            print("period is", x)
            return x
    print("something went wrong in calculating the period...")
    return 0

# NOTE: not implemented for things like square roots
# calculating period using long division
# places will probably be used as a limiter
def calcPeriodLongDiv(numerator, denominator, places):
    res = ""
    decimal = False
    if numerator < denominator:
        decimal = True
        res = "0."
    numStr = str(numerator)
    numIndex = 0
    decimalPlaces = 0
    remainder = int(numStr[numIndex])
    remainders = set()
    while(remainder != 0 and decimalPlaces < places):
        if remainder >= denominator:
            if decimal:
                if remainder in remainders:
                    return decimalPlaces
                else:
                    remainders.add(remainder)
            i = 0
            while (i < 10):
                i = i + 1
                if i * denominator > remainder:
                    i = i - 1
                    break
            res = res + str(i)
            if decimal:
                decimalPlaces = decimalPlaces + 1
            remainder = int(str(remainder - i * denominator))
        else:
            if res != "" and res != "0.":
                res = res + "0"
                if decimal:
                    decimalPlaces = decimalPlaces + 1
        
        if remainder == 0:
            break
        numIndex = numIndex + 1
        if numIndex == len(numStr):
            if "." not in res:
                res = res + "."
                decimal = True
            numStr = numStr + "0"
            
        remainder = int(str(remainder) + numStr[numIndex])
    print(res)
    return decimal

def main():
    # calcPeriodFrac(3923, 6173)
    assert calcPeriodLongDiv(3923, 6173, 6173) == 3086
    assert calcPeriodLongDiv(10, 3, 100) == 1
    assert calcPeriodLongDiv(119, 13 , 10) == 6
    assert calcPeriodLongDiv(1, 7 , 10) == 6
    assert calcPeriodLongDiv(1, 37 , 10) == 3
    return

if __name__ == '__main__':
    main()