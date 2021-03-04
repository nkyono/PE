'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. 
The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

def findDivisors(target):
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
    
    return sum - target

def createSumTable():
    total = 0
    sums = {}
    for x in range(1, 10001):
        sum = findDivisors(x)
        sums[x] = sum
        if sum in sums and x == sums[sum] and sum != x:
            print("pair: ", x, " ", sum)
            total = total + x + sum
            
    return total

def main():
    print(createSumTable())
    print(findDivisors(6368))
    print(findDivisors(6232))

if __name__ == '__main__':
    main()