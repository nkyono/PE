'''
Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, 
but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, 
a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, 
a square spiral with side length 9 will be formed. 
If this process is continued, 
what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?


'''
# from prob 28, pattern is different, but diagnols are the same
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

def calcDiags():
    numDiags = 1
    primeDiags = 0
    curr_side = 0
    sum = 1
    last = 1
    x = 1
    while primeDiags*1.0/numDiags == 0 or primeDiags*1.0/numDiags > .1:
        curr_side = 2*x
        last = last + 2*x
        numDiags = numDiags + 1
        if calcDivisors(last):
            primeDiags = primeDiags + 1
        for y in range(3):
            last = last + curr_side
            numDiags = numDiags + 1
            if calcDivisors(last):
                primeDiags = primeDiags + 1
        x = x + 1

    print(primeDiags, numDiags, primeDiags*1.0/numDiags)
    print(curr_side + 1)

def main():
    calcDiags()

if __name__ == '__main__':
    main()