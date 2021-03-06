'''
The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.
'''

# by keeping track of chain lengths created so far, we can reduce number of computations
# we can check to see if we already computed the rest of the chain of number we get rather than recompute
chains = {}

def makeChain(num):
    chainLen = 0
    while(num != 1):
        if num in chains:
            return chainLen + chains[num]
        chainLen = chainLen + 1
        if(num % 2 == 0):
            num = num / 2
        else:
            num = 3 * num + 1
    return chainLen + 1

def main():
    maxChain = 0
    startingVal = -1
    for x in range(1,1000000):
        chain = makeChain(x)
        if x not in chains:
            chains[x] = chain
        if chain > maxChain:
            maxChain = chain
            startingVal = x
    print(startingVal)
    

if __name__ == '__main__':
    main()