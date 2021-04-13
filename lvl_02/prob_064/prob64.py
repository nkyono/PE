'''
How many continued fractions for n <= 10000 have an odd period?
'''
import math
def conFracIrrIntArith(x):
    arr = []
    rem = math.floor(math.sqrt(x))
    arr.append(rem)
    if rem**2 == x:
        # x is a square root
        return arr
    q = 1
    p = 0
    a = rem
    while True:
        p = a * q - p
        q = int((x - p*p) / q)
        a = int((rem + p) / q)
        arr.append(a)
        if q == 1:
            break
    return arr

def main():
    odd = 0
    even = 0
    for x in range(1,10001):
        sqrtX = math.sqrt(x)
        if not sqrtX.is_integer():
            arr = conFracIrrIntArith(x)
            print(x, arr, len(arr)-1)
            if (len(arr) - 1) % 2 == 0:
                even = even + 1
            else:
                odd = odd + 1
    print(even, odd, odd/(even+odd))
    return

if __name__ == '__main__':
    main()