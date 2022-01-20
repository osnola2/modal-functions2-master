from Structure.basic_functions import *


def pr1(prop1):
    return prop1

la_2 = (0, 6, 9, 1)

tau1 = (falsum1, neg, pr1, verum1)


def unary_modal(f1, f2, prop1):
    if prop1 in (0, 1):
        return f2(prop1)
    else:
        return f1(prop1)


def verum_(prop1):
    return unary_modal(verum1, verum1, prop1)


def poss_(prop1):
    return unary_modal(verum1, pr1, prop1)


def not_nec_(prop1):
    return unary_modal(verum1, neg, prop1)


def cont_(prop1):
    return unary_modal(verum1, falsum1, prop1)


def not_cont_fal(prop1):
    return unary_modal(pr1, verum1, prop1)


def id_(prop1):
    return unary_modal(pr1, pr1, prop1)


def imp_or_cont_tr(prop1):
    return unary_modal(pr1, neg, prop1)


def cont_tr(prop1):
    return unary_modal(pr1, falsum1, prop1)


def not_cont_tr(prop1):
    return unary_modal(neg, verum1, prop1)


def nec_or_cont_fal(prop1):
    return unary_modal(neg, pr1, prop1)


def neg_(prop1):
    return unary_modal(neg, neg, prop1)


def cont_fal(prop1):
    return unary_modal(neg, falsum1, prop1)


def rigid_(prop1):
    return unary_modal(falsum1, verum1, prop1)


def nec_(prop1):
    return unary_modal(falsum1, pr1, prop1)


def imposs_(prop1):
    return unary_modal(falsum1, neg, prop1)


def falsum_(prop1):
    return unary_modal(falsum1, falsum1, prop1)




un_mod = (falsum_, imposs_, nec_,
          rigid_, cont_fal, neg_, nec_or_cont_fal,
          not_cont_tr, cont_tr, imp_or_cont_tr, id_,
          not_cont_fal, cont_, not_nec_, poss_, verum_)