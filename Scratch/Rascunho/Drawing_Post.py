from Structure.binary_functions import *


coordinates = [0, 1]

one_color = (0, 0, 255)
zero_color = (255, 255, 0)
colors = (zero_color, one_color)

p_one = (100, 100)
p_zero = (100, 300)

var_1 = (p_zero, p_one)

q_one = (300, 100)
q_zero = (300, 300)

var_2 = (q_zero, q_one,)


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


for i in range(len(coordinates)):
    print('stroke', colors[i])
    print('strokeWeight(17)')
    print('point', var_1[i])

for i in range(len(coordinates)):
    print('stroke', colors[i])
    print('strokeWeight(17)')
    print('point', var_2[i])

# print(i, j, k.__name__, k(i, j))
# toy = [tau2[0], tau2[1], tau2[3], tau2[4]]


# for k in toy:
#     for i in coordinates:
#         for j in coordinates:
#             print(i, j, k.__name__, k(i, j))
#
# for k in range(len(toy)):
#     for i in coordinates:
#         for j in coordinates:
#             print('if (fun ==', k, '){')
#             print('stroke', colors[toy[k](i, j)])
#             print('line', var_1[i] + var_2[j])
#             print('}')
#             print('//', toy[k].__name__)