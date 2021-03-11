'''
If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, 
there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p ≤ 1000, is the number of solutions maximised?
'''

def methodTwo():
    vals = {}
    for a in range(1,1001):
        for b in range(a+1, 1001):
            c = (a*a + b*b)**0.5
            if c.is_integer() and a + b + c <= 1000:
                # print("a: ", a," b: ", b, " c: ", c)
                p = a + b + c
                if p in vals:
                    vals[p].append({a,b,c})
                else:
                    vals[p] = [{a,b,c}]
    
    index = -1
    max = 0
    for x in vals:
        print(x, vals[x])
        if len(vals[x]) > max:
            max = len(vals[x])
            index = x
    print(index, vals[index])

def brute():
    methodTwo()

def main():
    brute()

if __name__ == '__main__':
    main()