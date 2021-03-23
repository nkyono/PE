'''
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, 
by only moving to the right and down, is indicated in bold red and is equal to 2427.

 
Find the minimal path sum from the top left to the bottom right by only moving right and down in matrix.txt, 
a 31K text file containing an 80 by 80 matrix.
'''

def traverse(matrix):
    sums = matrix[:]
    for x in range(1,len(matrix)):
        matrix[0][x] = matrix[0][x - 1] + matrix[0][x]
    for y in range(1,len(matrix)):
        matrix[y][0] = matrix[y-1][0] + matrix[y][0]
    for x in range(1,len(matrix)):
        for y in range(1,len(matrix[x])):
            sums[x][y] = min(sums[x-1][y], sums[x][y-1]) + matrix[x][y]
    
    '''
    for line in matrix:
        print(line)
    '''
    print(matrix[-1][-1])
        
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
    eightyMatrix = readMatrix("lvl_02/prob_081/p081_matrix.txt")
    testMatrix = readMatrix("lvl_02/prob_081/test_matrix.txt")

    traverse(testMatrix)
    traverse(eightyMatrix)

if __name__ == '__main__':
    import time
    start = time.time()
    main()
    print("time:", time.time() - start)