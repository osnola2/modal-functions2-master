from Structure.modal_functions import *
from Polymorphisms.pi21_first_third import *
from Structure.taumodels import *
import time


t0 = time.time()
for f in pi_21_a:
    a = []
    for i in K[0]:
        for j in K[0]:
            if modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i, j) not in K[0]:
                a.append(0)
    for i in K[1]:
        for j in K[1]:
            if modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i, j) not in K[1]:
                a.append(1)
    for i in K[2]:
        for j in K[2]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[2]:
                a.append(2)
    for i in K[3]:
        for j in K[3]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[3]:
                a.append(3)
    for i in K[4]:
        for j in K[4]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[2], j[2]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[3], j[3])]\
                    not in K[4]:
                a.append(4)
    for i in K[5]:
        for j in K[5]:
            if modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i, j) not in K[5]:
                a.append(5)
    for i in K[6]:
        for j in K[6]:
            if modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i, j) not in K[6]:
                a.append(6)
    for i in K[7]:
        for j in K[7]:
            if modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i, j) not in K[7]:
                a.append(7)
    for i in K[8]:
        for j in K[8]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[8]:
                a.append(8)
    for i in K[9]:
        for j in K[9]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[9]:
                a.append(9)
    for i in K[10]:
        for j in K[10]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[10]:
                a.append(10)
    for i in K[11]:
        for j in K[11]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[11]:
                a.append(11)
    for i in K[12]:
        for j in K[12]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[12]:
                a.append(12)
    for i in K[13]:
        for j in K[13]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[13]:
                a.append(13)
    for i in K[14]:
        for j in K[14]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[14]:
                a.append(14)
    for i in K[15]:
        for j in K[15]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[15]:
                a.append(15)
    for i in K[16]:
        for j in K[16]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[16]:
                a.append(16)
    for i in K[17]:
        for j in K[17]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[17]:
                a.append(17)
    for i in K[18]:
        for j in K[18]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[2], j[2])] \
                    not in K[18]:
                a.append(18)
    for i in K[19]:
        for j in K[19]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[2], j[2])] \
                    not in K[19]:
                a.append(19)
    for i in K[20]:
        for j in K[20]:
            if modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i, j) not in K[20]:
                a.append(20)
    for i in K[21]:
        for j in K[21]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[21]:
                a.append(21)
    for i in K[22]:
        for j in K[22]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[22]:
                a.append(22)
    for i in K[23]:
        for j in K[23]:
            if [modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[0], j[0]),
                modfun(tal[f[0]], tal[f[1]], tal[f[2]], tal[f[3]], tal[f[4]], tal[f[5]], tal[f[6]], i[1], j[1])]\
                    not in K[23]:
                a.append(23)
    # if set(a) in [{7, 8, 9, 10, 11, 16, 19, 22}, {7, 8, 9, 10, 11, 16, 18, 19, 22}, {7, 8, 9, 10, 11, 13, 16, 18, 19, 22},
    #               {2, 7, 8, 9, 10, 11, 13, 16, 18, 19, 22}, {2, 7, 8, 9, 10, 11, 13, 16, 18, 19},
    #               {2, 7, 8, 9, 10, 11, 13, 16, 18}, {2, 7, 8, 9, 10, 11, 13, 16}, {2, 7, 8, 9, 10, 11, 16},
    #               {2, 7, 8, 9, 10, 16}, {2, 7, 8, 9, 16}, {2, 7, 8, 16}, {2, 7, 16}, {2, 16}, {7, 16},
    #                 {8, 9, 10, 11, 16, 19, 22}, {8, 9, 10, 11, 16, 22}, {8, 9, 11, 16, 22}, {8, 9, 11, 16},
    #               {9, 11, 16}, {11, 16}, {16}, {16, 18, 22}, {16, 22}, {16, 18}, {5, 16, 18}]:
    #     print(f)
    if 16 in set(a):
        if len(set(a)) <= 11:
            print(f, set(a))


t1 = time.time()
print(t1-t0)
print(len(pi_21_a))
