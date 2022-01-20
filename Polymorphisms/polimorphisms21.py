from Polymorphisms.pi21 import *
from Counter_Polimorphisms.candidates import *

fpi21 = open('fpi21.txt', 'w+')

for i2 in candidate2:
    for i3 in candidate3:
        for i4 in candidate4:
            for i5 in candidate5:
                for i6 in candidate6:
                    for i7 in candidate7:
                        for i8 in candidate8:
                            if pi21(i2, i3, i4, i5, i6, i7, i8) != None:
                                fpi21.write(str(pi21(i2, i3, i4, i5, i6, i7, i8))+'\n')

fpi21.close()
