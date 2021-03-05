'''
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
# knuth algorithm L
# permuation generation in lexicographic order
def getPermutation(elems):
    if len(elems) < 2:
        return elems
    i = len(elems) - 2
    while i >= 0 and elems[i] > elems[i+1]:
        i = i - 1
    if i == -1:
        return elems
    k = len(elems) - 1
    while elems[i] > elems[k]:
        k = k - 1

    temp = elems[i]
    elems[i] = elems[k]
    elems[k] = temp

    low = i + 1
    high = len(elems) - 1
    while low < high:
        temp = elems[low]
        elems[low] = elems[high]
        elems[high] = temp
        low = low + 1
        high = high - 1
    return elems

def main():
    elems = [0,1,2,3,4,5,6,7,8,9]
    last = []
    x = 2
    while elems != last and x < 1000100:
        last = elems[:]
        getPermutation(elems)
        if (x == 1000000):
            s = ''.join(map(str, elems))
            print(x, s)
        x = x + 1

if __name__ == '__main__':
    main()