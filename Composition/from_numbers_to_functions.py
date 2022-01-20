from Composition.unary_moody import *


def num_to_func(num):
    if num == 15:
        return verum_
    if num == 14:
        return poss_
    if num == 13:
        return not_nec_
    if num == 12:
        return cont_
    if num == 11:
        return not_cont_fal
    if num == 10:
        return id_
    if num == 9:
        return imp_or_cont_tr
    if num == 8:
        return cont_tr
    if num == 7:
        return not_cont_tr
    if num == 6:
        return nec_or_cont_fal
    if num == 5:
        return neg_
    if num == 4:
        return cont_fal
    if num == 3:
        return rigid_
    if num == 2:
        return nec_
    if num == 1:
        return imposs_
    if num == 0:
        return falsum_

