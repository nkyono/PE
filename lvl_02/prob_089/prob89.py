'''
For a number written in Roman numerals to be considered valid there are basic rules which must be followed. 
Even though the rules allow some numbers to be expressed in more than one way there is always a "best" way of writing a particular number.

For example, it would appear that there are at least six ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

However, according to the rules only XIIIIII and XVI are valid, 
and the last example is considered to be the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt, contains one thousand numbers written in valid, 
but not necessarily minimal, Roman numerals

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.
'''
'''
Roman Numeral Rules:
    • Numerals must be arranged in descending order of size.
    • M, C, and X cannot be equalled or exceeded by smaller denominations.
    • D, L, and V can each only appear once.

Rules for subtraction
    • Only one I, X, and C can be used as the leading numeral in part of a subtractive pair.
    • I can only be placed before V and X.
    • X can only be placed before L and C.
    • C can only be placed before D and M.

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000
'''
numerals = {
    "I": 1, 
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}

'''
# completely misread problem
def parseRoman(num):
    numCount = {}
    # preset prev to max value, prev checks that numeral is descending 
    prev = numerals["I"]
    # preset numeral counts so that I don't need to check if in dict later
    for n in numerals:
        numCount[n] = 0

    val = 0
    for n in range(len(num)-1, -1, -1):
        x = num[n]
        if prev > numerals[x]:
            print("Breaks: Numerals must be arranged in descending order of size.")
            return False
        numCount[x] = numCount[x] + 1
        if (x == "M" or x == "C" or x == "X") and prev != numerals[x] and val >= numerals[x]:
            print("Breaks: M, C, and X cannot be equalled or exceeded by smaller denominations.")
            return False
        val = val + numerals[x]
        prev = numerals[x]
    
    for n in numCount:
        if (n == "D" or n == "L" or n == "V") and numCount[n] > 1:
            print("Breaks: D, L, and V can each only appear once.")
            return False

    return True
'''
def parseRoman(num):
    val = 0
    temp = 0
    for x in range(len(num)):
        if x < len(num)-1 and numerals[num[x]] < numerals[num[x+1]]:
            temp = temp - numerals[num[x]]
        else:
            val = val + temp + numerals[num[x]]
            temp = 0
    print(val)
    return False

def main():
    f = open("./lvl_02/prob_089/p089_roman.txt", "r")
    preCount = 0
    for line in f.readlines():
        num = list(line.strip())
        preCount = preCount + len(num)
        print(line.strip())
        parseRoman(num)
        print("------------------")
    print(preCount)
    return

if __name__  == '__main__':
    main()