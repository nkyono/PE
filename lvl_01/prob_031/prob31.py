'''
In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?
'''

# straight forward DP problem
def solve(n):
    # 1p, 2p, 5p, 10p, 20p, 50p, 100p, 200p
    coin_index = [0,1,2,3,4,5,6,7]
    coins = [1,2,5,10,20,50,100,200]
    ways = []
    for x in range(n+1):
        ways.append(0)
    ways[0] = 1
    for x in coins:
        for y in range(len(ways)):
            if x <= y:
                ways[y] = ways[y] + ways[y - x]
    print(ways[n])


def main():
    n = 200
    solve(n)
    test = 12
    solve(test)

if __name__ == '__main__':
    main()