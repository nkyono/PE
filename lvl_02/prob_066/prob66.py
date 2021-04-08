'''
Consider quadratic Diophantine equations of the form:

x^2 – Dy^2 = 1

For example, when D=13, the minimal solution in x is 649^2 – 13×180^2 = 1.

It can be assumed that there are no solutions in positive integers when D is square.

By finding minimal solutions in x for D = {2, 3, 5, 6, 7}, we obtain the following:

3^2 – 2×2^2 = 1
2^2 – 3×1^2 = 1
9^2 – 5×4^2 = 1
5^2 – 6×2^2 = 1
8^2 – 7×3^2 = 1

Hence, by considering minimal solutions in x for D ≤ 7, the largest x is obtained when D=5.

Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
'''
# x^2 - D * y^2 == 1
# x^2 - 1 == D * y^2
# therefore the minimal solutions will be where y^2 is a factor of x^2-1.
# (x^2 - 1)/y^2 = D
# D * y^2 + 1 = x^2
# (x^2 - 1)/D = y^2 , find MIN x

import math

def testDioXY(x, y):
    res = float((x**2 - 1)/y**2)
    if res.is_integer():
        return int(res)
    else:
        return -1

def testDioDY(d, y):
    res = float(d * y**2 + 1.0)
    resSqrt = math.sqrt(res)
    if resSqrt.is_integer():
        return int(resSqrt)
    else:
        return -1

# how do I figure out the upper limit of x
def diophantine():
    minDio = {}
    for x in range(2,1000):
        if not math.sqrt(x).is_integer():
            for y in range(2,10000):
                d = testDioDY(x, y)
                if d != -1 and ((d not in minDio)):
                    minDio[d] = [x,y]

    maxX = d
    for d in minDio:
        print(d, minDio[d])
        if d > maxX:
            maxX = d
    print(maxX, minDio[maxX])
    return

def main():
    diophantine()
    return

if __name__ == '__main__':
    import time
    start = time.time()
    try:
        main()
    finally:
        print("time:",time.time()-start)