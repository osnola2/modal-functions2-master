from Structure.modal_functions import *
from Structure.taumodels import *

pi21 = [(0, 1, 3, 0, 15, 2, 2), (0, 1, 14, 0, 1, 11, 2), (0, 1, 14, 0, 15, 12, 2), (0, 2, 0, 0, 13, 11, 0), (0, 3, 3, 0, 0, 3, 2), (0, 3, 3, 0, 2, 2, 2), (0, 3, 3, 0, 15, 0, 2), (0, 3, 14, 0, 2, 12, 2), (0, 3, 14, 0, 15, 1, 2), (0, 10, 14, 0, 13, 0, 2), (1, 1, 3, 0, 2, 0, 2), (1, 1, 13, 0, 1, 2, 2), (1, 1, 13, 0, 2, 11, 2), (1, 1, 13, 0, 12, 12, 2), (1, 1, 14, 0, 2, 12, 2), (1, 1, 14, 0, 3, 3, 2), (1, 1, 14, 0, 14, 12, 2), (1, 3, 13, 0, 1, 1, 2), (1, 10, 3, 0, 14, 3, 2), (1, 10, 14, 0, 15, 1, 2), (2, 1, 3, 3, 0, 1, 3), (2, 1, 3, 3, 1, 0, 3), (2, 1, 3, 11, 1, 12, 3), (2, 1, 3, 11, 12, 2, 3), (2, 1, 13, 3, 14, 11, 3), (2, 1, 14, 11, 12, 2, 3), (2, 1, 14, 11, 15, 12, 3), (2, 2, 0, 3, 1, 12, 1), (2, 3, 3, 3, 0, 11, 3), (2, 3, 3, 11, 3, 0, 3), (2, 3, 13, 3, 0, 2, 3), (2, 3, 14, 3, 12, 2, 3), (2, 3, 14, 11, 15, 3, 3), (2, 10, 3, 3, 1, 2, 3), (2, 10, 3, 3, 12, 1, 3), (2, 10, 14, 3, 1, 0, 3), (2, 10, 14, 11, 15, 11, 3), (3, 1, 3, 11, 0, 3, 3), (3, 1, 3, 11, 13, 3, 3), (3, 1, 13, 11, 13, 2, 3), (3, 1, 14, 3, 3, 0, 3), (3, 1, 14, 3, 13, 12, 3), (3, 2, 0, 3, 2, 11, 1), (3, 2, 0, 11, 1, 12, 1), (3, 3, 3, 11, 12, 0, 3), (3, 10, 3, 3, 14, 0, 3), (3, 10, 13, 3, 13, 12, 3), (3, 10, 13, 11, 0, 12, 3), (3, 10, 14, 3, 0, 3, 3), (3, 10, 14, 3, 3, 11, 3), (3, 10, 14, 3, 3, 11, 3), (3, 10, 14, 11, 0, 0, 3), (3, 10, 14, 11, 0, 1, 3), (3, 10, 14, 11, 12, 2, 3), (3, 10, 14, 11, 12, 2, 3), (12, 12, 1, 12, 2, 0, 12), (12, 12, 1, 12, 2, 11, 12), (12, 12, 2, 1, 1, 0, 12), (12, 12, 2, 1, 13, 2, 12), (12, 12, 2, 2, 14, 1, 12), (12, 12, 2, 12, 14, 1, 12), (12, 12, 2, 12, 15, 3, 12), (12, 12, 12, 1, 0, 0, 12), (12, 12, 12, 1, 1, 2, 12), (12, 13, 15, 1, 3, 3, 14), (12, 13, 15, 2, 0, 12, 14), (12, 13, 15, 2, 14, 3, 14), (12, 13, 15, 12, 15, 3, 14), (12, 14, 1, 2, 3, 0, 12), (12, 14, 1, 2, 3, 1, 12), (12, 14, 1, 12, 1, 11, 12), (12, 14, 2, 1, 3, 12, 12), (12, 14, 2, 12, 12, 12, 12), (12, 14, 2, 12, 15, 11, 12), (12, 14, 12, 12, 1, 1, 12), (12, 15, 15, 1, 0, 0, 14), (12, 15, 15, 1, 3, 2, 14), (12, 15, 15, 12, 1, 1, 14), (13, 12, 1, 1, 3, 12, 12), (13, 12, 1, 1, 13, 11, 12), (13, 12, 1, 1, 14, 1, 12), (13, 12, 1, 1, 15, 12, 12), (13, 12, 1, 12, 1, 1, 12), (13, 12, 2, 1, 15, 11, 12), (13, 12, 2, 2, 2, 12, 12), (13, 12, 2, 12, 3, 11, 12), (13, 12, 12, 1, 0, 11, 12), (13, 12, 12, 2, 2, 11, 12), (13, 13, 15, 2, 3, 1, 14), (13, 13, 15, 12, 15, 0, 14), (13, 14, 1, 12, 15, 12, 12), (13, 14, 2, 2, 2, 3, 12), (13, 14, 2, 2, 12, 12, 12), (13, 14, 2, 12, 15, 1, 12), (13, 14, 12, 2, 2, 12, 12), (13, 14, 12, 2, 15, 11, 12), (13, 14, 12, 12, 15, 3, 12), (13, 15, 15, 1, 3, 1, 14), (13, 15, 15, 1, 14, 3, 14), (13, 15, 15, 2, 12, 1, 14)]


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

for k in range(len(pi21)):
    for i in coordinates:
        for j in coordinates:
            print('if (int(fun) ==', k, '){')
            print('stroke',colors[
                  modfun(tal[pi21[k][0]], tal[pi21[k][1]], tal[pi21[k][2]], tal[pi21[k][3]], tal[pi21[k][4]],
                         tal[pi21[k][5]], tal[pi21[k][6]], i, j)])
            print('line', var_1[i] + var_2[j])
            print('}')


for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_1[i])

for i in coordinates:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_2[i])

for i in range(20):

    print("if (mouseY >", i*40, "&& mouseY <=", i*40+40, "){ fun = map(mouseX, 0, 450,", i*7, ",", i*7+7, "); }")

print( 'fill(0)')
print('text(pi21[int(fun)], 100, 580)')

# for k in range(len(pi21)):
#     for i in coordinates:
#         for j in coordinates:
#             print('modfun', tal[pi21[k][0]], tal[pi21[k][1]], tal[pi21[k][2]], tal[pi21[k][3]], tal[pi21[k][4]],
#                    tal[pi21[k][5]], tal[pi21[k][6]], i, j)
#             print(i, j, modpro(i, j))

# a = []
# for i in range(len(pi21)):
#     a.append(list(map(lambda x : tau2[x].__name__, pi21[i])))
# print(a)   ## to give readable names to the functions
