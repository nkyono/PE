'''
The number 145 is well known for the property that the sum of the factorial of its digits is equal to 145:

1! + 4! + 5! = 1 + 24 + 120 = 145

Perhaps less well known is 169, in that it produces the longest chain of numbers that link back to 169; 
it turns out that there are only three such loops that exist:

169 → 363601 → 1454 → 169
871 → 45361 → 871
872 → 45362 → 872

It is not difficult to prove that EVERY starting number will eventually get stuck in a loop. For example,

69 → 363600 → 1454 → 169 → 363601 (→ 1454)
78 → 45360 → 871 → 45361 (→ 871)
540 → 145 (→ 145)

Starting with 69 produces a chain of five non-repeating terms, 
but the longest non-repeating chain with a starting number below one million is sixty terms.

How many chains, with a starting number below one million, contain exactly sixty non-repeating terms?
'''
def factorial(n):
    fact = 1
    while(n > 0):
        fact = fact * n
        n = n - 1
    return fact

# could be optimized
def main():
    singleDigitFacts = {}
    for x in range(10):
        singleDigitFacts[x] = factorial(x)
    facts = {}
    for x in range(1,1000000):
        strx = str(x)
        next = 0
        count = 1
        seen = set()
        for c in strx:
            next = next + singleDigitFacts[int(c)]
        while True:
            if next in facts:
                count = count + facts[next]
                seen.add(next)
            if next in seen:
                break
            seen.add(next)
            strx = str(next)
            next = 0
            for c in strx:
                next = next + singleDigitFacts[int(c)]
            count = count + 1
        facts[x] = count
    count = 0
    for x in facts:
        if facts[x] == 60:
            count = count + 1
    print(count)

if __name__ == '__main__':
    import time
    start = time.time()
    try:
        main()
    finally:
        print("\ntime:", time.time() - start)