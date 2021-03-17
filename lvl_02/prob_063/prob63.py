'''
The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?
'''
def compDigits(num, x):
    strPow = str(num ** x)
    if len(strPow) == x:
        print(num, x, strPow)
        return True
    return False

def test():
    count = 0
    for x in range(1,100):
        for y in range(1,100):
            if compDigits(x, y):
                count = count + 1
    print(count)

if __name__ == '__main__':
    test()