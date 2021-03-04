'''
If the numbers 1 to 5 are written out in words: 
one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, 
how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
'''
# hardest part and thing I messed up on most was the spellings
def writeNum(num):
    #print(num)
    length = 0
    thou = 'thousand'
    hund = 'hundred'
    # keeping ones, tens empty b/c they have own pattern
    # could have just hardcoded lengths, but easier to visualize this way
    # could have also used a dictionary to map numbers to spellings. prob/might have been better
    tens = [len(''), len(''), len('twenty'), len('thirty'), len('forty'), len('fifty'), len('sixty'), len('seventy'), len('eighty'), len('ninety')]
    teens = [len('ten'), len('eleven'), len('twelve'), len('thirteen'), len('fourteen'), len('fifteen'), len('sixteen'), len('seventeen'), len('eighteen'), len('nineteen')]
    ones = [len(''), len('one'), len('two'), len('three'), len('four'), len('five'), len('six'), len('seven'), len('eight'), len('nine')]
    
    numStr = str(num)
    if num > 999:
        # one thousand is max
        length = len('one') + len(thou)
    elif num > 99:
        # we know hundreds will not be 0
        length = length + ones[int(numStr[0])] + len(hund)
        rest = writeNum(int(numStr[1:]))
        length = length + rest
        if rest > 0:
            length = length + len('and')
    elif num > 19:
        length = length + tens[int(numStr[0])] + writeNum(int(numStr[1]))
    elif num > 9:
        length = teens[int(numStr[1])]
    else:
        length = ones[num]
        
    #print(length)
    return length

def getLengths():
    sum = 0
    for x in range(1,1001):
        sum = sum + writeNum(x)
    print(sum)

def main():
    getLengths()
    #writeNum(115)
    #writeNum(342)

if __name__ == '__main__':
    main()