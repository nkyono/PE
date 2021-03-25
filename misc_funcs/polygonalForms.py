def triNums(minLim, maxLim):
    nums = []
    x = 1
    while(True):
        num = int(x*(x+1)/2)
        if num < maxLim:
            if num > minLim:
                nums.append(num)
        else:
            break
        x = x + 1
    return nums

def sqrNums(minLim, maxLim):
    nums = []
    x = 1
    while(True):
        num = int(x*x)
        if num < maxLim:
            if num > minLim:
                nums.append(num)
        else:
            break
        x = x + 1
    return nums
    
def pentNums(minLim, maxLim):
    nums = []
    x = 1
    while(True):
        num = int(x*(3*x-1)/2)
        if num < maxLim:
            if num > minLim:
                nums.append(num)
        else:
            break
        x = x + 1
    return nums

def hexNums(minLim, maxLim):
    nums = []
    x = 1
    while(True):
        num = int(x*(2*x-1))
        if num < maxLim:
            if num > minLim:
                nums.append(num)
        else:
            break
        x = x + 1
    return nums

def heptNums(minLim, maxLim):
    nums = []
    x = 1
    while(True):
        num = int(x*(5*x-3)/2)
        if num < maxLim:
            if num > minLim:
                nums.append(num)
        else:
            break
        x = x + 1
    return nums

def octNums(minLim, maxLim):
    nums = []
    x = 1
    while(True):
        num = int(x*(3*x-2))
        if num < maxLim:
            if num > minLim:
                nums.append(num)
        else:
            break
        x = x + 1
    return nums

def main():
    assert triNums(0,20) == [1, 3, 6, 10, 15]
    assert triNums(0,3) == [1]
    assert sqrNums(0,30) == [1, 4, 9, 16, 25]
    assert pentNums(0,40) == [1, 5, 12, 22, 35]
    assert hexNums(0,50) == [1, 6, 15, 28, 45]
    assert heptNums(0,60) == [1, 7, 18, 34, 55]
    assert octNums(0,70) == [1, 8, 21, 40, 65]

if __name__ == '__main__':
    main()