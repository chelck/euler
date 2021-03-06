#!/usr/bin/env python3

import fractions
import sys


# check that n is in N \{0}.
def is_valid(n):
    if n <= 0:
        return 0
    elif n - int(n) != 0:
        return 0
    return 1


def gcd(x, y):
    while y != 0:
        (x, y) = (y, x % y)
    return x


# The Mobius function .
def mu(n):
    if not is_valid(n):
        return 0
    elif n == 1:
        return 1
    # Important to chech this first .
    elif is_divisible_by_square(n):
        return 0
    else:
        # As n is not divisible by a square ,
        # every power of a prime is equal to one.
        # Hence , the number of factors is correct .
        return (-1) ** number_of_factors(n)


# Check if n is divisible by a square .
def is_divisible_by_square(n):
    i = 2
    while i ** 2 <= n:
        if n % (i ** 2) == 0:
            return 1
        i += 1
    return 0


# Count the number of prime factors of n.
def number_of_factors(n):
    counter = 0
    while n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                n /= i
                counter += 1
                break
            i += 1
    return counter


def find_factors(n):
    factors = []
    while n > 1:
        i = 2
        while i <= n:
            if n % i == 0:
                factors.append(n)
                n //= i
                break
            i += 1
    return factors[:-1]



# The summation of mu(n).
# mu (1)=1 , 0 otherwise .
def sum_of_mu(n):
    d = 1
    mu_sum = 0
    while d <= n:
        if n % d == 0:
            mu_sum += mu(d)
        d += 1
    return mu_sum


# The number of numbers smaller than or
# equal to n which is relatively prime to n
def phi(n):
    if not is_valid(n):
        return 0
    if n == 1:
        return 1
    else:
        print(n)
        for i in range(2, n + 1):
            if (n % i) == 0 and is_prime(i):
                n *= (1 - (1.0 / i))
        return int(n)


def range1(n):
    return range(1, n+1)

def phi2(n):
    amount = 0

    for k in range1(n):
        if fractions.gcd(n, k) == 1:
            amount += 1

    return amount


# Check if a numer is prime or not
def is_prime(n):
    return not (n < 2 or any(n % i == 0 for i in range(2, int(n ** 0.5) + 1)))


# The summation of phi(n).
# The sum over the divisors
# is equal to n.
def sum_of_phi(n):
    d = 1
    phi_sum = 0
    while d <= n:
        if n % d == 0:
            phi_sum += phi(d)
        d += 1
    return phi_sum


def sum_of_phi2(n):
    phi_sum = 0
    for d in range1(n):
        phi_sum += phi2(d)

    return phi_sum


def f(n):
    if n == 1:
        return 1

    return n*n - sum([f(n//k) for k in range(2, n+1)])


def ff(n):
    if n == 1:
        return 1

    sum=0
    for k in range(2,n+1):
        print("  %d -> %d" % (n, n//k))
        sum += ff(n//k)

    return n*n - sum


foo = {}


def mf(n):
    if n == 1:
        return 1

    if n not in foo:
        sum=0
        for k in range(2,n+1):
            sum += mf(n//k)

        foo[n] = n*n - sum

    return foo[n]


def graph(n):
    print('digraph "ff" {')
    ff(n)
    print("}")



def main(argv):


    limit = 10

    count = 0


    goal = 10000000000
    million = 1000000
    m = 10 * million
    m = 10
    #for n in range(m, m+5):
    #    print("f(%d) => %d" % (n, f(n)))

    print()

    for n in range(m, m+1):
        print("f(%d) => %d" % (n, mf(n)))

    print(len(foo))






if __name__ == "__main__":
    main(sys.argv)
