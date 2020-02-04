def prime_factorization():
    n = int(input('Input number: '))
    primes_list = [2]
    prime_factor_list = []
    for num in range(3, n, 2):
        count = 0
        for prime in primes_list:
            if num % prime == 0:
                count += 1
        if count == 0:
            primes_list.append(num)

    for prime in primes_list:
        if n % prime == 0:
            prime_factor_list.append(prime)

    if len(prime_factor_list) > 0:
        return prime_factor_list

    else:
        return 'No prime factors exist!'


print(prime_factorization())

