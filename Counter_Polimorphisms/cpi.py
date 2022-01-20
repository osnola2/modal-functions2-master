from Counter_Polimorphisms.testcpi import * # Here we filter counter-polymorphisms for all the matrices except for K[21] (or K[23]).
from Counter_Polimorphisms.candidates import *


for i in can:
    test(i[0], i[1], i[2], i[3], i[4], i[5], i[6])