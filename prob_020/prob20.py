'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!
'''
def sumDigits(num):
    strNum = str(num)
    sum = 0
    for i in range(len(strNum)):
        sum = sum + int(strNum[i])
    return sum

def factorial(num):
    factTotal = 1
    for n in range(1, num+1):
        factTotal = factTotal * n
    print(factTotal)
    print(sumDigits(factTotal))

def main():
    factorial(100)

if __name__ == '__main__':
    main()