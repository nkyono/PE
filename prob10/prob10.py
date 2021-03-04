'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# brute force, need to come back after problem 7
def isPrime(num):
    for x in range(2, int(num/2)+1):
        if num%x == 0:
            return False
    return True

def sumOfPrimes(limit):
    sum = 0
    for x in range(2, limit):
        if isPrime(x):
            sum = sum + x
    print("sum: ", sum)

def main():
    sumOfPrimes(2000000)

if __name__ == '__main__':
    main()