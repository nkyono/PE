'''
The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
'''

def selfPowers(lim):
    sum = 0
    for x in range(1, lim+1):
        sum = sum + x ** x
    return sum

def main():
    assert selfPowers(10) == 10405071317
    ans = selfPowers(1000)
    print(str(ans)[-10:])

if __name__ == '__main__':
    main()