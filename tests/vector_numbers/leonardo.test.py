import leonardo
from pyspare import deco_vector

from foba.vectors.vector_numbers.functions.leonardo import leonardo


def test():
    vec = leonardo(7)
    print(deco_vector(vec))


test()
