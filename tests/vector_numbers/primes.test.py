from pyspare import deco_vector

from foba.vectors.vector_numbers.functions.primes import primes


def test():
    vec = primes(10)
    print(deco_vector(vec))


test()
