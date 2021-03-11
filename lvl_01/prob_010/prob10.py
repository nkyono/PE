'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# brute force, need to come back after problem 7
def calcDivisors(target):
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

def sumOfPrimes(limit):
    sum = 0
    for x in range(2, limit):
        if calcDivisors(x):
            sum = sum + x
    print("sum: ", sum)

def main():
    sumOfPrimes(2000000)

if __name__ == '__main__':
    main()