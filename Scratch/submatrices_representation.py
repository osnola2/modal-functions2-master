# cartesian_relation = []
# for i in relation:
#     for j in relation:
#         cartesian_relation.append([i,j])
#
# lin_cart_p =[]
# lin_cart_q =[]
# for a in cartesian_relation:
#     lin_cart_p.append(a[0][0])
#     lin_cart_p.append(a[0][1])
#     lin_cart_q.append(a[1][0])
#     lin_cart_q.append(a[1][1])
#
#
# p_relation_place = (430, 50)
# p_rel_aux = [430, 10]
# p_rplace = []
#
# margin = 619
#
# for i in range(len(lin_cart_p)):
#     if p_rel_aux[1]+40 < margin:
#         if i %2 == 0:
#             p_rel_aux = [p_rel_aux[0], p_rel_aux[1]+40]
#             p_rplace.append((p_rel_aux[0], p_rel_aux[1]))
#         if i %2 > 0:
#             p_rel_aux = [p_rel_aux[0], p_rel_aux[1] + 20]
#             p_rplace.append((p_rel_aux[0], p_rel_aux[1]))
#     elif p_rel_aux[1]+40 >= margin:
#         p_rel_aux = [p_rel_aux[0]+150, 50]
#         p_rplace.append((p_rel_aux[0], p_rel_aux[1]))
#
# q_relation_place = (530, 50)
# q_rel_aux = (530, 10)
# q_rplace = []
#
# for i in range(len(lin_cart_q)):
#     if q_rel_aux[1]+40 < margin:
#         if i %2 == 0:
#             q_rel_aux = [q_rel_aux[0], q_rel_aux[1]+40]
#             q_rplace.append((q_rel_aux[0], q_rel_aux[1]))
#         if i %2 > 0:
#             q_rel_aux = [q_rel_aux[0], q_rel_aux[1] + 20]
#             q_rplace.append((q_rel_aux[0], q_rel_aux[1]))
#     elif q_rel_aux[1]+40 >= margin:
#         q_rel_aux = [q_rel_aux[0]+150, 50]
#         q_rplace.append((q_rel_aux[0], q_rel_aux[1]))



# print('strokeWeight(4)')
#
# for k in range(len(funcs)):
#     for i in range(len(lin_cart_p)):
#         print('if (int(fun) ==', k, '){')
#         print('stroke', colors[
#                   modfun(tal[funcs[k][0]], tal[funcs[k][1]], tal[funcs[k][2]], tal[funcs[k][3]], tal[funcs[k][4]],
#                            tal[funcs[k][5]], tal[funcs[k][6]], lin_cart_p[i], lin_cart_q[i])])
#         print('line', p_rplace[i] + q_rplace[i])
#         print('}')

#

# for i in range(len(p_rplace)):
#     print('stroke', colors[lin_cart_p[i]])
#     print('strokeWeight(10)')
#     print('point', p_rplace[i])
#
# for i in range(len(q_rplace)):
#     print('stroke', colors[lin_cart_q[i]])
#     print('strokeWeight(10)')
#     print('point', q_rplace[i])
