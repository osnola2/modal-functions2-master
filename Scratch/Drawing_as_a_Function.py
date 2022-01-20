from Structure.modal_functions import *
from Structure.taumodels import *
from Structure.matrices import *
from Scratch.pi2 import *
from Scratch.Draw_setup import *
from Scratch.get_away_unary import *
from Scratch.get_away_matrices import *
from Scratch.get_away_ternary import *
from Scratch.get_away_quaternary import *



funcs = easy_end_pi23

canvas = (1800, 900)

p_1 = (225, 150)
skip_1 = 150


p_2 = (200, 500)
skip_2 = 100

p_3 = (150, 1000)
skip_3 = 75


# for i in funcs:
#     print(list(map(lambda x: tau2[x].__name__, i)))




p_one3 = (p_3[0], p_3[1])
p_five3 = (p_3[0], p_3[1]+skip_3)
p_four3 = (p_3[0], p_3[1]+2*skip_3)
p_nine3 = (p_3[0], p_3[1]+3*skip_3)
p_six3 = (p_3[0], p_3[1]+4*skip_3)
p_two3 = (p_3[0], p_3[1]+5*skip_3)
p_three3 = (p_3[0], p_3[1]+6*skip_3)
p_zero3 = (p_3[0], p_3[1]+7*skip_3)

var_p_3 = (p_zero3, p_one3, p_two3, p_three3, p_four3, p_five3, p_six3, [], [], p_nine3)

q_3 = (p_3[0]+skip_3*4, p_3[1])

q_one3 = (q_3[0], q_3[1])
q_five3 = (q_3[0], q_3[1]+skip_3)
q_four3 = (q_3[0], q_3[1]+2*skip_3)
q_nine3 = (q_3[0], q_3[1]+3*skip_3)
q_six3 = (q_3[0], q_3[1]+4*skip_3)
q_two3 = (q_3[0], q_3[1]+5*skip_3)
q_three3 = (q_3[0], q_3[1]+6*skip_3)
q_zero3 = (q_3[0], q_3[1]+7*skip_3)

var_q_3 = (q_zero3, q_one3, q_two3, q_three3, q_four3, q_five3, q_six3, [], [], q_nine3)




p_one2 = (p_2[0], p_2[1])
p_nine2 = (p_2[0], p_2[1]+skip_2)
p_six2 = (p_2[0], p_2[1]+2*skip_2)
p_zero2 = (p_2[0], p_2[1]+3*skip_2)

var_p_2 = (p_zero2, p_one2, [], [], [], [], p_six2, [], [], p_nine2)

q_2 = (p_2[0]+skip_2*2, p_2[1])

q_one2 = (q_2[0], q_2[1])
q_nine2 = (q_2[0], q_2[1]+skip_2)
q_six2 = (q_2[0], q_2[1]+2*skip_2)
q_zero2 = (q_2[0], q_2[1]+3*skip_2)

var_q_2 = (q_zero2, q_one2, [], [], [], [], q_six2, [], [], q_nine2)

p_one1 = (p_1[0], p_1[1])
p_zero1 = (p_1[0], p_1[1]+skip_1)

var_p_1 = (p_zero1, p_one1, [], [], [], [], [], [], [], [])

q_1 = (p_1[0]+skip_1, p_1[1])

q_one1 = (q_1[0], q_1[1])
q_zero1 = (q_1[0], q_1[1]+skip_1)

var_q_1 = (q_zero1, q_one1, [], [], [], [], [], [], [], [])


print('strokeWeight(3)')
for k in range(len(funcs)):
    for i in coordinates3:
        for j in coordinates3:
            print('if (int(fun) ==', k, '){')
            print('stroke', colors[
                  modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
                         tal[funcs[k][5]], tal[funcs[k][6]], i, j)])
            print('line', var_p_3[i] + var_q_3[j])
            print('}')


for k in range(len(funcs)):
    for i in coordinates2:
        for j in coordinates2:
            print('if (int(fun) ==', k, '){')
            print('stroke', colors[
                  modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
                         tal[funcs[k][5]], tal[funcs[k][6]], i, j)])
            print('line', var_p_2[i] + var_q_2[j])
            print('}')


for k in range(len(funcs)):
    for i in coordinates1:
        for j in coordinates1:
            print('if (int(fun) ==', k, '){')
            print('stroke', colors[
                  modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
                         tal[funcs[k][5]], tal[funcs[k][6]], i, j)])
            print('line', var_p_1[i] + var_q_1[j])
            print('}')


for i in coordinates3:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_p_3[i])

for i in coordinates3:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_q_3[i])

for i in coordinates2:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_p_2[i])

for i in coordinates2:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_q_2[i])

for i in coordinates1:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_p_1[i])

for i in coordinates1:
    print('stroke', colors[i])
    print('strokeWeight(12)')
    print('point', var_q_1[i])



