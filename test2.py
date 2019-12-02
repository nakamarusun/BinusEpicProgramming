def prime(n):
    prime = [2]
    testPrime = 1
    while len(prime) < n:
        primeCheck = False
        testPrime += 2
        for i in prime:
            if (testPrime % i == 0):
                primeCheck = True
        if primeCheck == False:
            prime.append(testPrime)
    print(prime)
    return prime[n-1]

print(prime(10))