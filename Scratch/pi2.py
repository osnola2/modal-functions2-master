import random as rnd
from supendem_all import *
from special_functions import *

easy_end_pi23 = [[1, 9, 1, 0, 1, 1, 4], [15, 6, 7, 7, 7, 7, 11], [1, 4, 9, 0, 4, 4, 4], [1, 11, 6, 0, 1, 1, 1], [1, 11, 6, 0, 11, 11, 11], [3, 4, 9, 3, 4, 4, 4], [3, 11, 6, 3, 11, 11, 11], [7, 0, 0, 1, 7, 7, 7], [7, 1, 3, 1, 1, 1, 4], [7, 1, 3, 1, 1, 1, 6], [7, 1, 3, 1, 1, 1, 7], [7, 1, 3, 1, 1, 1, 9], [7, 1, 3, 1, 1, 1, 11], [7, 1, 3, 1, 1, 3, 1], [7, 1, 3, 1, 1, 4, 1], [7, 1, 3, 1, 1, 6, 1], [7, 1, 3, 1, 1, 7, 1], [7, 1, 3, 1, 1, 8, 1], [7, 1, 3, 1, 1, 9, 1], [7, 1, 3, 1, 1, 11, 1], [7, 1, 3, 1, 1, 14, 1], [7, 1, 3, 1, 4, 1, 1], [7, 1, 3, 1, 6, 1, 1], [7, 1, 3, 1, 7, 1, 1], [7, 1, 3, 1, 7, 7, 7], [7, 1, 3, 1, 8, 1, 1], [7, 1, 3, 1, 9, 1, 1], [7, 1, 3, 1, 10, 1, 1], [7, 1, 3, 1, 11, 1, 1], [7, 1, 3, 1, 14, 1, 1], [7, 3, 7, 1, 1, 1, 1], [7, 3, 7, 1, 1, 7, 7], [7, 3, 7, 1, 4, 7, 7], [7, 3, 7, 1, 6, 7, 7], [7, 3, 7, 1, 7, 1, 7], [7, 3, 7, 1, 7, 3, 7], [7, 3, 7, 1, 7, 4, 7], [7, 3, 7, 1, 7, 6, 7], [7, 3, 7, 1, 7, 7, 1], [7, 3, 7, 1, 7, 7, 4], [7, 3, 7, 1, 7, 7, 6], [7, 3, 7, 1, 7, 7, 9], [7, 3, 7, 1, 7, 7, 11], [7, 3, 7, 1, 7, 8, 7], [7, 3, 7, 1, 7, 9, 7], [7, 3, 7, 1, 7, 11, 7], [7, 3, 7, 1, 7, 14, 7], [7, 3, 7, 1, 8, 7, 7], [7, 3, 7, 1, 9, 7, 7], [7, 3, 7, 1, 10, 7, 7], [7, 3, 7, 1, 11, 7, 7], [7, 3, 7, 1, 14, 7, 7], [7, 4, 9, 1, 4, 4, 4], [7, 4, 9, 1, 7, 7, 7], [7, 8, 10, 1, 7, 7, 7], [7, 10, 14, 1, 1, 1, 1], [7, 11, 6, 1, 1, 1, 1], [7, 11, 6, 1, 11, 11, 11], [7, 15, 15, 1, 1, 1, 1], [9, 4, 9, 6, 1, 9, 9], [9, 4, 9, 6, 4, 4, 4], [9, 4, 9, 6, 4, 9, 9], [9, 4, 9, 6, 7, 9, 9], [9, 4, 9, 6, 8, 9, 9], [9, 4, 9, 6, 9, 1, 9], [9, 4, 9, 6, 9, 4, 9], [9, 4, 9, 6, 9, 7, 9], [9, 4, 9, 6, 9, 8, 9], [9, 4, 9, 6, 9, 9, 1], [9, 4, 9, 6, 9, 9, 4], [9, 4, 9, 6, 9, 9, 7], [9, 4, 9, 6, 9, 9, 11], [9, 4, 9, 6, 9, 11, 9], [9, 4, 9, 6, 9, 14, 9], [9, 4, 9, 6, 11, 9, 9], [9, 4, 9, 6, 14, 9, 9], [9, 11, 6, 6, 1, 6, 6], [9, 11, 6, 6, 4, 6, 6], [9, 11, 6, 6, 6, 1, 6], [9, 11, 6, 6, 6, 4, 6], [9, 11, 6, 6, 6, 6, 1], [9, 11, 6, 6, 6, 6, 4], [9, 11, 6, 6, 6, 6, 7], [9, 11, 6, 6, 6, 6, 11], [9, 11, 6, 6, 6, 7, 6], [9, 11, 6, 6, 6, 8, 6], [9, 11, 6, 6, 6, 11, 6], [9, 11, 6, 6, 6, 14, 6], [9, 11, 6, 6, 7, 6, 6], [9, 11, 6, 6, 8, 6, 6], [9, 11, 6, 6, 11, 6, 6], [9, 11, 6, 6, 11, 11, 11], [9, 11, 6, 6, 14, 6, 6], [15, 4, 9, 7, 4, 4, 4], [15, 4, 9, 7, 7, 7, 7], [15, 11, 6, 7, 11, 11, 11]]

