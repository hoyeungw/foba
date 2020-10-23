from pyspare import deco_vector

from foba.vectors.vector_numbers.functions import absolute_mirror


def test():
    vec = absolute_mirror(10)
    print(deco_vector(vec))


test()
