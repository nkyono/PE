'''
Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
'''

# upper right + 2*layer
# 3 is first layer, 13 is second layer
# 13 = 9 + 4, next would be 31 = 25+6
# where n is diagonal length, 2n+1 = side

def calcDiags(n):
    diag = int((n - 1) / 2)
    sum = 1
    last = 1
    for x in range(1,diag+1):
        curr_side = 2*x
        last = last + 2*x
        sum = sum + last
        # print(last)
        for y in range(3):
            last = last + curr_side
            sum = sum + last
            # print(last)
    print(sum)

def main():
    calcDiags(1001)

if __name__ == '__main__':
    main()