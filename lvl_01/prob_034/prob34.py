'''
145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Note: As 1! = 1 and 2! = 2 are not sums they are not included.
'''
# I think there is a limit below 2500000
# 9! = 362880
# 9,999,999 = 7 * 9! = 2540160 therefore no way for sum to catch up

def fact(n):
    sum = 1
    while n > 0:
        sum = sum * n
        n = n - 1
    return sum

def iter():
    total = 0
    for x in range(3, 2500000):
        strX = str(x)
        sum = 0
        for y in strX:
            sum = sum + fact(int(y))
        if sum == x:
            print(x, sum)
            total = total + sum
    print(total)

def main():
    iter()

if __name__ == '__main__':
    main()