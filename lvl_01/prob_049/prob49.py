'''
The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330, is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, exhibiting this property, 
but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?
'''
def calcDivisors(target):
    divisors = []
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
                return False
            else:
                divisors.append(i)
                divisors.append(target/i)
                return False
    return True


# could definitely be done more efficiently
def seq():
    prime_digs = {}
    for x in range(1000,10000):
        if calcDivisors(x):
            nums = []
            for y in str(x):
                nums.append(y)
            nums_key = str(sorted(nums))
            if nums_key in prime_digs:
                prime_digs[nums_key].append(x)
            else:
                prime_digs[nums_key] = [x]

    for x in prime_digs:
        if len(prime_digs[x]) > 3:
            # if prime_digs[x][2]-prime_digs[x][1] == prime_digs[x][1]-prime_digs[x][0]:
            # print(x, prime_digs[x])
            diffs = {}
            prime_digs[x] = sorted(prime_digs[x])
            for y in prime_digs[x]:
                for z in prime_digs[x]:
                    diff = y - z
                    if diff in diffs:
                        diffs[diff].append(y)
                    else:
                        diffs[diff] = [y, z]
            for y in diffs:
                if len(diffs[y]) == 3 and y > 0:
                    diffs[y] = sorted(diffs[y])
                    # print(diffs[y])
                    if diffs[y][2] - diffs[y][1] == diffs[y][1] - diffs[y][0]:
                        print(y, diffs[y])
                        print(str(diffs[y][0]) + str(diffs[y][1]) + str(diffs[y][2]))

def main():
    seq()

if __name__ == '__main__':
    main()