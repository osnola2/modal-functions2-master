from special_functions import *
from supendem_all import *

spec_fun_1 = [falsum1]
spec_fun = []
spec_fun_3 = []


a = []

for f in spec_fun:
    for i in K[0]:
        for j in K[0]:
            if (f(i, j)) not in K[0]:
                a.append(0)

for f in spec_fun_1:
    for i in K[0]:
        if (f(i)) not in K[0]:
            a.append(0)


for f in spec_fun_3:
    for i in K[0]:
        for j in K[0]:
            for k in K[0]:
                if (f(i, j, k)) not in K[0]:
                    a.append(0)


for f in spec_fun:
    for i in K[1]:
        for j in K[1]:
            if (f(i, j)) not in K[1]:
                a.append(1)

for f in spec_fun_1:
    for i in K[1]:
        if (f(i)) not in K[1]:
            a.append(1)

for f in spec_fun_3:
    for i in K[1]:
        for j in K[1]:
            for k in K[1]:
                if (f(i, j, k)) not in K[1]:
                    a.append(1)


for f in spec_fun:
    for i in K[2]:
        for j in K[2]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[2]:
                a.append(2)

for f in spec_fun_1:
    for i in K[2]:
        if ([f(i[0]), f(i[1])]) not in K[2]:
            a.append(2)

for f in spec_fun_3:
    for i in K[2]:
        for j in K[2]:
            for k in K[2]:
                if ([f(i[0], j[0], k[0]),f(i[1], j[1], k[1])]) not in K[2]:
                    a.append(2)

for f in spec_fun:
    for i in K[3]:
        for j in K[3]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[3]:
                a.append(3)

for f in spec_fun_1:
    for i in K[3]:
       if ([f(i[0]), f(i[1])]) not in K[3]:
                a.append(3)

for f in spec_fun_3:
    for i in K[3]:
        for j in K[3]:
            for k in K[3]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1])]) not in K[3]:
                    a.append(3)


for f in spec_fun:
    for i in K[4]:
        for j in K[4]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1]),
                 f(i[2], j[2]),
                 f(i[3], j[3])]) not in K[4]:
                a.append(4)

for f in spec_fun_1:
    for i in K[4]:
         if ([f(i[0]), f(i[1]), f(i[2]), f(i[3])]) not in K[4]:
                a.append(4)

for f in spec_fun_3:
    for i in K[4]:
        for j in K[4]:
            for k in K[4]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1]), f(i[2], j[2], k[2]), f(i[3], j[3], k[3])]) not in K[4]:
                    a.append(4)


for f in spec_fun:
    for i in K[5]:
        for j in K[5]:
            if (f(i, j)) not in K[5]:
                a.append(5)

for f in spec_fun_1:
    for i in K[5]:
        if (f(i)) not in K[5]:
            a.append(5)

for f in spec_fun_3:
    for i in K[5]:
        for j in K[5]:
            for k in K[5]:
                if (f(i, j, k)) not in K[5]:
                    a.append(5)


for f in spec_fun:
    for i in K[6]:
        for j in K[6]:
            if (f(i, j)) not in K[6]:
                a.append(6)

for f in spec_fun_1:
    for i in K[6]:
        if (f(i)) not in K[6]:
                a.append(6)

for f in spec_fun_3:
    for i in K[6]:
        for j in K[6]:
            for k in K[6]:
                if (f(i, j, k)) not in K[6]:
                    a.append(6)

for f in spec_fun:
    for i in K[7]:
        for j in K[7]:
            if (f(i, j)) not in K[7]:
                a.append(7)

for f in spec_fun_1:
    for i in K[7]:
        if (f(i)) not in K[7]:
                a.append(7)

for f in spec_fun_3:
    for i in K[7]:
        for j in K[7]:
            for k in K[7]:
                if (f(i, j, k)) not in K[7]:
                    a.append(7)

for f in spec_fun:
    for i in K[8]:
        for j in K[8]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[8]:
                a.append(8)

for f in spec_fun_1:
    for i in K[8]:
       if ([f(i[0]), f(i[1])]) not in K[8]:
                a.append(8)

for f in spec_fun_3:
    for i in K[8]:
        for j in K[8]:
            for k in K[8]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1])]) not in K[8]:
                    a.append(8)


for f in spec_fun:
    for i in K[9]:
        for j in K[9]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[9]:
                a.append(9)


for f in spec_fun_1:
    for i in K[9]:
       if ([f(i[0]), f(i[1])]) not in K[9]:
                a.append(9)

for f in spec_fun_3:
    for i in K[9]:
        for j in K[9]:
            for k in K[9]:
                if ([f(i[0], j[0], k[0]),
                 f(i[1], j[1], k[1])]) not in K[9]:
                    a.append(9)


for f in spec_fun:
    for i in K[10]:
        for j in K[10]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[10]:
                a.append(10)

for f in spec_fun_1:
    for i in K[10]:
       if ([f(i[0]), f(i[1])]) not in K[10]:
                a.append(10)

for f in spec_fun_3:
    for i in K[10]:
        for j in K[10]:
            for k in K[10]:
                if ([f(i[0], j[0], k[0]),
                 f(i[1], j[1], k[1])]) not in K[10]:
                    a.append(10)


for f in spec_fun:
    for i in K[11]:
        for j in K[11]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[11]:
                a.append(11)

