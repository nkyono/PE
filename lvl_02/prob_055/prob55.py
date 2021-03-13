'''
If we take 47, reverse and add, 47 + 74 = 121, which is palindromic.

Not all numbers produce palindromes so quickly. For example,

349 + 943 = 1292,
1292 + 2921 = 4213
4213 + 3124 = 7337

That is, 349 took three iterations to arrive at a palindrome.

Although no one has proved it yet, it is thought that some numbers, like 196, never produce a palindrome. 
A number that NEVER forms a palindrome through the reverse and add process is called a Lychrel number.
Due to the theoretical nature of these numbers, and for the purpose of this problem, 
we shall assume that a number is Lychrel until proven otherwise. 
In addition you are given that for every number below ten-thousand, 
it will either 
    (i) become a palindrome in less than fifty iterations, or, 
    (ii) no one, with all the computing power that exists, has managed so far to map it to a palindrome. 
In fact, 10677 is the first number to be shown to require over fifty iterations before producing a palindrome: 4668731596684224866951378664 (53 iterations, 28-digits).

Surprisingly, there are palindromic numbers that are themselves Lychrel numbers; the first example is 4994.

How many Lychrel numbers are there below ten-thousand?
'''
import time

def checkPalindrome(num):
    numStr = str(num)
    for c in range(int(len(numStr)/2)):
        if numStr[c] != numStr[(len(numStr)-1) - c]:
            return False
    return True

def flip(num):
    newNum = ''
    strNum = str(num)
    for x in strNum:
        newNum = x + newNum
    return int(newNum)

def test(lim):
    count = 0
    pals = {}
    lychrel = set()
    for x in range(lim):
        sum = x
        count = count + 1
        lychrel.add(x)
        for i in range(50):
            sum = sum + flip(sum)
            if sum in pals:
                if pals[sum]:
                    count = count - 1
                    print(x, sum, i)
                    lychrel.remove(x)
                    break
            else:
                if checkPalindrome(sum):
                    pals[sum] = True
                    count = count - 1
                    print(x, sum, i)
                    lychrel.remove(x)
                    break
                else:
                    pals[sum] = False
        
    print(count)
    assert 47 not in lychrel
    assert 349 not in lychrel
    assert 196 in lychrel
    assert 4994 in lychrel
    return lychrel

def testSingle(num):
    sum = num
    for i in range(50):
        print(i, sum, flip(sum))
        sum = sum + flip(sum)
        if checkPalindrome(sum):
            print("found:",num, sum, i)
            break

if __name__ == '__main__':
    assert flip(123) == 321
    assert flip(22345) == 54322
    assert checkPalindrome(1234) == False
    assert checkPalindrome(55455) == True
    # testSingle(4994)
    start_time = time.time()
    lychrel = test(10000)
    print("--- %s seconds ---" % (time.time() - start_time))



