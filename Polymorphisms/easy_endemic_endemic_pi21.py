# This searches for a function described with a same number in four coordinates.
from Polymorphisms.endpi21 import *


a = []
for i in endpi21:
    for j in range(len(i)):
        for k in range(len(i)):
            for m in range(len(i)):
                for n in range(len(i)):
                    if j != k:
                        if j != m:
                            if j != n:
                                if k != m:
                                    if k != n:
                                        if m != n:
                                            if i[j] == i[k]:
                                                if i[k] == i[m]:
                                                    if i[m] == i[n]:
                                                        if i in endpi21:
                                                            if i not in a:
                                                                a.append(i)
print(a)




