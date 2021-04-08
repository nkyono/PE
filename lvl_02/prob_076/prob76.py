'''
It is possible to write five as a sum in exactly six different ways:

6 + 1
5 + 1 + 1
4 + 2 + 1
3 + 3 + 1
4 + 1 + 1 + 1
3 + 2 + 1 + 1
3 + 1 + 1 + 1 + 1
2 + 2 + 1 + 1 + 1
2 + 1 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1 + 1
5 + 2
3 + 2 + 2
4 + 3


5 + 1
4 + 2
3 + 3
4 + 1 + 1
3 + 2 + 1
3 + 1 + 1 + 1
2 + 2 + 1 + 1
2 + 1 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1 + 1

4 + 1
3 + 2
3 + 1 + 1
2 + 2 + 1
2 + 1 + 1 + 1
1 + 1 + 1 + 1 + 1

3 + 1
2 + 2
2 + 1 + 1
1 + 1 + 1 + 1

2 + 1
1 + 1 + 1

1 + 1

0, 1, 2, 4, 6, 9,

How many different ways can one hundred be written as a sum of at least two positive integers?
'''

def calcWays(lim):
    ways = [0 for x in range(lim)]
    ways[2] = 1
    for x in range(3,lim):
        sum = ways[x-1] + 1
        for y in range(1,int(x/2)+1):
            sum = sum + int(y/2)
        ways[x] = sum
    print(ways)
    
def test():
    calcWays(100)

if __name__ == '__main__':
    import time
    start = time.time()
    test()
    print("time:",time.time()-start)