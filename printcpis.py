from Scratch.modpro_aux import *
from Structure.taumodels_list import *
from Structure.modal_functions import *


def test0p(i2, i3, i4, i5, i6, i7, i8):

    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[0]:
                                    for j in K[0]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[0]:
                                            print(i, j, modfun(f2, f3, f4, f5, f6, f7, f8, i, j),modpro(i, j),
                                                  '(',[tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__][modaux(i, j)],')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test1p(i2, i3, i4, i5, i6, i7, i8):

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
                                            print(i, j, modfun(f2, f3, f4, f5, f6, f7, f8, i, j), modpro(i, j),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i, j)], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test2p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[2]:
                                    for j in K[2]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[2]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test3p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[3]:
                                    for j in K[3]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[3]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test4p(i2, i3, i4, i5, i6, i7, i8):

    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[4]:
                                    for j in K[4]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[2], j[2]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[3], j[3])]) not in K[4]:
                                            print(i[0], j[0], i[1], j[1], i[2], j[2], i[3], j[3],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[2], j[2]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[3], j[3]),  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]), modpro(i[2], j[2]), modpro(i[3], j[3]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[2], j[2])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[3], j[3])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test5p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[5]:
                                    for j in K[5]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[5]:
                                            print(i, j, modfun(f2, f3, f4, f5, f6, f7, f8, i, j),
                                                  modpro(i, j),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i, j)], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test6p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[6]:
                                    for j in K[6]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[6]:
                                            print(i, j, modfun(f2, f3, f4, f5, f6, f7, f8, i, j), modpro(i, j),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i, j)], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)





def test7p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[7]:
                                    for j in K[7]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[7]:
                                            print(i, j, modfun(f2, f3, f4, f5, f6, f7, f8, i, j),
                                                  modpro(i, j),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i, j)], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test8p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[8]:
                                    for j in K[8]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[8]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test9p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[9]:
                                    for j in K[9]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[9]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test10p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[10]:
                                    for j in K[10]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[10]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test11p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[11]:
                                    for j in K[11]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[11]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test12p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[12]:
                                    for j in K[12]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[12]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test13p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[13]:
                                    for j in K[13]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[13]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test14p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[14]:
                                    for j in K[14]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[14]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test15p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[15]:
                                    for j in K[15]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[15]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test16p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[16]:
                                    for j in K[16]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[16]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test17p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[17]:
                                    for j in K[17]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[17]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test18p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[18]:
                                    for j in K[18]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[2], j[2])]) not in K[18]:
                                            print(i[0], j[0], i[1], j[1], i[2], j[2],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[2], j[2]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  modpro(i[2], j[2]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[2], j[2])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test19p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[19]:
                                    for j in K[19]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[2], j[2])]) not in K[19]:
                                            print(i[0], j[0], i[1], j[1],i[2], j[2],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[2], j[2]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  modpro(i[2], j[2]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[2], j[2])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test20p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[20]:
                                    for j in K[20]:
                                        if modfun(f2, f3, f4, f5, f6, f7, f8, i, j) not in K[20]:
                                            print(i, j, modfun(f2, f3, f4, f5, f6, f7, f8, i, j),
                                                  modpro(i, j),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i, j)], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test21p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[21]:
                                    for j in K[21]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[21]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]), modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test22p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[22]:
                                    for j in K[22]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[22]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


def test23p(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                for i in K[23]:
                                    for j in K[23]:
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                             modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1])]) not in K[23]:
                                            print(i[0], j[0], i[1], j[1],
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[0], j[0]),
                                                  modfun(f2, f3, f4, f5, f6, f7, f8, i[1], j[1]),
                                                  modpro(i[0], j[0]),
                                                  modpro(i[1], j[1]),
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[0], j[0])], ')',
                                                  '(', [tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                        tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                        tal[i8][0].__name__][modaux(i[1], j[1])], ')',
                                                  tal[i2][0].__name__, tal[i3][0].__name__, tal[i4][0].__name__,
                                                  tal[i5][0].__name__, tal[i6][0].__name__, tal[i7][0].__name__,
                                                  tal[i8][0].__name__)


testp = [test0p, test1p, test2p, test3p, test4p, test5p, test6p, test7p, test8p, test9p, test10p,
    test11p, test12p, test13p, test14p, test15p, test16p, test17p, test18p, test19p, test20p, test21p,
    test22p, test23p]