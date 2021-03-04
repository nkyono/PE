'''
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?
'''

def calcPower():
    num = 2**1000
    num = str(num)
    sum = 0 
    for x in range(len(num)):
        sum = sum + int(num[x])
    print(sum)

def main():
    calcPower()

if __name__ == '__main__':
    main()