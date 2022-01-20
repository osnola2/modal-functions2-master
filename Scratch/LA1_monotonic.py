from special_functions import *

r_zero = [0]
r_one = [1]
r_two = [[0, 1], [1, 0]]
r_three = [[0, 0], [0, 1], [1, 1]]
r_four = [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0],
              [1, 1, 1, 1]]
R_LA1 = (r_zero, r_one, r_two, r_three, r_four)

cartesian_r_three = []
for i in r_three:
    for j in r_three:
        cartesian_r_three.append([i,j])

lin_cart_p =[]
lin_cart_q =[]
for a in cartesian_r_three:
    lin_cart_p.append(a[0][0])
    lin_cart_p.append(a[0][1])
    lin_cart_q.append(a[1][0])
    lin_cart_q.append(a[1][1])


p_relation_place = (350, 50)
p_rel_aux = [350, 10]
p_rplace = []


for i in range(18):
    if i %2 == 0:
        p_rel_aux = [p_rel_aux[0], p_rel_aux[1]+40]
        p_rplace.append((p_rel_aux[0], p_rel_aux[1]))
    if i %2 > 0:
        p_rel_aux = [p_rel_aux[0], p_rel_aux[1] + 20]
        p_rplace.append((p_rel_aux[0], p_rel_aux[1]))

q_relation_place = (450, 50)
q_rel_aux = (450, 10)
q_rplace = []

for i in range(18):
    if i % 2 == 0:
        q_rel_aux = [q_rel_aux[0], q_rel_aux[1] + 40]
        q_rplace.append((q_rel_aux[0], q_rel_aux[1]))
    if i % 2 > 0:
        q_rel_aux = [q_rel_aux[0], q_rel_aux[1] + 20]
        q_rplace.append((q_rel_aux[0], q_rel_aux[1]))

matrix_place = (100, 500)

matrix_p = []
for i in range(len(r_three)):
    matrix_p.append((matrix_place[0]+40*i, matrix_place[1]))

matrix_q = []
for i in range(len(r_three)):
    matrix_q.append((matrix_place[0]+40*i, matrix_place[1]+40))


coordinates = [0, 1]

one_color = (255, 255, 255)
zero_color = (0, 0, 0)
colors = (zero_color, one_color)

p_one = (50, 50)
p_zero = (50, 300)

var_1 = (p_zero, p_one)

q_one = (250, 50)
q_zero = (250, 300)

var_2 = (q_zero, q_one)


# for k in tau2:
#     for i in coordinates:
#         for j in coordinates:
#             print(i, j, k.__name__, k(i, j))

for k in range(len(tau2)):
    for i in coordinates:
        for j in coordinates:
            print('if (fun ==', k, '){')
            print('stroke', colors[tau2[k](i, j)])
            print('line', var_1[i] + var_2[j])
            print('}')
            print('//', tau2[k].__name__)


for k in range(len(tau2)):
    for m in range(len(p_rplace)):
        print('if (fun ==', k, '){')
        print('strokeWeight(5)')
        print('stroke', colors[tau2[k](lin_cart_p[m], lin_cart_q[m])])
        print('line', p_rplace[m] + q_rplace[m])
        print('}')
        print('//', tau2[k].__name__)




for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(17)')
    print('point', var_1[i])

for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(17)')
    print('point', var_2[i])

for i in range(len(p_rplace)):
    print('stroke', colors[lin_cart_p[i]])
    print('strokeWeight(10)')
    print('point', p_rplace[i])

for i in range(len(q_rplace)):
    print('stroke', colors[lin_cart_q[i]])
    print('strokeWeight(10)')
    print('point', q_rplace[i])

for i in range(len(r_three)):
    print('stroke', colors[r_three[i][0]])
    print('strokeWeight(10)')
    print('point', matrix_p[i])

for i in range(len(r_three)):
    print('stroke', colors[r_three[i][1]])
    print('strokeWeight(10)')
    print('point', matrix_q[i])




