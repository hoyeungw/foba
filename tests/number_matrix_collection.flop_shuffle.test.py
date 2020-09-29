from pyspare import deco_matrix, deco_str

from foba.matrices import number_matrix_collection

k, mx = number_matrix_collection.flop_shuffle(length=7)

print(deco_str(k), deco_matrix(mx))
