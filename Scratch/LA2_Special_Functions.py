from Structure.binary_functions import *
from special_functions import *
coordinates = [0, 6, 9, 1]

one_color = (0, 0, 255)
nine_color = (	238,130,238)
six_color = (0,250,154)
zero_color = (255, 255, 0)
colors = (zero_color, one_color, [], [], [], [], six_color, [], [], nine_color)

p_one = (50, 50)
p_six = (50, 200)
p_nine = (50, 350)
p_zero = (50, 500)

var_1 = (p_zero, p_one, [], [], [], [], p_six, [], [], p_nine)

q_one = (350, 50)
q_six = (350, 200)
q_nine = (350, 350)
q_zero = (350, 500)

var_2 = (q_zero, q_one, [], [], [], [], q_six, [], [], q_nine)


# for k in spec_fun:
#     for i in coordinates:
#         for j in coordinates:
#             print(i, j, k.__name__, k(i, j))

for k in range(len(spec_fun)):
    for i in coordinates:
        for j in coordinates:
            print('if (fun ==', k, '){')
            print('stroke', colors[spec_fun[k](i, j)])
            print('line', var_1[i] + var_2[j])
            print('}')
            print('//', spec_fun[k].__name__)


for i in [0,1, 6, 9]:
    print('stroke', colors[i])
    print('strokeWeight(17)')
    print('point', var_1[i])

for i in [0,1, 6, 9]:
    print('stroke', colors[i])
    print('strokeWeight(17)')
    print('point', var_2[i])