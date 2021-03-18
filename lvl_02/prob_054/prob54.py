'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

0.High Card: Highest value card.
1.One Pair: Two cards of the same value.
2.Two Pairs: Two different pairs.
3.Three of a Kind: Three cards of the same value.
4.Straight: All cards are consecutive values.
5.Flush: All cards of the same suit.
6.Full House: Three of a kind and a pair.
7.Four of a Kind: Four cards of the same value.
8.Straight Flush: All cards are consecutive values of same suit.
9.Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; 
for example, a pair of eights beats a pair of fives (see example 1 below). 
But if two ranks tie, for example, both players have a pair of queens, 
then highest cards in each hand are compared (see example 4 below); 
if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. 
Each line of the file contains ten cards (separated by a single space): 
the first five are Player 1's cards and the last five are Player 2's cards. 
You can assume that all hands are valid (no invalid characters or repeated cards), 
each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace ==> 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

# calcHand computes hand val and returns hand value and highest card (for tie break)
def calcHand(hand):
    isFlush = hand[0][1] == hand[1][1] == hand[2][1] == hand[3][1] == hand[4][1]
    isStraight = True
    isFour = False
    isThree = False
    numPairs = 0
    isRoyal = True
    highest = -1
    pairs = {}
    for card in hand:
        if card[0] > highest:
            highest = card[0]
        if card[0] in pairs:
            pairs[card[0]] = pairs[card[0]] + 1
        else:
            pairs[card[0]] = 1

    pairTypes = {}
    for pair in pairs:
        if pairs[pair] == 4:
            pairTypes[4] = [pair]
            isFour = True
        elif pairs[pair] == 3:
            pairTypes[3] = [pair]
            isThree = True
        elif pairs[pair] == 2:
            if 2 in pairTypes:
                numPairs = 2
                pairTypes[2].append(pair)
            else:
                numPairs = 1
                pairTypes[2] = [pair]

    for x in range(4):
        if hand[x][0] < 11:
            isRoyal = False
        if hand[x][0] - hand[x+1][0] != -1:
            isStraight = False
            break

    if isStraight:
        return [highest, 4, highest]
    if isFlush:
        if isRoyal:
            return [highest, 9, -1]
        if isStraight:
            return [highest, 8, highest]    
        return [highest, 5, highest]
    if isFour:
        return [highest, 7, pairTypes[4][0]]
    if numPairs == 1 and isThree:
        return [highest, 6, pairTypes[3][0]]
    if isThree:
        return [highest, 3, pairTypes[3][0]]
    if numPairs == 2:
        return [highest, 2, max(pairTypes[2][0], pairTypes[2][1])]
    if numPairs == 1:
        return [highest, 1, pairTypes[2][0]]

    return [highest, 0, highest]

# compares hand values (or highest card if tie)
def compHands(a,b):
    if a[1] == b[1]:
        if a[2] == b[2]:
            return a[0] > b[0]
        return a[2] > b[2]
    return a[1] > b[1]

# translates the hands to a format I want to use for my calcs
def cleanHand(hand):
    newHand = []
    for card in hand:
        val = -1
        try:
            val = int(card[0])
        except:
            cases = {'T':10, 'J':11, 'Q':12, 'K':13, 'A':14}
            val = cases[card[0]]
        newHand.append([val, card[1]])

    return newHand

def sortHand(hand):
    hand = sorted(hand)
    return hand

def test():
    count = 0
    f = open("lvl_02/prob_054/p054_poker.txt")
    for line in f.readlines():
        line = line.split()
        print("player 1:", line[:5], " | player 2:", line[5:])
        p1 = calcHand(sortHand(cleanHand(line[:5])))
        p2 = calcHand(sortHand(cleanHand(line[5:])))
        if compHands(p1, p2):
            print("player 1 wins!", p1,p2)
            count = count + 1
        else:
            print("player 2 wins!",p1, p2)
    print(count)

if __name__ == '__main__':
    import time
    start = time.time()
    test()
    print("time:",time.time()-start)