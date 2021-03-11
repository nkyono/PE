'''
Using names.txt, a 46K text file containing over five-thousand first names, 
begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, 
COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
def getNameVal(name):
    val = 0
    for x in name:
        val = val + (ord(x) - 64)
    
    return val

def readFile():
    with open('prob_022/p022_names.txt','r') as file:
        lines = file.read().replace("\"","").split(",")

    lines = sorted(lines)
    # assertion to test sorting
    # assert lines[937] == 'COLIN'
    return lines

def sumScores(names):
    sum = 0
    for x in range(len(names)):
        val = getNameVal(names[x])
        sum = sum + ((x+1) * val)
    
    print(sum)

def main():
    names = readFile()
    sumScores(names)
    # getNameVal('COLIN')

if __name__ == '__main__':
    main()