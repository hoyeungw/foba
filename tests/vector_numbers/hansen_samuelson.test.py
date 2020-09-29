from pyspare import deco_vector

from foba.vectors.vector_numbers.functions import hansen_samuelson


def test():
    hs_vec = hansen_samuelson(10)
    print(deco_vector(hs_vec))


test()