rand_easy_end_pí23 = []
for i in range(10):
    rand_easy_end_pí23.append(rnd.choice(easy_end_pi23))
# print(sorted(rand_easy_end_pí21))


binary_supen = [supen_1, supen_5, supen_6, supen_10, supen_14, supen_15, supen_16, supen_17, supen_20, supen_21, supen_22, supen_23]



easy_end_pol_21 = [(1, 9, 1, 0, 1, 1, 4), (15, 6, 7, 7, 7, 7, 11)]
proj = [(10,10,10,10,10,10,10), (12,12,12,12,12,12,12)]
sheffer = [[1, 0, 0, 1, 1, 1, 2],
[1, 0, 0, 1, 1, 1, 4],
[1, 0, 0, 1, 1, 1, 6],
[1, 0, 0, 1, 1, 1, 7],
[1, 0, 0, 1, 1, 1, 9],
[1, 0, 0, 1, 1, 1, 11],
[1, 0, 0, 1, 1, 2, 1],
[1, 0, 0, 1, 1, 2, 2],
[1, 0, 0, 1, 1, 2, 4],
[1, 0, 0, 1, 1, 2, 6],
[1, 0, 0, 1, 1, 2, 7],
[1, 0, 0, 1, 1, 2, 9],
[1, 0, 0, 1, 1, 2, 11],
[1, 0, 0, 1, 1, 3, 1],
[1, 0, 0, 1, 1, 3, 2],
[1, 0, 0, 1, 1, 3, 4],
[1, 0, 0, 1, 1, 3, 6],
[1, 0, 0, 1, 1, 3, 7],
[1, 0, 0, 1, 1, 3, 9],
[1, 0, 0, 1, 1, 3, 11],
[1, 0, 0, 1, 1, 4, 1],
[1, 0, 0, 1, 1, 4, 2],
[1, 0, 0, 1, 1, 4, 4],
[1, 0, 0, 1, 1, 4, 6],
[1, 0, 0, 1, 1, 4, 7],
[1, 0, 0, 1, 1, 4, 9],
[1, 0, 0, 1, 1, 4, 11],
[1, 0, 0, 1, 1, 6, 1],
[1, 0, 0, 1, 1, 6, 2],
[1, 0, 0, 1, 1, 6, 4],
[1, 0, 0, 1, 1, 6, 6],
[1, 0, 0, 1, 1, 6, 7],
[1, 0, 0, 1, 1, 6, 9],
[1, 0, 0, 1, 1, 6, 11],
[1, 0, 0, 1, 1, 7, 1],
[1, 0, 0, 1, 1, 7, 2],
[1, 0, 0, 1, 1, 7, 4],
[1, 0, 0, 1, 1, 7, 6],
[1, 0, 0, 1, 1, 7, 7],
[1, 0, 0, 1, 1, 7, 9],
[1, 0, 0, 1, 1, 7, 11],
[1, 0, 0, 1, 1, 8, 1],
[1, 0, 0, 1, 1, 8, 2],
[1, 0, 0, 1, 1, 8, 4],
[1, 0, 0, 1, 1, 8, 6],
[1, 0, 0, 1, 1, 8, 7],
[1, 0, 0, 1, 1, 8, 9],
[1, 0, 0, 1, 1, 8, 11],
[1, 0, 0, 1, 1, 9, 1],
[1, 0, 0, 1, 1, 9, 2],
[1, 0, 0, 1, 1, 9, 4],
[1, 0, 0, 1, 1, 9, 6],
[1, 0, 0, 1, 1, 9, 7],
[1, 0, 0, 1, 1, 9, 9],
[1, 0, 0, 1, 1, 9, 11],
[1, 0, 0, 1, 1, 11, 1],
[1, 0, 0, 1, 1, 11, 2],
[1, 0, 0, 1, 1, 11, 4],
[1, 0, 0, 1, 1, 11, 6],
[1, 0, 0, 1, 1, 11, 7],
[1, 0, 0, 1, 1, 11, 9],
[1, 0, 0, 1, 1, 11, 11],
[1, 0, 0, 1, 1, 14, 1],
[1, 0, 0, 1, 1, 14, 2],
[1, 0, 0, 1, 1, 14, 4],
[1, 0, 0, 1, 1, 14, 6],
[1, 0, 0, 1, 1, 14, 7],
[1, 0, 0, 1, 1, 14, 9],
[1, 0, 0, 1, 1, 14, 11],
[1, 0, 0, 1, 2, 1, 1],
[1, 0, 0, 1, 2, 1, 2],
[1, 0, 0, 1, 2, 1, 4],
[1, 0, 0, 1, 2, 1, 6],
[1, 0, 0, 1, 2, 1, 7],
[1, 0, 0, 1, 2, 1, 9],
[1, 0, 0, 1, 2, 1, 11],
[1, 0, 0, 1, 2, 2, 1],
[1, 0, 0, 1, 2, 2, 2],
[1, 0, 0, 1, 2, 2, 4],
[1, 0, 0, 1, 2, 2, 6],
[1, 0, 0, 1, 2, 2, 7],
[1, 0, 0, 1, 2, 2, 9],
[1, 0, 0, 1, 2, 2, 11],
[1, 0, 0, 1, 2, 3, 1],
[1, 0, 0, 1, 2, 3, 2],
[1, 0, 0, 1, 2, 3, 4],
[1, 0, 0, 1, 2, 3, 6],
[1, 0, 0, 1, 2, 3, 7],
[1, 0, 0, 1, 2, 3, 9],
[1, 0, 0, 1, 2, 3, 11],
[1, 0, 0, 1, 2, 4, 1],
[1, 0, 0, 1, 2, 4, 7],
[1, 0, 0, 1, 2, 6, 1],
[1, 0, 0, 1, 2, 6, 2],
[1, 0, 0, 1, 2, 6, 4],
[1, 0, 0, 1, 2, 6, 6],
[1, 0, 0, 1, 2, 6, 7],
[1, 0, 0, 1, 2, 6, 9],
[1, 0, 0, 1, 2, 6, 11],
[1, 0, 0, 1, 2, 7, 1],
[1, 0, 0, 1, 2, 7, 2],
[1, 0, 0, 1, 2, 7, 4],
[1, 0, 0, 1, 2, 7, 6],
[1, 0, 0, 1, 2, 7, 7],
[1, 0, 0, 1, 2, 7, 9],
[1, 0, 0, 1, 2, 7, 11],
[1, 0, 0, 1, 2, 8, 1],
[1, 0, 0, 1, 2, 8, 7],
[1, 0, 0, 1, 2, 9, 1],
[1, 0, 0, 1, 2, 9, 2],
[1, 0, 0, 1, 2, 9, 4],
[1, 0, 0, 1, 2, 9, 6],
[1, 0, 0, 1, 2, 9, 7],
[1, 0, 0, 1, 2, 9, 9],
[1, 0, 0, 1, 2, 9, 11],
[1, 0, 0, 1, 2, 11, 1],
[1, 0, 0, 1, 2, 11, 2],
[1, 0, 0, 1, 2, 11, 4],
[1, 0, 0, 1, 2, 11, 6],
[1, 0, 0, 1, 2, 11, 7],
[1, 0, 0, 1, 2, 11, 9],
[1, 0, 0, 1, 2, 11, 11],
[1, 0, 0, 1, 2, 14, 1],
[1, 0, 0, 1, 2, 14, 7],
[1, 0, 0, 1, 4, 1, 1],
[1, 0, 0, 1, 4, 1, 2],
[1, 0, 0, 1, 4, 1, 4],
[1, 0, 0, 1, 4, 1, 6],
[1, 0, 0, 1, 4, 1, 7],
[1, 0, 0, 1, 4, 1, 9],
[1, 0, 0, 1, 4, 1, 11],
[1, 0, 0, 1, 4, 2, 1],
[1, 0, 0, 1, 4, 2, 2],
[1, 0, 0, 1, 4, 2, 4],
[1, 0, 0, 1, 4, 2, 6],
[1, 0, 0, 1, 4, 2, 7],
[1, 0, 0, 1, 4, 2, 9],
[1, 0, 0, 1, 4, 2, 11],
[1, 0, 0, 1, 4, 3, 1],
[1, 0, 0, 1, 4, 3, 2],
[1, 0, 0, 1, 4, 3, 4],
[1, 0, 0, 1, 4, 3, 6],
[1, 0, 0, 1, 4, 3, 7],
[1, 0, 0, 1, 4, 3, 9],
[1, 0, 0, 1, 4, 3, 11],
[1, 0, 0, 1, 4, 4, 1],
[1, 0, 0, 1, 4, 4, 2],
[1, 0, 0, 1, 4, 4, 4],
[1, 0, 0, 1, 4, 4, 6],
[1, 0, 0, 1, 4, 4, 7],
[1, 0, 0, 1, 4, 4, 9],
[1, 0, 0, 1, 4, 4, 11],
[1, 0, 0, 1, 4, 6, 1],
[1, 0, 0, 1, 4, 6, 2],
[1, 0, 0, 1, 4, 6, 4],
[1, 0, 0, 1, 4, 6, 6],
[1, 0, 0, 1, 4, 6, 7],
[1, 0, 0, 1, 4, 6, 9],
[1, 0, 0, 1, 4, 6, 11],
[1, 0, 0, 1, 4, 7, 1],
[1, 0, 0, 1, 4, 7, 2],
[1, 0, 0, 1, 4, 7, 4],
[1, 0, 0, 1, 4, 7, 6],
[1, 0, 0, 1, 4, 7, 7],
[1, 0, 0, 1, 4, 7, 9],
[1, 0, 0, 1, 4, 7, 11],
[1, 0, 0, 1, 4, 8, 1],
[1, 0, 0, 1, 4, 8, 2],
[1, 0, 0, 1, 4, 8, 4],
[1, 0, 0, 1, 4, 8, 6],
[1, 0, 0, 1, 4, 8, 7],
[1, 0, 0, 1, 4, 8, 9],
[1, 0, 0, 1, 4, 8, 11],
[1, 0, 0, 1, 4, 9, 1],
[1, 0, 0, 1, 4, 9, 2],
[1, 0, 0, 1, 4, 9, 4],
[1, 0, 0, 1, 4, 9, 6],
[1, 0, 0, 1, 4, 9, 7],
[1, 0, 0, 1, 4, 9, 9],
[1, 0, 0, 1, 4, 9, 11],
[1, 0, 0, 1, 4, 11, 1],
[1, 0, 0, 1, 4, 11, 2],
[1, 0, 0, 1, 4, 11, 4],
[1, 0, 0, 1, 4, 11, 6],
[1, 0, 0, 1, 4, 11, 7],
[1, 0, 0, 1, 4, 11, 9],
[1, 0, 0, 1, 4, 11, 11],
[1, 0, 0, 1, 4, 14, 1],
[1, 0, 0, 1, 4, 14, 2],
[1, 0, 0, 1, 4, 14, 4],
[1, 0, 0, 1, 4, 14, 6],
[1, 0, 0, 1, 4, 14, 7],
[1, 0, 0, 1, 4, 14, 9],
[1, 0, 0, 1, 4, 14, 11],
[1, 0, 0, 1, 6, 1, 1],
[1, 0, 0, 1, 6, 1, 2],
[1, 0, 0, 1, 6, 1, 4],
[1, 0, 0, 1, 6, 1, 6],
[1, 0, 0, 1, 6, 1, 7],
[1, 0, 0, 1, 6, 1, 9]]


