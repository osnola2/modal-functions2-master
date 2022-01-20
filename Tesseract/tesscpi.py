from Tesseract.tess_modal_functions import *
from Tesseract.tess_taumodels import *


def test24(i1, i2, i3, i4, i5, i6, i7, i8):
    for f1 in tal[i1]:
        for f2 in tal[i2]:
            for f3 in tal[i3]:
                for f4 in tal[i4]:
                    for f5 in tal[i5]:
                        for f6 in tal[i6]:
                            for f7 in tal[i7]:
                                for f8 in tal[i8]:
                                    for i in K[24]:
                                        for j in K[24]:
                                            if modfun(f1, f2, f3, f4, f5, f6, f7, f8, i, j) not in K[24]:
                                                print(i1, i2, i3, i4, i5, i6, i7, i8)