'''
The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1); 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt, a 16K text file containing nearly two-thousand common English words, 
how many are triangle words?
'''

def checkTri(wordSum, n):
    for x in range(n+1):
        tri = (.5)*x*(x+1)
        if tri == wordSum:
            print(tri, wordSum)
            return True
    return False


def readFile():
    with open('prob_042/p042_words.txt','r') as file:
        lines = file.read().replace("\"","").split(",")

    lines = sorted(lines)
    return lines

def main():
    words = readFile()

    maxLength = 0
    for word in words:
        if len(word) > maxLength:
            maxLength = len(word)
    print(maxLength)
    
    triWords = []
    for word in words:
        calc_word = [ord(x)-64 for x in word]
        wordSum = 0
        for x in calc_word:
            wordSum = wordSum + x
        if checkTri(wordSum, 27):
            triWords.append(word)
        # print(word, calc_word, wordSum)

    print(len(triWords))


if __name__ == '__main__':
    main()