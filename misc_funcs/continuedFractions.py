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

# continued fraction for irrational numbers only works up to a certain point then breaks due to rounding errors
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

# a different continued fraction
# also breaks at a certain point due to floating point error 
# shouldn't use floating point arithmetic
import math
def contFracIrrII(a):
    arr = [int(math.sqrt(a))]
    next = arr[0]
    prev = math.sqrt(a)
    while(True):
        prev = prev - next
        prev = 1/(prev)
        next = int(prev)
        arr.append(next)
        # print(next, prev)
        if next == arr[0] * 2:
            break
    
    return arr

# a0/1, 
# (a1a0 + 1)/a1, 
# (a2(a1a0 + 1) + a0)/(a2a1 + 1), 
# (a3(a2(a1a0 + 1) + a0) + (a1a0 + 1))/(a3(a2a1 + 1) + a1)
def convergFrac(a, b, arr, lim):
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

# kinda cheating way to do euler's number
def contFracEuler(lim):
    arr = [2,1]
    for x in range(3,lim):
        if x % 3 == 0:
            arr.append(int(x/3 * 2))
        else:
            arr.append(1)
    return arr

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


    for x in range(2,150):
        if not math.sqrt(x).is_integer():
            print(x, contFracIrrII(x))
    # print(contFracIrrII(9969))

if __name__ == '__main__':
    main()