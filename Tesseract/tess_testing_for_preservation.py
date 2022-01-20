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
                                                return i1, i2, i3, i4, i5, i6, i7, i8


# for i1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
#     for i2 in [3]:
#         for i3 in [2]:
#             for i4 in [4]:
#                 for i5 in [6]:
#                     for i6 in [1]:
#                         for i7 in [1]:
#                             for i8 in [1]:
#                                 print(i1, test24(i1, i2, i3, i4, i5, i6, i7, i8))

def test25(i1, i2, i3, i4, i5, i6, i7, i8):
    for f1 in tal[i1]:
        for f2 in tal[i2]:
            for f3 in tal[i3]:
                for f4 in tal[i4]:
                    for f5 in tal[i5]:
                        for f6 in tal[i6]:
                            for f7 in tal[i7]:
                                for f8 in tal[i8]:
                                    for i in K[25]:
                                        for j in K[25]:
                                            if modfun(f1, f2, f3, f4, f5, f6, f7, f8, i, j) not in K[25]:
                                                return i1, i2, i3, i4, i5, i6, i7, i8


for i1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
    for i2 in [9]:
        for i3 in [0]:
            for i4 in [0]:
                for i5 in [0]:
                    for i6 in [1]:
                        for i7 in [2]:
                            for i8 in [1]:
                                print(tal[i1], test25(i1, i2, i3, i4, i5, i6, i7, i8))


def test21(i1, i2, i3, i4, i5, i6, i7, i8):
    for f1 in tal[i1]:
        for f2 in tal[i2]:
            for f3 in tal[i3]:
                for f4 in tal[i4]:
                    for f5 in tal[i5]:
                        for f6 in tal[i6]:
                            for f7 in tal[i7]:
                                for f8 in tal[i8]:
                                    for i in K[21]:
                                        for j in K[21]:
                                            if [modfun(f1, f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                modfun(f1, f2, f3, f4, f5, f6, f7, f8, i[1], j[1])] not in K[21]:
                                                return i2, i3, i4, i5, i6, i7, i8

# for i in K[21]:
#     for j in K[21]:
#         print(i[0], j[0], i[1], j[1], modpro(i[0], j[0]), modpro(i[1], j[1]))



# for i1 in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]:
#     for i2 in [3]:
#         for i3 in [2]:
#             for i4 in [4]:
#                 for i5 in [6]:
#                     for i6 in [1]:
#                         for i7 in [1]:
#                             for i8 in [1]:
#                                 print(i1, test21(i1, i2, i3, i4, i5, i6, i7, i8))