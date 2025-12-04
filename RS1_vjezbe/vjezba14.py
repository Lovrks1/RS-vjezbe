# Vježba 14

def isPrime(n):
    if n <= 1:
        return False  
    for i in range(2, int(n**0.5) + 1):  
        if n % i == 0:
            return False
    return True

def primes_in_range(start, end):
    prosti = []
    for broj in range(start, end + 1):
        if isPrime(broj):
            prosti.append(broj)
    return prosti

print(f"{7} → {isPrime(7)}")
print(f"{10} → {isPrime(10)}")
print(primes_in_range(1, 10))
