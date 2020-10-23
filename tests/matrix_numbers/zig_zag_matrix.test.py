from pyspare import deco_matrix

from foba.matrices.matrix_numbers import zig_zag_matrix


def test():
    mx = zig_zag_matrix(5)
    print(mx)
    print(deco_matrix(mx))


test()
