'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, 
it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''
# from wikipedia: abundant numbers
# limit is 20161 not 28123
def calcDivisors(target):
    divisors = []
    for i in range(1,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(target/i)

    sum = 0
    for x in divisors:
        sum = sum + x

    # print(divisors)
    return sum - target

# O(n^2)???
# really inefficient, must be a better way
# didn't break minute rule
def findTypes(limit):
    # find the number types up to 'limit' 
    numList = {}
    for x in range(1,limit):
        sum = calcDivisors(x)
        numType = ""
        if x > sum:
            numList[x] = "deficient"
        elif x < sum:
            numList[x] = "abundant"
        else:
            numList[x] = "perfect"
    
    checkList = {}
    for x in numList:
        for y in range(1,x):
            z = x-y
            if numList[z] == "abundant" and numList[y] == "abundant":
                checkList[x] = 1
                # print(z, y)
            y = x
    # print(checkList)
    sum = 0
    for x in range(limit):
        if x not in checkList:
            sum = sum + x
    print(sum)
            
def main():
    # print(calcDivisors(12))
    # print(calcDivisors(28))
    findTypes(28123)

if __name__ == '__main__':
    main()