'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
import time

def test():
    for x in range(1,10000000):
        xSet = set(str(x))
        i = 1
        newX = x * i
        newSet = set(str(newX))
        while newSet == xSet:
            # print(newSet, xSet)
            i = i + 1
            newX = x * i
            newSet = set(str(newX))
        if i >= 6:
            print(x)
            return x

def testSets(setA, setB):
    if setA == setB:
        return True
    return False

if __name__ == '__main__':
    assert testSets(set('125874'), set('251748'))
    start_time = time.time()
    test()
    print("--- %s seconds ---" % (time.time() - start_time))
