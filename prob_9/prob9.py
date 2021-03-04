'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
# O(n^3)
def methodOne():
    a = 0
    b = 1
    c = 2
    while c < 1000:
        a = 0
        b = 1
        while b < c:
            a = 0
            while a < b:
                if a*a + b*b == c*c:
                    # print("a: ", a," b: ", b, " c: ", c)
                    if a + b + c == 1000:
                        print("Ans: ", a*b*c)
                a = a + 1
            b = b + 1
        c = c + 1

# O(n^2)
def methodTwo():
    # note: could have been range(1000), 
    # but then you can get 0, 500, 500, but we need a < b < c and I didn't want to add another check
    for a in range(1,1000):
        for b in range(a+1, 1000):
            c = (a*a + b*b)**0.5
            if a+b+c == 1000:
                print("a: ", a," b: ", b, " c: ", c)
                print("Ans: ", a*b*c)

# just gonna brute force
def main():
    #methodOne()
    methodTwo()

if __name__ == '__main__':
    main()