def triNums(minLim, maxLim):
    nums = []
    for x in range(minLim, maxLim + 1):
        nums.append(x*(x+1)/2)
    return nums

def sqrNums(minLim, maxLim):
    nums = []
    for x in range(minLim, maxLim + 1):
        nums.append(x*x)
    return nums
    
def pentNums(minLim, maxLim):
    nums = []
    for x in range(minLim, maxLim + 1):
        nums.append(x*(3*x-1)/2)
    return nums

def hexNums(minLim, maxLim):
    nums = []
    for x in range(minLim, maxLim + 1):
        nums.append(x*(2*x-1))
    return nums

def heptNums(minLim, maxLim):
    nums = []
    for x in range(minLim, maxLim + 1):
        nums.append(x*(5*x-3)/2)
    return nums

def octNums(minLim, maxLim):
    nums = []
    for x in range(minLim, maxLim + 1):
        nums.append(x*(3*x-2))
    return nums

def main():
    assert triNums(1,5) == [1, 3, 6, 10, 15]
    assert sqrNums(1,5) == [1, 4, 9, 16, 25]
    assert pentNums(1,5) == [1, 5, 12, 22, 35]
    assert hexNums(1,5) == [1, 6, 15, 28, 45]
    assert heptNums(1,5) == [1, 7, 18, 34, 55]
    assert octNums(1,5) == [1, 8, 21, 40, 65]

if __name__ == '__main__':
    main()