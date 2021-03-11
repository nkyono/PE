'''
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
'''

def main():
    concat = ""
    x = 0
    while len(concat) < 1000001:
        concat = concat + str(x)
        x = x + 1
    print(int(concat[1])*int(concat[10])*int(concat[100])*int(concat[1000])*int(concat[10000])*int(concat[100000])*int(concat[1000000]))

if __name__ == '__main__':
    main()