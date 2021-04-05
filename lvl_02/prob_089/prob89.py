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

# proposal: find minimal way to make each digit place
# ex 999 and 666: 999 -> CM | XC | IX; 666 -> DC | LX | VI

def createRoman(num):
    roman = ""
    numStr = str(num)
    nums = {
        '1' : ["I","X","C"],
        '2' : ["II","XX","CC"],
        '3' : ["III","XXX","CCC"],
        '4' : ["IV","XL","CD"],
        '5' : ["V","L","D"],
        '6' : ["VI","LX","DC"],
        '7' : ["VII","LXX","DCC"],
        '8' : ["VIII","LXXX","DCCC"],
        '9' : ["IX","XC","CM"],
        '0' : ["","",""]
    }
    for i in range(len(numStr)-1,-1,-1):
        if len(numStr) - i < 4:
            roman = nums[numStr[i]][len(numStr) - i - 1] + roman
        else:
            roman = ('M'*(int(numStr[0]))) + roman
            break
    print(roman)
    return roman


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
    return val

def main():
    f = open("./lvl_02/prob_089/p089_roman.txt", "r")
    preCount = 0
    for line in f.readlines():
        num = list(line.strip())
        preCount = preCount + len(num)
        print(line.strip())
        val = parseRoman(num)
        roman = createRoman(val)
        print(len(num)-len(str(roman)))
        preCount = preCount - len(str(roman))

        print("------------------")
    print(preCount)
    return

if __name__  == '__main__':
    main()