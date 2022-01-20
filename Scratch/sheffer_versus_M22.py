from Structure.modal_functions import *
from Structure.taumodels import *

shef_list = [[1, 0, 0, 1, 1, 1, 2],
            [1, 0, 0, 1, 1, 1, 4],
            [1, 0, 0, 1, 1, 1, 6],
            [1, 0, 0, 1, 1, 1, 7],
            [1, 0, 0, 1, 1, 1, 9],
            [1, 0, 0, 1, 1, 1, 11],
            [1, 0, 0, 1, 1, 1, 13],
            [1, 0, 0, 1, 1, 2, 1],
            [1, 0, 0, 1, 1, 2, 2],
            [1, 0, 0, 1, 1, 2, 4],
             [3, 0, 0, 1, 1, 1, 2],
             [3, 0, 0, 1, 1, 1, 4],
             [3, 0, 0, 1, 1, 1, 6],
             [3, 0, 0, 1, 1, 1, 7],
             [3, 0, 0, 1, 1, 1, 9],
             [3, 0, 0, 1, 1, 1, 11],
             [3, 0, 0, 1, 1, 1, 13],
             [3, 0, 0, 1, 1, 2, 1],
             [3, 0, 0, 1, 1, 2, 2],
             [3, 0, 0, 1, 1, 2, 4],
             [3, 0, 0, 1, 1, 2, 6],
             [3, 0, 0, 1, 1, 2, 7],
             [3, 0, 0, 1, 1, 2, 9],
             [3, 0, 0, 1, 1, 2, 11],
             [3, 0, 0, 1, 1, 2, 13],
             [3, 0, 0, 1, 1, 3, 1],
             [3, 0, 0, 1, 1, 3, 2],
             [3, 0, 0, 1, 1, 3, 4],
             [3, 0, 0, 1, 1, 3, 6],
             [3, 0, 0, 1, 1, 3, 7],
[5, 8, 8, 1, 10, 13, 1],
[5, 8, 8, 1, 10, 13, 7],
[5, 8, 8, 1, 10, 14, 1],
[5, 8, 8, 1, 10, 14, 7],
[5, 8, 8, 1, 11, 1, 1],
[5, 8, 8, 1, 11, 1, 2],
[5, 8, 8, 1, 11, 1, 4],
[5, 8, 8, 1, 11, 1, 6],
[5, 8, 8, 1, 11, 1, 7],
[5, 8, 8, 1, 11, 1, 9],
[5, 8, 8, 1, 11, 1, 11],
[5, 8, 8, 1, 11, 1, 13],
[5, 8, 8, 1, 11, 2, 1],
             [13, 0, 0, 1, 7, 2, 4], [13, 0, 1, 1, 2, 3, 13], [13, 0, 1, 6, 1, 11, 6], [13, 0, 1, 6, 13, 8, 13],
             [13, 0, 2, 0, 9, 14, 6], [13, 0, 2, 1, 11, 13, 7], [13, 0, 2, 2, 4, 7, 11], [13, 0, 2, 3, 6, 11, 13],
             [13, 0, 2, 4, 10, 2, 2], [13, 0, 2, 6, 11, 11, 1], [13, 0, 3, 1, 9, 7, 13], [13, 0, 9, 0, 8, 7, 9],
             [13, 0, 9, 1, 7, 9, 2], [13, 0, 9, 2, 7, 2, 9], [13, 0, 10, 6, 10, 2, 6], [13, 0, 11, 6, 8, 2, 6],
             [13, 1, 0, 1, 9, 8, 6], [13, 1, 0, 6, 9, 8, 7], [13, 1, 1, 1, 6, 1, 7], [13, 1, 1, 6, 8, 7, 13],
             [13, 1, 2, 0, 9, 9, 7], [13, 1, 2, 3, 7, 1, 9], [13, 1, 2, 4, 13, 1, 1], [13, 1, 2, 7, 4, 7, 7],
             [13, 1, 3, 6, 2, 14, 1], [13, 1, 3, 6, 13, 12, 1], [13, 1, 8, 1, 7, 6, 13], [13, 1, 8, 1, 13, 7, 9],
             [13, 1, 9, 2, 1, 7, 7], [13, 1, 9, 4, 7, 11, 6]]

r_22 = [[0, 0], [6, 6], [2, 4], [3, 5], [5, 3], [4, 2], [9, 9], [1, 1]]

funcs = shef_list
relation = r_22

# for i in funcs:
#     print(list(map(lambda x: tau2[x].__name__, i)))

cartesian_relation = []
for i in relation:
    for j in relation:
        cartesian_relation.append([i,j])

lin_cart_p =[]
lin_cart_q =[]
for a in cartesian_relation:
    lin_cart_p.append(a[0][0])
    lin_cart_p.append(a[0][1])
    lin_cart_q.append(a[1][0])
    lin_cart_q.append(a[1][1])


