from math import sqrt
from typing import Dict

# Sieve of Eratosthenes
# Code by David Eppstein, UC Irvine, 28 Feb 2002
# http://code.activestate.com/recipes/117119/

def get_next_prime():
    """ Generate an infinite sequence of prime numbers.
    """
    # Maps composites to primes witnessing their compositeness.
    # This is memory efficient, as the sieve is not "run forward"
    # indefinitely, but only as long as required by the current
    # number being tested.
    #
    D = {}

    # The running integer that's checked for primeness
    q = 2

    while True:
        if q not in D:
            # q is a new prime.
            # Yield it and mark its first multiple that isn't
            # already marked in previous iterations
            #
            yield q
            D[q * q] = [q]
        else:
            # q is composite. D[q] is the list of primes that
            # divide it. Since we've reached q, we no longer
            # need it in the map, but we'll mark the next
            # multiples of its witnesses to prepare for larger
            # numbers
            #
            for p in D[q]:
                D.setdefault(p + q, []).append(p)
            del D[q]

        q += 1


found_primes = []
prime_gen = get_next_prime()


def prime_factorization(n: int) -> Dict[int, int]:
    while len(found_primes) == 0 or found_primes[-1] < sqrt(n):
        found_primes.append(prime_gen.__next__())

    factors = {}

    for p in found_primes:
        while n % p == 0:
            if p not in factors:
                factors[p] = 1
            else:
                factors[p] += 1
            n = n / p

    if n > 2:
        factors[n] = 1

    return factors


# print(prime_factorization(315))
# print(prime_factorization(70))
# print(prime_factorization(529))


def sum_of_factors(n: int) -> int:
    factors = prime_factorization(n)
    total = 1
    for factor, count in factors.items():
        total *= round((pow(factor, count+1) - 1) / (factor - 1))

    return total


# print(sum_of_factors(32))
# print(sum_of_factors(48))
# print(sum_of_factors(70))
# print(sum_of_factors(10000))

TARGET = 36000000
n = 1

# Guessed 1049160 - too high
while True:
    sof = sum_of_factors(n)
    if sof*10 >= TARGET:
        print("Part 1: " + str(n))
        break
    n += 1

