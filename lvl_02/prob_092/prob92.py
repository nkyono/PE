'''
A number chain is created by continuously adding the square of the digits in a number to form a new number until it has been seen before.

For example,

44 → 32 → 13 → 10 → 1 → 1
85 → 89 → 145 → 42 → 20 → 4 → 16 → 37 → 58 → 89

Therefore any chain that arrives at 1 or 89 will become stuck in an endless loop. 
What is most amazing is that EVERY starting number will eventually arrive at 1 or 89.

How many starting numbers below ten million will arrive at 89?
'''

# took a little long, but idk it gets it done relatively fast ~ 101 seconds
# should have made a dictionary that marked whether a number goes to 1 or 89, would be much faster

def chain(num):
    strNum = str(num)
    while num != 89 and num != 1:
        n = 0
        for c in strNum:
            n = n + int(c)**2
        num = n
        strNum = str(num)
    return num


def main():
    count = 0
    for x in range(1,10000001):
        if chain(x) == 89:
            # print(x)
            count = count + 1
    print(count)

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:", time.time()-start)