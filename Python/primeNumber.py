def prime(n):
    prime, testPrime = [2], 1
    while len(prime) < n:
        primeCheck = False
        testPrime += 2
        for i in prime:
            if (testPrime % i == 0):
                primeCheck = True
                break
            if (testPrime // 2 < i):
                break
        if primeCheck == False:
            prime.append(testPrime)
    return prime[n-1]

print(prime(5000))