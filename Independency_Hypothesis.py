box_sys_profile = {5, 7, 9, 10, 11, 19}
not_cont_false_sys_profile = {0, 2, 8, 10, 12}
cont_true_sys_profile = {1, 2, 9, 10, 13}
fla4_sys_profile = {9, 10, 11, 14, 15, 19}
fla5_sys_profile = {2, 4, 8, 9, 10, 11, 13, 18, 19}
fla6_sys_profile = {10, 6}
fla7_sys_profile = {3, 8, 9, 10, 11, 12, 13, 18, 19}
fla8_sys_profile = {8, 9, 10, 12, 13, 17, 18}
fla9_sys_profile = {21}
fla10_sys_profile = {7, 8, 10, 11, 15, 16, 19, 22} # find
fla11_sys_profile = {24}
fla12_sys_profile = {25}
fla13_sys_profile = {22, 23}
fla14_sys_profile = {20, 22}

sys_profile = [box_sys_profile, not_cont_false_sys_profile, cont_true_sys_profile, fla4_sys_profile, fla5_sys_profile,
               fla6_sys_profile, fla7_sys_profile, fla8_sys_profile, fla9_sys_profile, fla10_sys_profile,
               fla11_sys_profile,
               fla12_sys_profile, fla13_sys_profile, fla14_sys_profile]

a = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25}
c = []

for b in sys_profile:
    c.append(a-b)


def teste(lista, indice):
    i = 0
    v = a
    while i < len(lista):
        if i != indice:
            v = v & lista[i]
        i = i+1
    return v


lista = c

for i in range(14):
    teste(c, i)

    print(i+1, teste(c, i))


