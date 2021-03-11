'''
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, 
there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?
'''
# seems like a quite straight forward dynamic programming problem
# we can represent the vertices/corners as indexes of a matrix 
# NOTE: for a NxN grid there are N+1 vertices/corners

def getRoutes():
    # initialize matrix
    matrix = []
    for x in range(21):
        matrix.append(1)
        matrix[x] = []
        for y in range(21):
            matrix[x].append(1)

    for x in range(1, 21):
        for y in range(1, 21):
            matrix[x][y] = matrix[x-1][y] + matrix[x][y-1] 
    
    print(matrix[20][20])

def main():
    getRoutes()

if __name__ == '__main__':
    main()