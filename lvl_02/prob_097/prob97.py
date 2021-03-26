'''
The first known prime found to exceed one million digits was discovered in 1999, and is a Mersenne prime of the form 2^6972593−1; 
it contains exactly 2,098,960 digits. Subsequently other Mersenne primes, of the form 2^p−1, have been found which contain more digits.

However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×2^7830457+1.

Find the last ten digits of this prime number.
'''
# you don't need to keep all the digits

def main():
    num = 1
    for x in range(1,7830457+1):
        num = num * 2
        strNum = str(num)[-10:]
        num = int(strNum)
        # print(x, num)
    num = num * 28433 + 1
    strNum = str(num)[-10:]
    print(strNum)

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:", time.time()-start)