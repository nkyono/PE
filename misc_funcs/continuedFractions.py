# takes in two integers and returns an array of ints
# parameters a,b represents numerator,denominator repectively and returns array representing continued function
# For example, 3/8 returns [0,2,1,2]; 2/5 returns [0,2,2]; 415/93 returns [4,2,6,7]
# made to calc continuous fraction and not for things like root(2) == [1,2,2,2,2,...]
def contFrac(a, b):
    arr = []
    rem = a % b
    while(rem != 0):
        arr.append(int(a/b))
        temp = b
        b = rem
        a = temp
        rem = a % b
    arr.append(int(a/b))
    return arr

def contFracIrr(a, b, lim):
    arr = []
    rem = a % b
    while(rem != 0 and len(arr) < lim-1):
        arr.append(int(a/b))
        temp = b
        b = rem
        a = temp
        rem = a % b
    arr.append(int(a/b))
    return arr

# a0/1, 
# (a1a0 + 1)/a1, 
# (a2(a1a0 + 1) + a0)/(a2a1 + 1), 
# (a3(a2(a1a0 + 1) + a0) + (a1a0 + 1))/(a3(a2a1 + 1) + a1)
def convergFrac(a, b, lim):
    arr = []
    rem = a % b
    while(rem != 0 and len(arr) < lim-1):
        arr.append(int(a/b))
        temp = b
        b = rem
        a = temp
        rem = a % b
    arr.append(int(a/b))
    if len(arr) == 0:
        return

    nums = [arr[0], arr[1]*arr[0] + 1]
    dems = [1, arr[1]]
    fracs = [[nums[0],dems[0]],[nums[1],dems[1]]] 
    for x in range(2,lim):
        nums.append(arr[x]*nums[x-1] + nums[x-2])
        dems.append(arr[x]*dems[x-1] + dems[x-2])
        fracs.append([nums[x], dems[x]])

    for x in range(len(nums)):
        print("fraction:",nums[x],"/",dems[x])

    return fracs


def main():
    import math
    print(contFrac(415, 93))
    print(contFrac(3, 8))
    print(contFrac(2, 5))
    print(contFrac(1, 3))
    print(contFracIrr(math.sqrt(2),1,5))
    print(contFracIrr(math.sqrt(19),1,10))
    print(contFracIrr(math.pi,1,10))
    assert contFracIrr(math.sqrt(2),1,5) == [1,2,2,2,2]
    assert contFracIrr(math.sqrt(19),1,13) == [4,2,1,3,1,2,8,2,1,3,1,2,8]
    assert contFracIrr(math.pi,1,12) == [3,7,15,1,292,1,1,1,2,1,3,1]

    print(convergFrac(math.sqrt(2),1,5))

if __name__ == '__main__':
    main()