from special_functions import *

r_zero = [0]
r_one = [1]
r_two = [[0, 1], [1, 0]]
r_three = [[0, 0], [0, 1], [1, 1]]
r_four = [[0, 0, 0, 0], [0, 0, 1, 1],
          [0, 1, 0, 1], [0, 1, 1, 0],
          [1, 0, 0, 1], [1, 0, 1, 0],
          [1, 1, 0, 0], [1, 1, 1, 1]]

R_LA1 = (r_zero, r_one, r_two, r_three, r_four)

cartesian_r_two = []
for i in r_two:
    for j in r_two:
        cartesian_r_two.append([i,j])

lin_cart = []
for a in cartesian_r_two:
    for b in a:
        lin_cart.append(b)

p_relation_place = (350, 50)
p_rplace = []
for i in range(8):
    p_rplace.append((p_relation_place[0], p_relation_place[1]+50*i))

q_relation_place = (450, 50)
q_rplace = []
for i in range(8):
    q_rplace.append((q_relation_place[0], q_relation_place[1]+50*i))


coordinates = [0, 1]

one_color = (0, 0, 255)
zero_color = (255, 255, 0)
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
    for m in range(8):
        print('if (fun ==', k, '){')
        print('stroke', colors[tau2[k](lin_cart[m][0], lin_cart[m][1])])
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

for i in range(len(lin_cart)):
    print('stroke', colors[lin_cart[i][0]])
    print('strokeWeight(17)')
    print('point', p_rplace[i])

for i in range(len(lin_cart)):
    print('stroke', colors[lin_cart[i][1]])
    print('strokeWeight(17)')
    print('point', q_rplace[i])



