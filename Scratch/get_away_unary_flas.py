from Structure.modal_functions import *
from Structure.taumodels import *
from Scratch.Draw_setup import *


def get_away_unary(funcs, relation, place):

    matrix_place = place
    matrix_p1 = []
    matrix_p1_aux = []
    for i in range(len(relation)):
        matrix_p1.append((matrix_place[0] + step_m * i, matrix_place[1]))
        matrix_p1_aux.append(relation[i])


    matrix_q1 = []
    matrix_q1_aux = []
    for i in range(len(relation)):
        matrix_q1.append((matrix_place[0] + step_m * i + step_m * (len(relation) + 4), matrix_place[1]))
        matrix_q1_aux.append(relation[i])


    for i in range(len(relation)):
        print('stroke', colors[relation[i]])
        print('strokeWeight(', p_stroke,')')
        print('point', matrix_p1[i])


    for i in range(len(relation)):
        print('stroke', colors[relation[i]])
        print('strokeWeight(', p_stroke,')')
        print('point', matrix_q1[i])


    print('strokeWeight(', l_stroke, ')')

    for k in range(len(funcs)):
        get_away = []
        for i in range(len(matrix_p1_aux)):
            for j in range(len(matrix_q1_aux)):
                if funcs[k](matrix_p1_aux[i], matrix_q1_aux[j]) not in relation:
                    if len(get_away) < 1:
                        get_away.append([i, j])
                        print('if (int(fun) ==', k, '){')
                        print('stroke', colors[funcs[k](matrix_p1_aux[get_away[0][0]], matrix_q1_aux[get_away[0][1]])])
                        print('line', matrix_p1[get_away[0][0]] + matrix_q1[get_away[0][1]])
                        print('}')
