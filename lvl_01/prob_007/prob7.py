'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?
'''
# prime number theorem?, prime counting function?
# there's an extremely inefficient and slow algorithm of iterating, checking, and counting numbers/primes

# solution found using a more efficient divisor function
def calcDivisors(target):
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                return False
            else:
                return False

    return True

def findPrime():
    num = 0
    i = 1
    while num < 10001:
        i = i + 1
        if calcDivisors(i):
            num = num + 1
            print(i)
    print(i)

def main():
    findPrime()

if __name__ == '__main__':
    main()