from special_functions import *

r_three = ((0, 0), (0, 1), (1, 1))

cartesian_r_three = []
for i in r_three:
    for j in r_three:
        cartesian_r_three.append([i,j])

lin_cart = []
for a in cartesian_r_three:
    for b in a:
        lin_cart.append(b)


print(cartesian_r_three)
print(lin_cart)
print(len(lin_cart))

coordinates = [0, 1]

one_color = (0, 0, 255)
zero_color = (255, 255, 0)
colors = (zero_color, one_color)

p_relation_place = (350, 50)
p_rplace = []
for i in range(18):
    p_rplace.append((p_relation_place[0], p_relation_place[1]+25*i))
print(p_rplace)

q_relation_place = (450, 50)
q_rplace = []

for i in range(18):
    q_rplace.append((q_relation_place[0], q_relation_place[1]+25*i))
print(q_rplace)

relation_place = [p_relation_place, q_relation_place]


for i in range(len(lin_cart)):
    print('stroke', colors[lin_cart[i][0]])
    print('strokeWeight(10)')
    print('point', p_rplace[i])

for i in range(len(lin_cart)):
    print('stroke', colors[lin_cart[i][1]])
    print('strokeWeight(10)')
    print('point', q_rplace[i])




