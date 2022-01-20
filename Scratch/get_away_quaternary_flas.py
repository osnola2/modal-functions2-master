from Structure.modal_functions import *
from Structure.taumodels import *
from Scratch.Draw_setup import *


def get_away_quaternary(funcs, relation, place):

    matrix_place = place

    matrix_p1 = []
    matrix_p1_aux = []
    for i in range(len(relation)):
        matrix_p1.append((matrix_place[0] + step_m * i, matrix_place[1]))
        matrix_p1_aux.append(relation[i][0])

    matrix_p2 = []
    matrix_p2_aux = []
    for i in range(len(relation)):
        matrix_p2.append((matrix_place[0] + step_m * i, matrix_place[1] + step_m))
        matrix_p2_aux.append(relation[i][1])

    matrix_p3 = []
    matrix_p3_aux = []
    for i in range(len(relation)):
        matrix_p3.append((matrix_place[0] + step_m * i, matrix_place[1] + step_m*2))
        matrix_p3_aux.append(relation[i][2])

    matrix_p4 = []
    matrix_p4_aux = []
    for i in range(len(relation)):
        matrix_p4.append((matrix_place[0] + step_m * i, matrix_place[1] + step_m*3))
        matrix_p4_aux.append(relation[i][3])

    matrix_q1 = []
    matrix_q1_aux = []
    for i in range(len(relation)):
        matrix_q1.append((matrix_place[0] + step_m * i + step_m * (len(relation) + 4), matrix_place[1]))
        matrix_q1_aux.append(relation[i][0])

    matrix_q2 = []
    matrix_q2_aux = []
    for i in range(len(relation)):
        matrix_q2.append((matrix_place[0] + step_m * i + step_m * (len(relation) + 4), matrix_place[1] + step_m))
        matrix_q2_aux.append(relation[i][1])

    matrix_q3 = []
    matrix_q3_aux = []
    for i in range(len(relation)):
        matrix_q3.append((matrix_place[0] + step_m * i + step_m * (len(relation) + 4), matrix_place[1] + step_m*2))
        matrix_q3_aux.append(relation[i][2])

    matrix_q4 = []
    matrix_q4_aux = []
    for i in range(len(relation)):
        matrix_q4.append((matrix_place[0] + step_m * i + step_m * (len(relation) + 4), matrix_place[1] + step_m*3))
        matrix_q4_aux.append(relation[i][3])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][0]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_p1[i])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][1]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_p2[i])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][2]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_p3[i])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][3]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_p4[i])


    for i in range(len(relation)):
        print('stroke', colors[relation[i][0]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_q1[i])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][1]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_q2[i])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][2]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_q3[i])

    for i in range(len(relation)):
        print('stroke', colors[relation[i][3]])
        print('strokeWeight(', p_stroke, ')')
        print('point', matrix_q4[i])


    print('strokeWeight(', l_stroke, ')')

    for k in range(len(funcs)):
        get_away = []
        for i in range(len(matrix_p1_aux)):
            for j in range(len(matrix_q1_aux)):
                if [funcs[k](matrix_p1_aux[i], matrix_q1_aux[j]),
                    funcs[k](matrix_p2_aux[i], matrix_q2_aux[j]),
                    funcs[k](matrix_p3_aux[i], matrix_q3_aux[j]),
                    funcs[k](matrix_p4_aux[i], matrix_q4_aux[j])] not in relation:
                    if len(get_away) < 1:
                        get_away.append([i, j])
                        print('if (int(fun) ==', k, '){')
                        print('stroke',
                              colors[funcs[k](
                                        matrix_p1_aux[get_away[0][0]],
                                        matrix_q1_aux[get_away[0][1]])])
                        print('line', matrix_p1[get_away[0][0]] + matrix_q1[get_away[0][1]])
                        print('}')

                        print('if (int(fun) ==', k, '){')
                        print('stroke', colors[
                        funcs[k](
                               matrix_p2_aux[get_away[0][0]],
                               matrix_q2_aux[get_away[0][1]])])
                        print('line', matrix_p2[get_away[0][0]] + matrix_q2[get_away[0][1]])
                        print('}')

                        print('if (int(fun) ==', k, '){')
                        print('stroke', colors[
                            funcs[k](
                                   matrix_p3_aux[get_away[0][0]],
                                   matrix_q3_aux[get_away[0][1]])])
                        print('line', matrix_p3[get_away[0][0]] + matrix_q3[get_away[0][1]])
                        print('}')

                        print('if (int(fun) ==', k, '){')
                        print('stroke', colors[
                            funcs[k](
                                   matrix_p4_aux[get_away[0][0]],
                                   matrix_q4_aux[get_away[0][1]])])
                        print('line', matrix_p4[get_away[0][0]] + matrix_q4[get_away[0][1]])
                        print('}')

