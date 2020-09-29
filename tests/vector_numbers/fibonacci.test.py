from pyspare import deco_vector

from foba.vectors.vector_numbers.functions.fibonacci import fibonacci


def test():
    vec = fibonacci(10)
    print(deco_vector(vec))


test()
