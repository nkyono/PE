'''
Comparing two numbers written in index form like 211 and 37 is not difficult, 
as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382^518061 > 519432^525806 would be much more difficult, 
as both numbers contain over three million digits.

Using base_exp.txt, a 22K text file containing one thousand lines with a base/exponent pair on each line, 
determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.
'''
import math

# solved via getting # of digits of each exponent rather than calculating
# line 172 and 709 both have 3005316 digits
# I just guessed cause only two options, I assume you can also look at the base + exponent to narrow down to line 709

def main():
    f = open("./lvl_02/prob_099/p099_base_exp.txt", "r")
    x = 1
    digits = []
    for line in f.readlines():
        line = line.strip().split(',')
        base = int(line[0])
        exp = int(line[1])
        dig = math.floor(math.log(base,10) * exp) + 1
        digits.append([dig, x])
        x = x + 1
    digits = sorted(digits)
    print(digits)
    return

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:",time.time()-start)