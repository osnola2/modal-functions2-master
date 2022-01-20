from Composition.gen_sys_index import *
from Composition.gen_sys import *

import time

# a = []
#
#
# b = [nec_, imposs_, cont_fal]
#
# for i in b:
#     a.append(i)
#     for j in a:
#         for k in a:
#             if val_to_func(list(map(lambda x: j(k(x)), la_2))) not in a:
#                 a.append(val_to_func(list(map(lambda x: j(k(x)), la_2))))
#
# for i in b:
#     print(i.__name__)
#     print('______________')
# for i in a:
#     print(i.__name__)




t0 = time.time()

basis = open('four_el_basis.txt', 'w+')

b = []
for i1 in un_mod:
    for i2 in un_mod:
        for i3 in un_mod:
            if set(gen_sys([i1, i2, i3])) not in b:
                b.append(set(gen_sys([i1, i2, i3])))

for a in b:
    print(a)

print(len(b))

t1 = time.time()
print(t1-t0)