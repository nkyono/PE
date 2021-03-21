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

def main():
    print(contFrac(415, 93))
    print(contFrac(3, 8))
    print(contFrac(2, 5))
    print(contFrac(1, 3))

if __name__ == '__main__':
    main()