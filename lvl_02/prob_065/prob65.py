'''
Find the sum of digits in the numerator of the 100th convergent of the continued fraction for e.
'''
import math

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
    for x in range(3,lim+1):
        if x % 3 == 0:
            arr.append(int(x/3 * 2))
        else:
            arr.append(1)
    return arr

def main():
    arr = contFracEuler(100)
    print(arr)
    fracs = convergFrac(math.e, 1, arr, 100)
    val = 0
    for x in str(fracs[-1][0]):
        val = val + int(x)
    print(val)
    return

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:",time.time()-start)