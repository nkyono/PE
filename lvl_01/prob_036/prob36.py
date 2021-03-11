'''
The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)
'''
def checkPalindrome(n):
    strN = str(n)
    i = 0
    j = len(strN) - 1
    while i < j:
        if strN[i] != strN[j]:
            return False
        i = i + 1
        j = j - 1
    
    return True

def main():
    sum = 0
    for x in range(1000000):
        if checkPalindrome(x):
            if checkPalindrome(bin(x)[2:]):
                print(x, bin(x)[2:])
                sum = sum + x
    print(sum)

if __name__ == '__main__':
    main()