from pyspare import deco_matrix

from foba.matrices.matrix_numbers import lower_pascal_matrix, symmetric_pascal_matrix, \
    upper_pascal_matrix


def test():
    mx = upper_pascal_matrix(5)
    print(mx)
    print(deco_matrix(mx))

    mx = lower_pascal_matrix(5)
    print(mx)
    print(deco_matrix(mx))

    mx = symmetric_pascal_matrix(5)
    print(mx)
    print(deco_matrix(mx))


test()
