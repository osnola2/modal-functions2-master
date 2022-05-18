from Sheffer_Functions.test_sheffer import *
from Counter_Polimorphisms.candidates import *
import time

t0 = time.time()

shef_complete = open('Shef_complete_test_1.txt', 'w+')

for i2 in candidate2:
    for i3 in candidate3:
        for i4 in candidate4:
            for i5 in candidate5:
                for i6 in candidate6:
                    for i7 in candidate7:
                        for i8 in candidate8:
                            if testsheffer(i2, i3, i4, i5, i6, i7, i8) is not None:
                                shef_complete.write(str(testsheffer(i2, i3, i4, i5, i6, i7, i8))+'\n')

shef_complete.close()
t1 = time.time()

print(t1-t0)






