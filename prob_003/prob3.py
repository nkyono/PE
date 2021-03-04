'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

def main():
    target = 600851475143
    factors = findFactors(target)

def findFactors(target):
    div = 2
    fact = 0
    while(target != 0):
        if(target%div != 0):
            div = div + 1
        else:
            fact = target
            target = target/div
            if(target==1):
                print(fact)
                return


if __name__ == '__main__':
    main()