from special_functions import *


def supen_0(prop1, prop2, prop3):
    return eq(conj(prop1, prop2), neg(diam(prop3)))


def supen_1(prop1, prop2):
    return eq(imp(prop1, prop2), rigid(prop2))


def two_three(prop1, prop2, prop3):
    return disj(disj(conj(prop1, prop2), conj(prop1, prop3)), conj(prop2, prop3))


def supen_2(prop1, prop2, prop3):
    return neg(two_three(prop1, prop2, box(prop3)))


def supen_5(prop1, prop2):
    return eq(neg(disj(prop1, prop2)), disj(rigid(prop1), rigid(prop2)))


def supen_6(prop1, prop2):
    return conj(imp(conj(diam(prop1), diam(prop2)), disj(conj(prop1, prop2), box(eq(prop1, prop2)))), neg(box(conj(prop1, prop2))))


def supen_7(prop1, prop2, prop3):
    return imp(disj(prop1, rigid(prop2)), conj(neg(conj(prop1, prop3)), rigid(prop2)))


def supen_8(prop1, prop2, prop3):
    return imp(box(prop1), conj(disj(prop2, eq(prop3, rigid(prop3))), neg(box(eq(prop2, prop3)))))


def supen_9(prop1, prop2, prop3):
    return conj(disj(conj(prop1, eq(prop2, rigid(prop2))), box(eq(prop1, prop2))), neg(diam(prop3)))


def supen_10(prop1, prop2):
    return neg(conj(prop1, prop2))


def supen_14(prop1, prop2):
    return conj(conj(imp(prop1, box(prop1)), imp(diam(prop2), prop2)), neg(box(conj(prop1, prop2))))


def supen_15a(prop1, prop2):
    return imp(disj(disj(prop1, prop2), conj(diam(prop1), diam(prop2))), disj(conj(prop1, prop2), box(eq(prop1, prop2))))


def supen_15(prop1, prop2):
    return conj(supen_15a(prop1, prop2), neg(box(conj(prop1, prop2))))


def supen_16(prop1, prop2):
    return conj(conj(neg(prop1), imp(diam(prop2), prop2)), neg(box(disj(prop1, prop2))))


def supen_17(prop1, prop2):
    return conj(disj(imp(diam(prop1), prop1), eq(prop2, rigid(prop2))), imp(prop1, neg(box(prop2))))


def supen_20a(prop1, prop2):
    return imp(phi(prop1, prop2), conj(imp(prop1, prop2), neg(box(prop2))))


def supen_20b(prop1, prop2):
    return phi(prop1, prop2)


def supen_20c(prop1, prop2):
    return imp(imp(imp(prop1, neg(ind(prop1, prop2))), prop2), S(prop1, prop2))


def supen_20(prop1, prop2):
    return conj(supen_20a(prop1, prop2), disj(supen_20b(prop1, prop2), supen_20c(prop1, prop2)))


def supen_21a(prop1, prop2):
    return disj(phi(prop1, prop2), conj(eq(prop1, S(prop1, prop2)), imp(prop2, S(prop1, prop2))))


def supen_21(prop1, prop2):
    return conj(supen_20a(prop1, prop2), supen_21a(prop1, prop2))


def supen_22(prop1, prop2):
    return conj(conj(neg(box(prop1)), eq(prop1, prop2)), neg(ind(prop1, prop2)))


def supen_23a(prop1, prop2):
    return imp(phi(prop1, prop2), conj(imp(prop1, prop2), neg(box(prop2))))


def supen_23b(prop1, prop2):
    return disj(disj(prop1, prop2), S(prop1, prop2))


def supen_23c(prop1, prop2):
    return disj(conj(prop1, prop2), S(neg(prop1), neg(prop2)))


def supen_23(prop1, prop2):
    return conj(conj(supen_23a(prop1, prop2), supen_23b(prop1, prop2)), supen_23c(prop1, prop2))