for f in spec_fun_1:
    for i in K[11]:
        if ([f(i[0]), f(i[1])]) not in K[11]:
            a.append(11)

for f in spec_fun_3:
    for i in K[11]:
        for j in K[11]:
            for k in K[11]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1])]) not in K[11]:
                    a.append(11)


for f in spec_fun:
    for i in K[12]:
        for j in K[12]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[12]:
                a.append(12)

for f in spec_fun_1:
    for i in K[12]:
        if ([f(i[0]), f(i[1])]) not in K[12]:
            a.append(12)

for f in spec_fun_3:
    for i in K[12]:
        for j in K[12]:
            for k in K[12]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[12]:
                    a.append(12)


for f in spec_fun:
    for i in K[13]:
        for j in K[13]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[13]:
                a.append(13)

for f in spec_fun_1:
    for i in K[13]:
        if ([f(i[0]), f(i[1])]) not in K[13]:
            a.append(13)

for f in spec_fun_3:
    for i in K[13]:
        for j in K[13]:
            for k in K[13]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[13]:
                    a.append(13)


for f in spec_fun:
    for i in K[14]:
        for j in K[14]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[14]:
                a.append(14)

for f in spec_fun_1:
    for i in K[14]:
        if ([f(i[0]), f(i[1])]) not in K[14]:
            a.append(14)

for f in spec_fun_3:
    for i in K[14]:
        for j in K[14]:
            for k in K[14]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[14]:
                    a.append(14)



for f in spec_fun:
    for i in K[15]:
        for j in K[15]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[15]:
                a.append(15)

for f in spec_fun_1:
    for i in K[15]:
       if ([f(i[0]), f(i[1])]) not in K[15]:
                a.append(15)

for f in spec_fun_3:
    for i in K[15]:
        for j in K[15]:
            for k in K[15]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[15]:
                    a.append(15)



for f in spec_fun:
    for i in K[16]:
        for j in K[16]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[16]:
                a.append(16)

for f in spec_fun_1:
    for i in K[16]:
       if ([f(i[0]), f(i[1])]) not in K[16]:
                a.append(16)

for f in spec_fun_3:
    for i in K[16]:
        for j in K[16]:
            for k in K[16]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[16]:
                    a.append(16)



for f in spec_fun:
    for i in K[17]:
        for j in K[17]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[17]:
                a.append(17)

for f in spec_fun_1:
    for i in K[17]:
       if ([f(i[0]), f(i[1])]) not in K[17]:
                a.append(17)

for f in spec_fun_3:
    for i in K[17]:
        for j in K[17]:
            for k in K[17]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[17]:
                    a.append(17)



for f in spec_fun:
    for i in K[18]:
        for j in K[18]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1]),
                 f(i[2], j[2])]) not in K[18]:
                a.append(18)

for f in spec_fun_1:
    for i in K[18]:
         if ([f(i[0]), f(i[1]), f(i[2])]) not in K[18]:
                a.append(18)

for f in spec_fun_3:
    for i in K[18]:
        for j in K[18]:
            for k in K[18]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1]),
                     f(i[2], j[2], k[2])]) not in K[18]:
                    a.append(18)



for f in spec_fun:
    for i in K[19]:
        for j in K[19]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1]),
                 f(i[2], j[2])]) not in K[19]:
                a.append(19)

for f in spec_fun_1:
    for i in K[19]:
         if ([f(i[0]), f(i[1]), f(i[2])]) not in K[19]:
                a.append(19)

for f in spec_fun_3:
    for i in K[19]:
        for j in K[19]:
            for k in K[19]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1]),
                     f(i[2], j[2], k[2])]) not in K[19]:
                    a.append(19)


for f in spec_fun:
    for i in K[20]:
        for j in K[20]:
            if (f(i, j)) not in K[20]:
                a.append(20)

for f in spec_fun_1:
    for i in K[20]:
        if (f(i)) not in K[20]:
                a.append(20)

for f in spec_fun_3:
    for i in K[20]:
        for j in K[20]:
            for k in K[20]:
                if (f(i, j, k)) not in K[20]:
                    a.append(20)



for f in spec_fun:
    for i in K[21]:
        for j in K[21]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[21]:
                a.append(21)

for f in spec_fun_1:
    for i in K[21]:
        if ([f(i[0]), f(i[1])]) not in K[21]:
            a.append(21)

for f in spec_fun_3:
    for i in K[21]:
        for j in K[21]:
            for k in K[21]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[21]:
                    a.append(21)


for f in spec_fun:
    for i in K[22]:
        for j in K[22]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[22]:
                a.append(22)

for f in spec_fun_1:
    for i in K[22]:
       if ([f(i[0]), f(i[1])]) not in K[22]:
                a.append(22)

for f in spec_fun_3:
    for i in K[22]:
        for j in K[22]:
            for k in K[22]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[22]:
                    a.append(22)


for f in spec_fun:
    for i in K[23]:
        for j in K[23]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[23]:
                a.append(23)

for f in spec_fun_1:
    for i in K[23]:
       if ([f(i[0]), f(i[1])]) not in K[23]:
                a.append(23)

for f in spec_fun_3:
    for i in K[23]:
        for j in K[23]:
            for k in K[23]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[23]:
                    a.append(23)

print(set(a))