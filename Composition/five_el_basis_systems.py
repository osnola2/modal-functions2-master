from Composition.gen_sys_index import *
from Composition.gen_sys import *
import time


t0 = time.time()

basis = open('five_el_basis_systems.txt', 'w+')
basis_code = open('five_el_basis_systems_code.txt', 'w+')
c = []
d = []

for i1 in un_mod:
    for i2 in un_mod:
        for i3 in un_mod:
            for i4 in un_mod:
                for i5 in un_mod:
                    if set(gen_sys([i1, i2, i3, i4, i5])) not in c:
                        c.append(set(gen_sys([i1, i2, i3, i4, i5])))
                        d.append(set(gen_sys_index([i1, i2, i3, i4, i5])))

for i in range(len(c)):
    print(c[i], d[i])




for a in c:
    basis.write(str(a)+','+'\n')

for a in d:
    basis_code.write(str(a)+','+'\n')



t1 = time.time()
print(t1-t0)
print(len(c))
