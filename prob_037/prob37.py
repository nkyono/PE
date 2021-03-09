'''
The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
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

# if a number contains an 0,1,2,4,6,8,9 
def iterPrimes():
    primes = []

    # range b/c singles don't count as truncatable primes
    # 1000000 was just an arbitrary range, happened to have the 11 primes
    for x in range(10,1000000):
        if calcDivisors(x):
            primes.append(x)
            # print("added: ", x)
            strX = str(x)
            if '0' not in strX:
                left = 0
                while left < len(strX):
                    if strX[left:] == '1' or not calcDivisors(int(strX[left:])):
                        # print("removed: ", x)
                        primes.remove(x)
                        break
                    left = left + 1

                right = len(strX) - 1
                while left == len(strX) and right > 0:
                    if strX[:right] == '1' or not calcDivisors(int(strX[:right])):
                        # print("removed: ", x)
                        primes.remove(x)
                        break
                    right = right - 1
            else:
                primes.remove(x)

    print(primes)
    print(len(primes))

    sum = 0
    for x in primes:
        sum = sum + x
    print(sum)

def main():
    iterPrimes()

if __name__ == '__main__':
    main()