p_relation_place = (430, 50)
p_rel_aux = [430, 10]
p_rplace = []

margin = 619

for i in range(len(lin_cart_p)):
    if p_rel_aux[1]+40 < margin:
        if i %2 == 0:
            p_rel_aux = [p_rel_aux[0], p_rel_aux[1]+40]
            p_rplace.append((p_rel_aux[0], p_rel_aux[1]))
        if i %2 > 0:
            p_rel_aux = [p_rel_aux[0], p_rel_aux[1] + 20]
            p_rplace.append((p_rel_aux[0], p_rel_aux[1]))
    elif p_rel_aux[1]+40 >= margin:
        p_rel_aux = [p_rel_aux[0]+150, 50]
        p_rplace.append((p_rel_aux[0], p_rel_aux[1]))

q_relation_place = (530, 50)
q_rel_aux = (530, 10)
q_rplace = []

for i in range(len(lin_cart_q)):
    if q_rel_aux[1]+40 < margin:
        if i %2 == 0:
            q_rel_aux = [q_rel_aux[0], q_rel_aux[1]+40]
            q_rplace.append((q_rel_aux[0], q_rel_aux[1]))
        if i %2 > 0:
            q_rel_aux = [q_rel_aux[0], q_rel_aux[1] + 20]
            q_rplace.append((q_rel_aux[0], q_rel_aux[1]))
    elif q_rel_aux[1]+40 >= margin:
        q_rel_aux = [q_rel_aux[0]+150, 50]
        q_rplace.append((q_rel_aux[0], q_rel_aux[1]))

matrix_place = (50, 630)

matrix_p = []
for i in range(len(relation)):
    matrix_p.append((matrix_place[0]+40*i, matrix_place[1]))

matrix_q = []
for i in range(len(relation)):
    matrix_q.append((matrix_place[0]+40*i, matrix_place[1]+40))


coordinates = [0, 1, 2, 3, 4, 5, 6, 9]

zero_color = (0, 0, 0)
one_color = (255, 255, 255)
two_color = (0, 0, 255)
three_color = (140, 0, 255)
four_color = (255, 102, 0)
five_color = (255, 0 , 0)
six_color = (0, 255, 0)
nine_color = (255, 255, 0)

colors = (zero_color, one_color, two_color, three_color, four_color, five_color, six_color, [], [], nine_color)

p_one = (50, 50)
p_three = (50, 470)
p_four = (50, 190)
p_nine = (50, 260)
p_six = (50, 330)
p_two = (50, 400)
p_five = (50, 120)
p_zero = (50, 540)

var_1 = (p_zero, p_one, p_two, p_three, p_four, p_five, p_six, [], [], p_nine)

q_one = (350, 50)
q_three = (350, 470)
q_four = (350, 190)
q_nine = (350, 260)
q_six = (350, 330)
q_two = (350, 400)
q_five = (350, 120)
q_zero = (350, 540)

var_2 = (q_zero, q_one, q_two, q_three, q_four, q_five, q_six, [], [], q_nine)


for k in range(len(funcs)):
    for i in coordinates:
        for j in coordinates:
            print('if (int(fun) ==', k, '){')
            print('stroke', colors[
                  modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
                         tal[funcs[k][5]], tal[funcs[k][6]], i, j)])
            print('line', var_1[i] + var_2[j])
            print('}')


print('strokeWeight(4)')

for k in range(len(funcs)):
    for i in range(len(lin_cart_p)):
        print('if (int(fun) ==', k, '){')
        print('stroke', colors[
                  modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
                           tal[funcs[k][5]], tal[funcs[k][6]], lin_cart_p[i], lin_cart_q[i])])
        print('line', p_rplace[i] + q_rplace[i])
        print('}')


for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_1[i])

for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_2[i])

for i in range(len(p_rplace)):
    print('stroke', colors[lin_cart_p[i]])
    print('strokeWeight(10)')
    print('point', p_rplace[i])

for i in range(len(q_rplace)):
    print('stroke', colors[lin_cart_q[i]])
    print('strokeWeight(10)')
    print('point', q_rplace[i])

for i in range(len(relation)):
    print('stroke', colors[relation[i][0]])
    print('strokeWeight(14)')
    print('point', matrix_p[i])

for i in range(len(relation)):
    print('stroke', colors[relation[i][1]])
    print('strokeWeight(14)')
    print('point', matrix_q[i])



for i in range(len(funcs)):

    print("if (mouseY >", i*60, "&& mouseY <=", i*60+60, "){ fun = map(mouseX, 0, 450,", i*5, ",", i*5+5, "); }")

print( 'fill(0)')
print('text(shef[int(fun)], 100, 580)')