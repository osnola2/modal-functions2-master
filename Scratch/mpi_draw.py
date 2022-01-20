from Structure.taumodels import *
from Scratch.Draw_setup import *
from Scratch.modal_profile_draw import *



def mpi_draw(funcs, relation, place):

    matrix_p1 = []
    matrix_p1_aux = []

    for i in range(len(relation)):
        matrix_p1.append((place[0], place[1]+ step_m * i))
        matrix_p1_aux.append(relation[i][0])


    matrix_q1 = []
    matrix_q1_aux = []
    for i in range(len(relation)):
        matrix_q1.append((place[0] + 50, place[1]+ step_m * i))
        matrix_q1_aux.append(relation[i][1])




    print('strokeWeight(', l_stroke, ')')

    for k in range(len(funcs)):
        for i in range(len(matrix_p1_aux)):
            print('if (int(fun) ==', k, '){')
            print('stroke',
                          colors[modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]],
                                        tal[funcs[k][4]], tal[funcs[k][5]], tal[funcs[k][6]],
                                        matrix_p1_aux[i],
                                        matrix_q1_aux[i])])

            print('line', matrix_p1[i] + matrix_q1[i])
            print('}')
            # print('text(', "'", tal[funcs[k][i]].__name__,"'", ',', matrix_p1[i][0]-50, ",", matrix_p1[i][1], ')')



    for i in range(len(relation)):
        print('stroke', colors[relation[i][0]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_p1[i])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][1]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_q1[i])

