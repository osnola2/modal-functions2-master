


from Structure.modal_functions import *
from Structure.taumodels import *
from Scratch.Draw_setup import *

step_m = 25
p_stroke = 12
l_stroke = 3

def get_away_draw(funcs, relation, place):

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

    matrix_q1 = []
    matrix_q1_aux = []
    for i in range(len(relation)):
        matrix_q1.append((matrix_place[0] + step_m * i + step_m*(len(relation)+3), matrix_place[1]))
        matrix_q1_aux.append(relation[i][0])

    matrix_q2 = []
    matrix_q2_aux = []
    for i in range(len(relation)):
        matrix_q2.append((matrix_place[0] + step_m * i + step_m*(len(relation)+3), matrix_place[1] + step_m))
        matrix_q2_aux.append(relation[i][1])

    # for i in range(len(relation)):
    #     print('stroke', colors[relation[i][0]])
    #     print('strokeWeight(', p_stroke, ')')
    #     print('point', matrix_p1[i])
    #
    # for i in range(len(relation)):
    #     print('stroke', colors[relation[i][1]])
    #     print('strokeWeight(', p_stroke, ')')
    #     print('point', matrix_p2[i])
    #
    # for i in range(len(relation)):
    #     print('stroke', colors[relation[i][0]])
    #     print('strokeWeight(', p_stroke, ')')
    #     print('point', matrix_q1[i])
    #
    # for i in range(len(relation)):
    #     print('stroke', colors[relation[i][1]])
    #     print('strokeWeight(', p_stroke, ')')
    #     print('point', matrix_q2[i])
    #
    # print('strokeWeight(', l_stroke, ')')

    for k in range(len(funcs)):
        get_away = []
        for i in range(len(matrix_p1_aux)):
            for j in range(len(matrix_q1_aux)):
                if type(funcs[k]) == list:
                    if [modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
                           tal[funcs[k][5]], tal[funcs[k][6]], matrix_p1_aux[i], matrix_q1_aux[j]),
                        modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
                           tal[funcs[k][5]], tal[funcs[k][6]], matrix_p2_aux[i], matrix_q2_aux[j])] not in relation:
                        if len(get_away) < 1:
                            get_away.append([i, j])
                            print('if (int(fun) ==', k, '){')
                            print('stroke',
                            colors[modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]],
                                        tal[funcs[k][4]], tal[funcs[k][5]], tal[funcs[k][6]],
                                        matrix_p1_aux[get_away[0][0]],
                                        matrix_q1_aux[get_away[0][1]])])

                            print('line', matrix_p1[get_away[0][0]] + matrix_q1[get_away[0][1]])
                            print('}')
                            print('if (int(fun) ==', k, '){')
                            print('stroke', colors[
                                modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]],
                                tal[funcs[k][4]], tal[funcs[k][5]], tal[funcs[k][6]], matrix_p2_aux[get_away[0][0]],
                                 matrix_q2_aux[get_away[0][1]])])
                            print('line', matrix_p2[get_away[0][0]] + matrix_q2[get_away[0][1]])
                            print('}')

                else:
                    if [funcs[k](matrix_p1_aux[i], matrix_q1_aux[j]), funcs[k](matrix_p2_aux[i], matrix_q2_aux[j])] not in relation:
                        if len(get_away) < 1:
                            get_away.append([i, j])
                            print('if (int(fun) ==', k, '){')
                            print('stroke',
                                      colors[funcs[k](matrix_p1_aux[get_away[0][0]],
                                                 matrix_q1_aux[get_away[0][1]])])

                            print('line', matrix_p1[get_away[0][0]] + matrix_q1[get_away[0][1]])
                            print('}')
                            print('if (int(fun) ==', k, '){')
                            print('stroke', colors[
                                    funcs[k](matrix_p2_aux[get_away[0][0]], matrix_q2_aux[get_away[0][1]])])
                            print('line', matrix_p2[get_away[0][0]] + matrix_q2[get_away[0][1]])
                            print('}')

