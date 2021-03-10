'''
It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?
'''
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

def findPrimes():
    primes = set()
    for n in range(1,10000):
        if calcDivisors(n):
            # print("prime: ", n)
            primes.add(n)
        else:
            if n % 2 != 0:
                # print("composite: ", n)
                found = False
                for x in range(int(n**.5)):
                    # print("Trying:", n - (2 * (x ** 2)), " for ", n)
                    if n - (2 * (x ** 2)) in primes:
                        # print("Found:", n - (2 * (x ** 2)), " for ", n)
                        found = True
                if not found:
                    print("Nothing found for:", n)

def main():
    findPrimes()

if __name__ == '__main__':
    main()