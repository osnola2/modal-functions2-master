from Structure.taumodels_list import *
from Structure.modal_functions import *

#  this returns a modal function (or better the 7-tuple describing it) if it doesn't preserves (that is the same as
#  being a counter-polymorphism) K[1].


def test1(i2, i3, i4, i5, i6, i7, i8):

    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[1]:
                                    for j in K[1]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[1]:
                                            return i2, i3, i4, i5, i6, i7, i8
