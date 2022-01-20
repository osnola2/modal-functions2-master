from Composition.one_esim_graph_1 import *
from Composition.one_esim_graph_2 import *
from Composition.one_esim_graph_3 import *
from Composition.one_esim_graph_4 import *
from Structure.matrices import *

def one_esim_graph(relation):
    if type(relation[0]) == int:
        return one_esim_un(relation)
    if type(relation[0]) == list:
        if len(relation[0]) == 2:
            return one_esim_bin(relation)
    if type(relation[0]) == list:
        if len(relation[0]) == 3:
            return one_esim_ter(relation)
    if type(relation[0]) == list:
        if len(relation[0]) == 4:
            return one_esim_qua(relation)


full = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 6, 9, 0], [0, 6, 9, 1], [0, 9, 6, 0], [0, 9, 6, 1], [0, 1, 1, 0],
            [0, 1, 1, 1], [1, 0, 0, 0], [1, 0, 0, 1], [1, 6, 9, 0], [1, 6, 9, 1], [1, 9, 6, 0], [1, 9, 6, 1],
            [1, 1, 1, 0], [1, 1, 1, 1]]

# a = []
# for i in range(len(K)):
#     if one_esim_graph(K[i])!= full:
#         print(i)
#         print(K[i])
#         for j in range(len(one_esim_graph(K[i]))):
#             print(one_esim_graph(K[i])[j], val_to_func(one_esim_graph(K[i])[j]).__name__)
#
