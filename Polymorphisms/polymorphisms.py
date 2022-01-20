from Counter_Polimorphisms.candidates import *
from Polymorphisms.pi23 import *
import time

t0 = time.time()
fpi23 = open('fpi23.txt', 'w+')

for i2 in candidate2:
    for i3 in candidate3:
        for i4 in candidate4:
            for i5 in candidate5:
                for i6 in candidate6:
                    for i7 in candidate7:
                        for i8 in candidate8:
                            if pi23(i2, i3, i4, i5, i6, i7, i8):
                                fpi23.write(str(pi23(i2, i3, i4, i5, i6, i7, i8))+'\n')

fpi23.close()

t1 = time.time()
print(t1-t0)




