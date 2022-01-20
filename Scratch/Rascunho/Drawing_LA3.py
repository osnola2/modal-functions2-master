from Structure.binary_functions import *
from special_functions import *

coordinates = [0, 1, 2, 3, 4, 5, 6, 9]

zero_color = (255, 255, 0)
one_color = (0, 0, 255)
two_color = (204, 160, 17)
three_color = (100, 200, 190)
four_color = (162, 3, 224)
five_color = (250, 5, 0)
six_color = (225, 105, 230)
nine_color = (40, 190, 25)

colors = (zero_color, one_color, two_color, three_color, four_color, five_color, six_color, [], [], nine_color)

p_one = (50, 50)
p_five = (50, 120)
p_four = (50, 190)
p_nine = (50, 260)
p_six = (50, 330)
p_two = (50, 400)
p_three = (50, 470)
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


for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_1[i])

for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_2[i])