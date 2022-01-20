from Polymorphisms.endemic_pi23 import *

# esse código procura 4 coordenadas idênticas dentre os ìndices  dos polimorfismos endêmicos de pi23 (4 só porque
# j, k, m, n são quatro).

for i in endpi23:
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
                                                        print(i)