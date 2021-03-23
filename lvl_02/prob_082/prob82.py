'''
NOTE: This problem is a more challenging version of Problem 81.

The minimal path sum in the 5 by 5 matrix below, 
by starting in any cell in the left column and finishing in any cell in the right column, 
and only moving up, down, and right, is indicated in red and bold; the sum is equal to 994.

Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt, 
a 31K text file containing an 80 by 80 matrix.
'''

def traverse(matrix):
    sums = []
    for x in range(len(matrix)):
        sums.append(matrix[x][:])

    for x in range(1,len(matrix)):
        for y in range(len(matrix[x])):
            sums[y][x] = matrix[y][x] + sums[y][x-1]
        # added this bool to check whether matrix has changed
        # way the current logic works, idt it would work if say it went up or down the same column more than once
        changed = True
        while changed:
            changed = False
            for z in range(len(matrix[x])):
                if z == 0:
                    if sums[z][x] > sums[z+1][x] + matrix[z][x]:
                        sums[z][x] = sums[z+1][x] + matrix[z][x]
                        changed = True
                elif z == len(matrix[x]) - 1:
                    if sums[z][x] > sums[z-1][x] + matrix[z][x]:
                        sums[z][x] = sums[z-1][x] + matrix[z][x]
                        changed = True
                else:
                    if sums[z][x] > sums[z-1][x] + matrix[z][x] or sums[z][x] > sums[z+1][x] + matrix[z][x]:
                        sums[z][x] = min(sums[z-1][x], sums[z+1][x]) + matrix[z][x]
                        changed = True
    
    minSum = sums[-1][-1]
    for x in range(len(matrix[0])):
        minSum = min(sums[x][-1],minSum)
    print(minSum)

        
def readMatrix(filename):
    file = open(filename, "r")
    matrix = []
    for line in file.readlines():
        matrix.append(list(map(int,line.split(','))))

    '''
    for x in matrix:
        print(x)
    print()
    '''

    return matrix

def main():
    eightyMatrix = readMatrix("lvl_02/prob_082/p082_matrix.txt")
    testMatrix = readMatrix("lvl_02/prob_082/test_matrix.txt")

    traverse(testMatrix)
    traverse(eightyMatrix)

if __name__ == '__main__':
    import time
    start = time.time()
    try:
        main()
    finally:
        print("time:", time.time() - start)