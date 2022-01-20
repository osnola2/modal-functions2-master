from Composition.from_values_to_functions import *
from Composition.val_to_num import *

def gen_sys_index(base):
    a = []
    b = []
    for i in base:
        a.append(i)
        b.append(val_to_num(list(map(lambda x: i(x), la_2))))
    for j in a:
        for k in a:
            if val_to_func(list(map(lambda x: j(k(x)), la_2))) not in a:
                a.append(val_to_func(list(map(lambda x: j(k(x)), la_2))))
                b.append(val_to_num(list(map(lambda x: j(k(x)), la_2))))
    return b

# print (gen_sys_index([verum1, imp_or_cont_tr]))