def triNums(lim):
    nums = []
    for x in range(1,lim + 1):
        nums.append(x*(x+1)/2)
    return nums

def sqrNums(lim):
    nums = []
    for x in range(1,lim + 1):
        nums.append(x*x)
    return nums
    
def pentNums(lim):
    nums = []
    for x in range(1,lim + 1):
        nums.append(x*(3*x-1)/2)
    return nums

def hexNums(lim):
    nums = []
    for x in range(1,lim + 1):
        nums.append(x*(2*x-1))
    return nums

def heptNums(lim):
    nums = []
    for x in range(1,lim + 1):
        nums.append(x*(5*x-3)/2)
    return nums

def octNums(lim):
    nums = []
    for x in range(1,lim + 1):
        nums.append(x*(3*x-2))
    return nums

def main():
    assert triNums(5) == [1, 3, 6, 10, 15]
    assert sqrNums(5) == [1, 4, 9, 16, 25]
    assert pentNums(5) == [1, 5, 12, 22, 35]
    assert hexNums(5) == [1, 6, 15, 28, 45]
    assert heptNums(5) == [1, 7, 18, 34, 55]
    assert octNums(5) == [1, 8, 21, 40, 65]

if __name__ == '__main__':
    main()