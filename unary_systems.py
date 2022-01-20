from Structure.unary_modpro import *

a = []
for i in tau1:
    for j in tau1:
        for m in tau1:
            for n in tau1:
                for k in [0, 6, 9, 1]:
                    if [mod(m, n, mod(i, j, 0)), mod(m, n, mod(i, j, 6)),
                            mod(m, n, mod(i, j, 9)), mod(m, n, mod(i, j, 1))] not in a:
                        a.append([mod(m, n, mod(i, j, 0)), mod(m, n, mod(i, j, 6)),
                                mod(m, n, mod(i, j, 9)), mod(m, n, mod(i, j, 1))])


print(len(a))
print(a)