multi_type_list = [[1, 0, 0, 1, 1, 1, 2], supendem21]

ind_basis_witness = ((10, 0, 4, 10, 0, 0, 8),
(10, 0, 4, 10, 0, 10, 8),
(10, 0, 4, 10, 0, 15, 8),
(10, 0, 4, 10, 3, 0, 8),
(10, 0, 4, 10, 3, 10, 8),
(10, 0, 4, 10, 3, 15, 8),
(10, 0, 4, 10, 15, 0, 8),
(10, 0, 4, 10, 15, 10, 8),
(10, 0, 4, 10, 15, 15, 8),
(10, 15, 11, 10, 0, 0, 14),
(10, 15, 11, 10, 0, 10, 14),
(10, 15, 11, 10, 0, 15, 14),
(10, 15, 11, 10, 3, 0, 14),
(10, 15, 11, 10, 3, 10, 14),
(10, 15, 11, 10, 3, 15, 14),
(10, 15, 11, 10, 10, 0, 14),
(10, 15, 11, 10, 10, 10, 14),
(10, 15, 11, 10, 10, 15, 14),
(10, 15, 11, 10, 11, 10, 14),
(10, 15, 11, 10, 14, 10, 14),
(10, 15, 11, 10, 15, 0, 14),
(10, 15, 11, 10, 15, 10, 14),
(10, 15, 11, 10, 15, 15, 14)

)