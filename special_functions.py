from Structure.binary_functions import *

def S(prop1, prop2):
    return disj(box(disj(prop1, prop2)), disj(box(imp(prop1,prop2)), box(cimp(prop1, prop2))))


def phi(prop1, prop2):
    return conj(conj(S(prop1, prop2), S(prop1, neg(prop2))), conj(S(neg(prop1), prop2),S(neg(prop1), neg(prop2))))


def endem0(prop1, prop2):
    return(eq(conj(prop1, prop2), neg(diam(prop2))))


def supendem21a(prop1, prop2):
    return imp(phi(prop1, prop2), conj(imp(prop1, prop2), neg(box(prop2))))


def supendem21b(prop1, prop2):

    return disj(phi(prop1, prop2), conj(eq(prop1, S(prop1, prop2)), imp(prop2, S(prop1, prop2))))


def supendem21(prop1, prop2):
    return conj(supendem21a(prop1, prop2), supendem21b(prop1, prop2))


def supendem23a(prop1, prop2):
    return imp(phi(prop1, prop2), conj(imp(prop1, prop2), neg(box(prop2))))


def supendem23b(prop1, prop2):
    return disj(disj(prop1, prop2), S(prop1, prop2))


def supendem23c(prop1, prop2):
    return disj(conj(prop1, prop2), S(neg(prop1), neg(prop2)))


def supendem23(prop1, prop2):
    return conj(conj(supendem23a(prop1, prop2), supendem23b(prop1, prop2)), supendem23c(prop1, prop2))


def not_cont_false(prop1):
    return neg(conj(conj(diam(prop1), diam(neg(prop1))), neg(prop1)))


def cont_true(prop1):
    return conj(conj(diam(prop1), diam(neg(prop1))), prop1)


def fla1(prop1):
    return(box(prop1))


def fla2(prop1):
    return not_cont_false(prop1)


def fla3(prop1):
    return cont_true(prop1)


def fla4(prop1, prop2):
    return conj(prop1, disj(box(prop1), diam(prop2)))


def fla5(prop1, prop2):
    return conj(prop1, imp(box(prop1), diam(prop2)))


def rigid(prop1):
    return disj(box(prop1), box(neg(prop1)))

def cont(prop1):
    return neg(rigid(prop1))

def fla6(prop1, prop2):
    return eq(prop1, imp(rigid(prop2), rigid(prop1)))


def fla7(prop1, prop2, prop3):
    return eq(prop1, imp(rigid(prop1), eq(box(prop2), box(prop3))))


def fla8(prop1, prop2):
    return imp(imp(prop1, imp(rigid(prop2), rigid(prop1))), conj(prop2, imp(rigid(prop2), rigid(prop1))))


def fla9(prop1, prop2):
    return imp(phi(prop1, prop2), prop2)


def fla10(prop1, prop2, prop3):
    return imp(imp(prop1, rigid(prop3)), conj(diam(prop1), conj(box(disj(prop1, prop2)), rigid(prop3))))


def ind(prop1, prop2):
    return conj(conj(diam(conj(prop1, prop2)), diam(conj(prop1, neg(prop2)))), conj(diam(conj(neg(prop1), prop2)), diam(conj(neg(prop1), neg(prop2)))))


def fla11(prop1, prop2, prop3):
    return eq(imp(eq(prop1, prop2), neg(ind(prop1, prop2))), prop3)


def fla12a(prop1, prop2, prop3):
    return disj(disj(disj(prop1, prop2), disj(prop3, box(imp(prop1, prop2)))), disj(box(imp(prop2, prop3)),
                                                                                    box(imp(prop3, prop1))))


def fla12(prop1, prop2, prop3):
    return imp(imp(fla12a(prop1, prop2, prop3), neg(ind(prop1, prop2))), prop3)


def fla13a(prop1, prop2):
    return conj(disj(prop1, S(prop1, prop2)), imp(prop1, S(prop1, neg(prop2))))


def fla13b(prop1, prop2):
    return conj(disj(prop2, conj(S(neg(prop1), prop2), S(neg(prop1), neg(prop2)))), imp(phi(prop1, prop2), prop2))


def fla13(prop1, prop2):
    return conj(fla13a(prop1, prop2), fla13b(prop1, prop2))


def fla14a(prop1, prop2):
    return imp(disj(prop1, prop2), S(prop1, prop2))


def fla14b(prop1, prop2):
    return imp(imp(prop1, prop2), S(neg(prop1), prop2))


def fla14c(prop1, prop2):
    return disj(imp(prop2, prop1), S(prop1, neg(prop2)))


def fla14d(prop1, prop2):
    return imp(conj(prop1, prop2), S(neg(prop1), neg(prop2)))


def fla14e(prop1, prop2):
    return imp(phi(prop1, prop2), prop2)


def fla14(prop1, prop2):
    return conj(fla14a,(conj(fla14b,(conj(fla14c, (conj(fla14d, fla14e)))))))


def fla10_new_a(prop1, prop2):
    return disj(conj(box(eq(prop1, prop2)), prop1), conj(box(prop1), neg(diam(prop2))))


def fla10_new_b(prop1, prop2):
    return conj(conj(conj(conj(cont(prop1), cont(prop2)), diam(eq(prop1, prop2))),
                disj(box(disj(prop1, prop2)), neg(diam(conj(prop1, prop2))))), prop2)


def fla10_new(prop1, prop2):
    return disj(fla10_new_a(prop1, prop2), fla10_new_b(prop1, prop2))


def fla10_alt(prop1, prop2):
    return disj(disj(box(prop1), conj(prop1, box(eq(prop1, prop2)))), conj(conj(cont(prop1), cont_true(prop2)),
            xor(diam(conj(prop1, prop2)), diam(conj(neg(prop1), neg(prop2))))))



# spec_fun = [fla4, fla5, fla6, fla8, fla9, fla13, fla14]
# spec_fun_1 = [fla1, fla2, fla3]
# spec_fun_3 = [fla7, fla10, fla11, fla12]



spec_fun = []
spec_fun_1 = []
spec_fun_3 = []











# for i in K[21]:
#     for j in K[21]:
#         if [supendem21(i[0], j[0]), supendem21(i[1], j[1])] not in K[21]:
#             print(i[0], j[0], i[1], j[1], supendem21(i[0], j[0]), supendem21(i[1], j[1]))
#
# # def supen23a(prop1, prop2):
#     return imp(phi(prop1, prop2), conj(imp(prop1, prop2), neg(box(prop2))))
#
#
# def supen23b(prop1, prop2):
#     return conj(disj(prop1, disj(prop2, S(prop1, prop2))), disj(conj(prop1, prop2), S(neg(prop1), neg(prop2))))
#
#
# def supen23(prop1, prop2):
#     return conj(supen23a(prop1, prop2), supen23b(prop1, prop2))
#
#
# for i in K[23]:
#     for j in K[23]:
#         if [supen23(i[0], j[0]), supen23(i[1], j[1])] not in K[21]:
#             print(i[0], j[0], i[1], j[1], supen23(i[0], j[0]), supen23(i[1], j[1]))

# spec_fun = [fla4, fla5, fla6, fla8, fla9, eq, phi]
# spec_fun_1 = [box, not_cont_false, cont_true, neg]
# spec_fun_3 = [fla7, fla10, fla11, fla12]

