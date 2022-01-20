from Structure.taumodels_list import *
from Structure.modal_functions import *


def pi23a(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 0, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 0, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 0, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 0, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 0, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 0, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 0, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 0, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 0, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23b(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 9, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 9, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 9, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 9, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 9, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 9, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 9, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 6, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 9, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23c(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 5, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 5, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 5, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 5, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 5, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 5, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 5, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 2, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 5, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23d(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 4, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 4, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 4, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 4, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 4, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 4, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 4, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 3, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 4, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23e(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 2, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 2, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 2, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 2, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 2, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 2, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 2, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 5, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 2, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23f(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 3, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 3, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 3, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 3, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 3, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 3, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 3, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 4, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 3, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23g(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 6, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 6, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 6, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 6, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 6, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 6, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 6, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 9, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 6, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23h(i2, i3, i4, i5, i6, i7, i8):
    for f2 in tal[i2]:
        for f3 in tal[i3]:
            for f4 in tal[i4]:
                for f5 in tal[i5]:
                    for f6 in tal[i6]:
                        for f7 in tal[i7]:
                            for f8 in tal[i8]:
                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 0),
                                        modfun(f2, f3, f4, f5, f6, f7, f8, 1, 0)]) in K[23]:
                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 6),
                                         modfun(f2, f3, f4, f5, f6, f7, f8, 1, 9)] in K[23]):
                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 2),
                                                modfun(f2, f3, f4, f5, f6, f7, f8, 1, 5)]) in K[23]:
                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 3),
                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 1, 4)]) in K[23]:
                                                if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 5),
                                                     modfun(f2, f3, f4, f5, f6, f7, f8, 1, 2)]) in K[23]:
                                                    if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 4),
                                                         modfun(f2, f3, f4, f5, f6, f7, f8, 1, 3)]) in K[23]:
                                                        if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 9),
                                                             modfun(f2, f3, f4, f5, f6, f7, f8, 1, 6)]) in K[23]:
                                                            if ([modfun(f2, f3, f4, f5, f6, f7, f8, 1, 1),
                                                                 modfun(f2, f3, f4, f5, f6, f7, f8, 1, 1)]) in K[23]:
                                                                return i2, i3, i4, i5, i6, i7, i8


def pi23(i2,i3, i4, i5, i6, i7, i8):
    if pi23a(i2, i3, i4, i5, i6, i7, i8):
        if pi23b(i2, i3, i4, i5, i6, i7, i8):
            if pi23c(i2, i3, i4, i5, i6, i7, i8):
                if pi23d(i2, i3, i4, i5, i6, i7, i8):
                    if pi23e(i2, i3, i4, i5, i6, i7, i8):
                        if pi23f(i2, i3, i4, i5, i6, i7, i8):
                            if pi23g(i2, i3, i4, i5, i6, i7, i8):
                                return pi23h(i2, i3, i4, i5, i6, i7, i8)