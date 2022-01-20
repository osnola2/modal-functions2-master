from Composition.unary_moody import *
from Structure.binary_functions import *
from Structure.matrices import *
from Composition.from_values_to_functions import *

def one_esim_un(relation):
    full = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 6, 9, 0], [0, 6, 9, 1], [0, 9, 6, 0], [0, 9, 6, 1], [0, 1, 1, 0],
            [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 6, 9, 0], [1, 6, 9, 1], [1, 9, 6, 0], [1, 9, 6, 1],
            [1, 1, 1, 0], [1, 1, 1, 1]]
    a = []
    for i in un_mod:
        for j in relation:
            if i(j) not in relation:
                if list(map(lambda x: i(x), la_2)) not in a:
                    a.append(list(map(lambda x: i(x), la_2)))

    b = []
    for i in a:
        b.append(list(map(lambda x : 2 if x == 0 else 3 if x == 6 else 4 if x == 9 else 5 if x == 1 else False, i)))

    c = []
    for i in sorted(b):
        c.append(list(map(lambda x : 0 if x == 2 else 6 if x == 3 else 9 if x == 4 else 1 if x == 5 else False, i)))
    d = []
    for i in full:
        if i not in c:
            d.append(i)
    return d


# for i in K:
#     if type(i[0]) == int:
#         print(i, one_esim_un(i))
#         print(i, list(map(lambda x: val_to_func(x).__name__, one_esim_un(i))))
# # #
# for x in a:
#     print(x, val_to_func(x))
#     print(sorted(a))
# print(sorted(b))
# print(c)