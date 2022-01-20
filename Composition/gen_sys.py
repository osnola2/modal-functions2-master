from Composition.from_values_to_functions import *



def gen_sys(base):
    a = []
    for i in base:
        a.append(i)
    for j in a:
        for k in a:
            if val_to_func(list(map(lambda x: j(k(x)), la_2))) not in a:
                a.append(val_to_func(list(map(lambda x: j(k(x)), la_2))))
    return a