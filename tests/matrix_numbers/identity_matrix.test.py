from pyspare import deco_matrix

from foba.matrices.matrix_numbers import identity_matrix


def test():
    mx = identity_matrix(5)
    print(deco_matrix(mx))


test()
