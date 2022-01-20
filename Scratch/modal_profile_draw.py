from Structure.modal_functions import *

LA_1 = (0, 1)
LA_2 = (0, 6, 9, 1)
LA_3 = atoms

algebras = (LA_1, LA_2, LA_3)

mp =[[[0, 0, 0, 1], [1, 1, 1, 0]],
 [[0, 0, 1, 0], [1, 1, 0, 1]],
 [[0, 1, 0, 0], [1, 0, 1, 1]],
 [[1, 0, 0, 0], [0, 1, 1, 1]],
 [[0, 0, 1, 1], [1, 1, 0, 0]],
 [[0, 1, 0, 1], [1, 0, 1, 0]],
 [[1, 0, 0, 1], [0, 1, 1, 0]]]


mpi_aux = [[[], [], [], [],[], [], []], [[], [], [], [], [], [], []], [[], [], [], [],[], [], []]]

for k in range(len(mp)):
    for m in range(len(algebras)):
        for i in algebras[m]:
            for j in algebras[m]:
                if modpro(i, j) == mp[k][0] or modpro(i, j) == mp[k][1]:
                    mpi_aux[m][k].append([i, j])

for k in range(len(mpi_aux)):
    print(mpi_aux[k])

mpi = mpi_aux[1]