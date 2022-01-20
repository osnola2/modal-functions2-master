from special_functions import *

p_one = (100, 50)
p_sigma = (100, 150)
p_rho = (100, 250)
p_zero = (100, 350)

var_1 = (p_one, p_sigma, p_rho, p_zero)

q_one = (300, 50)
q_sigma = (300, 150)
q_rho = (300, 250)
q_zero = (300, 350)

var_2 = (q_one, q_sigma, q_rho, q_zero)

one_color = (0, 0, 255)
sigma_color = (60, 179, 113)
rho_color = (238, 130, 238)
zero_color = (255, 255, 0)

colors = (one_color, sigma_color, rho_color, zero_color)




for i in range(4):
    for j in range(4):
        for k in range(4):
            print('if painting =', i, j, k )
            print('stroke', colors[i])
            print('line', var_1[j]+var_2[k])


print('_______________________________________________________')
# for i in var_1:
#     for j in var_2:
#         for k in colors:
#         print('stroke', colors[i])
#         print('line', i + j)
#




for i in range(4):
    print('stroke', colors[i])
    print('strokeWeight(14)')
    print('point', var_1[i])

for i in range(4):
    print('stroke', colors[i])
    print('strokeWeight(14)')
    print('point', var_2[i])






def verum1(prop1):
    return 1

def nbox(prop1):
    return neg(box(prop1))

def ndiam(prop1):
    return neg(diam(prop1))
def cont(prop1):
    return neg(rigid(prop1))
def impossible(prop1):
    return neg(diam(prop1))
def cont_false(prop1):
    return conj(cont(prop1), neg(prop1))
def cont_neg(prop1):
    return disj(box(prop1), cont_false(prop1))
def ncon_true(prop1):
    return neg(cont_true(prop1))
def rig_neg(prop1):
    return disj(impossible(prop1), cont_true(prop1))
def id(prop1):
    return prop1
def not_nec(prop1):
    return neg(box(prop1))




coordinates = [1, 6, 9, 0]


modfun1 = [falsum1, impossible, box, rigid, cont_false, neg, cont_neg, ncon_true, cont_true, rig_neg, id, not_cont_false,
           cont, not_nec, box, verum1]

for i in modfun1:
    print (i.__name__, (list(map(i, coordinates))))

# for i in range(30):
#
#     print("if (mouseY >", 0, "&& mouseY <=", 150, "){ number = map(mouseX, 0, 700,", 150, ",", 300, "); }")
#
# this associates a number between 0 and 10000 with each square of 7x7 pixels in the canvas

