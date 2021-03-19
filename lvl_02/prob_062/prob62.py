'''
The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). 
In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.
'''
            
def testSets(sets):
    nums = {}
    for x in sets:
        key = ''.join(sorted(list(str(x))))
        if key in nums:
            nums[key].append(x)
        else:
            nums[key] = [x]
    revNums = {}
    for x in nums:
        if len(nums[x]) == 5:
            print(nums[x])
        if len(nums[x]) in revNums:
            revNums[len(nums[x])].append(x)
        else:
            revNums[len(nums[x])] = [x]
    return revNums

def calcPows(lim, p):
    pows = set()
    for n in range(lim):
        pows.add(n**p)
    return pows

def test(lim):
    sets = calcPows(lim, 3)
    testSets(sets)

if __name__ == '__main__':
    import time
    start = time.time()
    test(10000)
    print("time:", time.time()-start)