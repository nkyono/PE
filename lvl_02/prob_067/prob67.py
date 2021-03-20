'''
By starting at the top of the triangle below and moving to adjacent numbers on the row below, 
the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt, a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, as there are 299 altogether! 
If you could check one trillion (1012) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)
'''

# literally just my prob 18 solution
# pattern: sumTo[a][b] = max(sumTo[a-1][b], sumTo[a-1][b-1]) + val[a][b], edge cases b=0, b=length of layer
def traverse(matrix):
    sums = matrix[:]
    for x in range(1,len(matrix)):
        # print("line: ", matrix[x], " size: ", len(matrix[x]))
        for y in range(len(matrix[x])):
            if(y == 0):
                sums[x][y] = sums[x-1][y] + matrix[x][y]
            elif(y == len(matrix[x])-1):
                sums[x][y] = sums[x-1][y-1] + matrix[x][y]
            else:
                sums[x][y] = max(sums[x-1][y], sums[x-1][y-1]) + matrix[x][y]
    maxSum = matrix[len(matrix)-1][0]
    for x in range(len(matrix[-1])):
        if(maxSum < matrix[-1][x]):
            maxSum = matrix[-1][x]
    print("maxSum: ", maxSum)
        

def main():
    f = open("lvl_02/prob_067/p067_triangle.txt", "r")
    big_tri = []
    for line in f.readlines():
        line = list(map(int, line.split()))
        big_tri.append(line)
    
    traverse(big_tri)

if __name__ == '__main__':
    main()