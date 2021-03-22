def genPrimes():
    num = 2
    while True:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            yield num
        num += 1


primes = genPrimes()

for _ in range(10):
    print(next(primes))