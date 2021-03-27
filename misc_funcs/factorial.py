def factorial(n):
    fact = 1
    while(n > 0):
        fact = fact * n
        n = n - 1
    return fact

if __name__ == '__main__':
    assert factorial(0) == 1
    assert factorial(10) == 3628800
    assert factorial(100) == 93326215443944152681699238856266700490715968264381621468592963895217599993229915608941463976156518286253697920827223758251185210916864000000000000000000000000
    
