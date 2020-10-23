from pyspare import deco_matrix, deco_str

from foba.matrices import string_matrix_collection

k, mx = string_matrix_collection.flop_shuffle(length=7)
print(mx)
print(deco_str(k), deco_matrix(mx))
