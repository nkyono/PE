# phi function (euler's totient function) gives the number of positive integers up to n that are relatively prime to n
# ie. a prime number would give n - 1
def phi(n): 
    result = n
    p = 2
    while p * p <= n : 
        if n % p == 0 : 
            while n % p == 0 : 
                n = n // p 
            result = result * (1.0 - (1.0 / float(p))) 
        p = p + 1
    if n > 1 :
        result = result * (1.0 - (1.0 / float(n))) 
   
    return int(result) 