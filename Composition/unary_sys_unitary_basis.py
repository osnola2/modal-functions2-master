from Composition.gen_sys import *
from Composition.gen_sys_index import *
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

basis = open('one_el_basis_index.txt', 'w+')

b = []
for i1 in un_mod:
    if set(gen_sys_index([i1])) not in b:
                b.append(list(map(lambda x: gen_sys_index([i1]))))
for a in b:
    basis.write(str(a)+','+'\n')


t1 = time.time()
print(t1-t0)
print(len(b))

