'''
The prime 41, can be written as the sum of six consecutive primes:

41 = 2 + 3 + 5 + 7 + 11 + 13
This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, 
contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
'''

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

def main():
    primes = []
    primesCheck = set()
    for x in range(2,1000000):
        if calcDivisors(x):
            primes.append(x)
            primesCheck.add(x)
    # primes = sorted(primes)
    # print(primes)

    ans = -1
    length = 0
    for lim in range(50, 1000):
        sum = 0
        for x in range(1000000):
            for y in range(x, x+lim):
                sum = sum + primes[y]
            if sum > 1000000:
                break
            if calcDivisors(sum):
                print(sum, lim)
                # we know we can search the next length of primes if one is found
                # if we find a chain of 100, we should just start looking at 101, etc.
                if lim > length:
                    length = lim
                    ans = sum
                    break
            sum = 0


if __name__ == '__main__':
    main()