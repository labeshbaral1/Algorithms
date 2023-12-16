def euclidean_gcd(a, b):
    if b == 0: return a

    
    return euclidean_gcd(b, a % b)


print(euclidean_gcd(10, 5))
