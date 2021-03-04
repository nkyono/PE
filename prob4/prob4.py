'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
def checkPalindrome(product):
    str_prod = str(product)
    for x in range(0, int(len(str_prod)/2)):
        if str_prod[x] != str_prod[len(str_prod)-x-1]:
            return False
    return True

# brute forced, seems highly inefficient
def main():
    max_palindrome = 0
    max_num1 = 0
    max_num2 = 0
    num1 = 999
    num2 = 999
    while num1 > 99 and num2 > 99:
        product = num1 * num2
        if checkPalindrome(product):
            if product > max_palindrome:
                max_palindrome = product
                max_num1 = num1
                max_num2 = num2
        temp1 = num1
        while num1 > 99 and num2 > 99:
            product = int(num1 * num2)
            if checkPalindrome(product):
                if product > max_palindrome:
                    max_palindrome = product
                    max_num1 = num1
                    max_num2 = num2
            num1 = num1 - 1
        num1 = temp1 - 1
        num2 = num2 - 1

    print("num1: ", max_num1, ", num2: ", max_num2, ", product: ", max_palindrome)


if __name__ == '__main__':
    main()