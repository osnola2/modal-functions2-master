from Composition.unary_moody import *


def val_to_func(seq):
    if seq == [1, 1, 1, 1]:
        return verum_
    if seq == [0, 1, 1, 1]:
        return poss_
    if seq == [1, 1, 1, 0]:
        return not_nec_
    if seq == [0, 1, 1, 0]:
        return cont_
    if seq == [1, 6, 9, 1]:
        return not_cont_fal
    if seq == [0, 6, 9, 1]:
        return id_
    if seq == [1, 6, 9, 0]:
        return imp_or_cont_tr
    if seq == [0, 6, 9, 0]:
        return cont_tr
    if seq == [1, 9, 6, 1]:
        return not_cont_tr
    if seq == [0, 9, 6, 1]:
        return nec_or_cont_fal
    if seq == [1, 9, 6, 0]:
        return neg_
    if seq == [0, 9, 6, 0]:
        return cont_fal
    if seq == [1, 0, 0, 1]:
        return rigid_
    if seq == [0, 0, 0, 1]:
        return nec_
    if seq == [1, 0, 0, 0]:
        return imposs_
    if seq == [0, 0, 0, 0]:
        return falsum_

