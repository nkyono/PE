'''
The number, 197, is called a circular prime because all rotations of the digits: 
197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?
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

def main():
    circ_primes = []
    for x in range(2,1000000):
        if calcDivisors(x):
            circ_primes.append(x)
            strX = str(x)
            for y in range(len(strX)):
                if not calcDivisors(int(strX[y:]+strX[:y])):
                    circ_primes.remove(x)
                    break

    print(circ_primes)
    print(len(circ_primes))

if __name__ == '__main__':
    main()