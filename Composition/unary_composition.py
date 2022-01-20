from Composition.unary_moody import *
from Composition.from_values_to_functions import *
from Composition.val_to_num import *

for i in un_mod:
    for j in un_mod:
        print(i.__name__, '*', j.__name__, '=', val_to_func(list(map(lambda x: i(j(x)), la_2))).__name__)


for i in un_mod:
    print('if seq ==', list(map(lambda x: i(x), la_2)), ':')
    print('return', i.__name__)




