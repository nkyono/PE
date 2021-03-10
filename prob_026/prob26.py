'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''
# think i need to do something with euler's totient function
# https://www.youtube.com/watch?v=qa_hksAzpSg; https://mathworld.wolfram.com/DecimalPeriod.html
# pretty sure the longest cycle will be the largest phi(prime < 1000)

# turns out it was 983 which is the 3rd largest prime,
# 983 has a decimal repeat of phi(983) = 982
# still not totally sure about this one, but the period will always be related to the totient
def calcDivisors(target):
    if target < 0:
        return False
    divisors = []
    for i in range(2,int(target**(1/2))+1):
        if target % i == 0:
            if target/i == i:
                divisors.append(i)
                return False
            else:
                divisors.append(i)
                divisors.append(target/i)
                return False
    return True

def main():
    for x in range(999, -1, -1):
        if calcDivisors(x):
            print(x)

if __name__ == '__main__':
    main()