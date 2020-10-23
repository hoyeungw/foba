from pyspare import deco_vector

from foba.vectors.vector_numbers.functions import compound_interest


def test():
    vec = compound_interest(20, 0.08, 3)
    print(deco_vector(vec))


test()
