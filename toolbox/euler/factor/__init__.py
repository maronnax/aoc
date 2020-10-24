import collections
import math
from toolbox.euler.primes.sieve import sieve

def factor_number(number):

    prime_factorization = collections.defaultdict(int)
    prime_list = sieve(math.floor(math.sqrt(number)))

    for p in prime_list:
        if number == 1:
            return prime_factorization

        while number%p==0:
            prime_factorization[p] += 1
            number = number // p

    if number != 1:
        prime_factorization[number] += 1

    return prime_factorization


def multiply_factorization(factor):
    num = 1
    for (k,v) in factor.items():
        num *= k**v
    return num


def gcd(*numbers):
    prime_factorizations = list(map(factor_number, numbers))
    prime_factors = set.union(*map(lambda d: set(d.keys()), prime_factorizations))

    gcd_factor = {
    }

    for x in prime_factors:
        factors = [factor[x] for factor in prime_factorizations]
        gcd_factor[x] = min(factors)

    return multiply_factorization(gcd_factor)


def lcm(*numbers):
    prime_factorizations = list(map(factor_number, numbers))
    prime_factors = set.union(*map(lambda d: set(d.keys()), prime_factorizations))

    lcm_factor = {
    }

    for x in prime_factors:
        factors = [factor[x] for factor in prime_factorizations]
        lcm_factor[x] = max(factors)

    return multiply_factorization(lcm_factor)
