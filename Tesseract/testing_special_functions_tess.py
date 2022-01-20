from Tesseract.special_functions_tess import *


for f in spec_fun:
    for i in K[0]:
        for j in K[0]:
            if (f(i, j)) not in K[0]:
                print('test0',K,  f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[0]:
        if (f(i)) not in K[0]:
                print('test0', f.__name__, i, f(i))


for f in spec_fun_3:
    for i in K[0]:
        for j in K[0]:
            for k in K[0]:
                if (f(i, j, k)) not in K[0]:
                    print('test0', f.__name__, i, j, k, f(i, j, k))



for f in spec_fun:
    for i in K[1]:
        for j in K[1]:
            if (f(i, j)) not in K[1]:
                print('test1', f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[1]:
        if (f(i)) not in K[1]:
                print('test1', f.__name__, i, f(i))

for f in spec_fun_3:
    for i in K[1]:
        for j in K[1]:
            for k in K[1]:
                if (f(i, j, k)) not in K[1]:
                    print('test0', f.__name__, i, j, k, f(i, j, k))


for f in spec_fun:
    for i in K[2]:
        for j in K[2]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[2]:
                print('test2', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[2]:
       if ([f(i[0]), f(i[1])]) not in K[2]:
                print('test2', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[2]:
        for j in K[2]:
            for k in K[2]:
                if ([f(i[0], j[0], k[0]),f(i[1], j[1], k[1])]) not in K[2]:
                    print('test2', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[3]:
        for j in K[3]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[3]:
                print('test3', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[3]:
       if ([f(i[0]), f(i[1])]) not in K[3]:
                print('test3', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[3]:
        for j in K[3]:
            for k in K[3]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1])]) not in K[3]:
                    print('test3', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[4]:
        for j in K[4]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1]),
                 f(i[2], j[2]),
                 f(i[3], j[3])]) not in K[4]:
                print('test4', f.__name__,
                      i[0], j[0], i[1], j[1], i[2], j[2], i[3], j[3],
                      f(i[0], j[0]), f(i[1], j[1]), f(i[2], j[2]), f(i[3], j[3]))

for f in spec_fun_1:
    for i in K[4]:
         if ([f(i[0]), f(i[1]), f(i[2]), f(i[3])]) not in K[4]:
                print('test4', f.__name__,
                      i[0], i[1], i[2], i[3], f(i[0]), f(i[1]), f(i[2]), f(i[3]))

for f in spec_fun_3:
    for i in K[4]:
        for j in K[4]:
            for k in K[4]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1]), f(i[2], j[2], k[2]), f(i[3], j[3], k[3])]) not in K[4]:
                    print('test4', f.__name__,
                      i[0], j[0], k[0], i[1], j[1], k[1], i[2], j[2], i[3], j[3],
                      f(i[0], j[0], k[0]), f(i[1], j[1], k[1]), f(i[2], j[2], k[2]), f(i[3], j[3], k[3]))


for f in spec_fun:
    for i in K[5]:
        for j in K[5]:
            if (f(i, j)) not in K[5]:
                print('test5', f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[5]:
        if (f(i)) not in K[5]:
            print('test5', f.__name__, i, f(i))

for f in spec_fun_3:
    for i in K[5]:
        for j in K[5]:
            for k in K[5]:
                if (f(i, j, k)) not in K[5]:
                    print('test5', f.__name__, i, j, k, f(i, j, k))


for f in spec_fun:
    for i in K[6]:
        for j in K[6]:
            if (f(i, j)) not in K[6]:
                print('test6', f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[6]:
        if (f(i)) not in K[6]:
                print('test6', f.__name__, i, f(i))

for f in spec_fun_3:
    for i in K[6]:
        for j in K[6]:
            for k in K[6]:
                if (f(i, j, k)) not in K[6]:
                    print('test6', f.__name__, i, j, k, f(i, j, k))

for f in spec_fun:
    for i in K[7]:
        for j in K[7]:
            if (f(i, j)) not in K[7]:
                print('test7', f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[7]:
        if (f(i)) not in K[7]:
                print('test7', f.__name__, i, f(i))

for f in spec_fun_3:
    for i in K[7]:
        for j in K[7]:
            for k in K[7]:
                if (f(i, j, k)) not in K[7]:
                    print('test7', f.__name__, i, j, k, f(i, j, k))

for f in spec_fun:
    for i in K[8]:
        for j in K[8]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[8]:
                print('test8', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[8]:
       if ([f(i[0]), f(i[1])]) not in K[8]:
                print('test8', f.__name__, i[0], i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[8]:
        for j in K[8]:
            for k in K[8]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1])]) not in K[8]:
                    print('test8', f.__name__, i[0], j[0], k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))



for f in spec_fun:
    for i in K[9]:
        for j in K[9]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[9]:
                print('test9', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[9]:
       if ([f(i[0]), f(i[1])]) not in K[9]:
                print('test9', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[9]:
        for j in K[9]:
            for k in K[9]:
                if ([f(i[0], j[0], k[0]),
                 f(i[1], j[1], k[1])]) not in K[9]:
                    print('test9', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[10]:
        for j in K[10]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[10]:
                print('test10', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[10]:
       if ([f(i[0]), f(i[1])]) not in K[10]:
                print('test10', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[10]:
        for j in K[10]:
            for k in K[10]:
                if ([f(i[0], j[0], k[0]),
                 f(i[1], j[1], k[1])]) not in K[10]:
                    print('test10', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[11]:
        for j in K[11]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[11]:
                print('test11', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[11]:
        if ([f(i[0]), f(i[1])]) not in K[11]:
            print('test11', f.__name__, i[0], i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[11]:
        for j in K[11]:
            for k in K[11]:
                if ([f(i[0], j[0], k[0]), f(i[1], j[1], k[1])]) not in K[11]:
                    print('test11', f.__name__, i[0], j[0], k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[12]:
        for j in K[12]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[12]:
                print('test12', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[12]:
        if ([f(i[0]), f(i[1])]) not in K[12]:
            print('test12', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[12]:
        for j in K[12]:
            for k in K[12]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[12]:
                    print('test12', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[13]:
        for j in K[13]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[13]:
                print('test13', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[13]:
        if ([f(i[0]), f(i[1])]) not in K[13]:
            print('test13', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[13]:
        for j in K[13]:
            for k in K[13]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[13]:
                    print('test13', f.__name__, i[0], j[0], k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[14]:
        for j in K[14]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[14]:
                print('test14', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[14]:
        if ([f(i[0]), f(i[1])]) not in K[14]:
            print('test14', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[14]:
        for j in K[14]:
            for k in K[14]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[14]:
                    print('test14', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))



for f in spec_fun:
    for i in K[15]:
        for j in K[15]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[15]:
                print('test15', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[15]:
       if ([f(i[0]), f(i[1])]) not in K[15]:
                print('test15', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[15]:
        for j in K[15]:
            for k in K[15]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[15]:
                    print('test15', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))



for f in spec_fun:
    for i in K[16]:
        for j in K[16]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[16]:
                print('test16', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[16]:
       if ([f(i[0]), f(i[1])]) not in K[16]:
                print('test16', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[16]:
        for j in K[16]:
            for k in K[16]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[16]:
                    print('test16', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))



for f in spec_fun:
    for i in K[17]:
        for j in K[17]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[17]:
                print('test17', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[17]:
       if ([f(i[0]), f(i[1])]) not in K[17]:
                print('test17', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[17]:
        for j in K[17]:
            for k in K[17]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[17]:
                    print('test17', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))



for f in spec_fun:
    for i in K[18]:
        for j in K[18]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1]),
                 f(i[2], j[2])]) not in K[18]:
                print('test18', f.__name__,
                      i[0], j[0], i[1], j[1], i[2], j[2],
                      f(i[0], j[0]), f(i[1], j[1]), f(i[2], j[2]))

for f in spec_fun_1:
    for i in K[18]:
         if ([f(i[0]), f(i[1]), f(i[2])]) not in K[18]:
                print('test18', f.__name__,
                      i[0], i[1], i[2], f(i[0]), f(i[1]), f(i[2]))

for f in spec_fun_3:
    for i in K[18]:
        for j in K[18]:
            for k in K[18]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1]),
                     f(i[2], j[2], k[2])]) not in K[18]:
                    print('test18', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], i[2], j[2], k[2],
                          f(i[0], j[0], k[0]), f(i[1], j[1], k[1]), f(i[2], j[2], k[2]))



for f in spec_fun:
    for i in K[19]:
        for j in K[19]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1]),
                 f(i[2], j[2])]) not in K[19]:
                print('test19', f.__name__,
                      i[0], j[0], i[1], j[1], i[2], j[2],
                      f(i[0], j[0]), f(i[1], j[1]), f(i[2], j[2]))

for f in spec_fun_1:
    for i in K[19]:
         if ([f(i[0]), f(i[1]), f(i[2])]) not in K[19]:
                print('test19', f.__name__,
                      i[0], i[1], i[2], f(i[0]), f(i[1]), f(i[2]))

for f in spec_fun_3:
    for i in K[19]:
        for j in K[19]:
            for k in K[19]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1]),
                     f(i[2], j[2], k[2])]) not in K[19]:
                    print('test19', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], i[2], j[2], k[2],
                          f(i[0], j[0], k[0]), f(i[1], j[1], k[1]), f(i[2], j[2], k[2]))


for f in spec_fun:
    for i in K[20]:
        for j in K[20]:
            if (f(i, j)) not in K[20]:
                print('test20', f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[20]:
        if (f(i)) not in K[20]:
                print('test20', f.__name__, i, f(i))

for f in spec_fun_3:
    for i in K[20]:
        for j in K[20]:
            for k in K[20]:
                if (f(i, j, k)) not in K[20]:
                    print('test0', f.__name__, i, j, k, f(i, j, k))



for f in spec_fun:
    for i in K[21]:
        for j in K[21]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[21]:
                print('test21', f.__name__, i[0], j[0], i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[21]:
       if ([f(i[0]), f(i[1])]) not in K[21]:
                print('test21', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[21]:
        for j in K[21]:
            for k in K[21]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[21]:
                    print('test21', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[22]:
        for j in K[22]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[22]:
                print('test22', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[22]:
       if ([f(i[0]), f(i[1])]) not in K[22]:
                print('test22', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[22]:
        for j in K[22]:
            for k in K[22]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[22]:
                    print('test22', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[23]:
        for j in K[23]:
            if ([f(i[0], j[0]),
                 f(i[1], j[1])]) not in K[23]:
                print('test23', f.__name__, i[0], j[0],i[1], j[1], f(i[0], j[0]), f(i[1], j[1]))

for f in spec_fun_1:
    for i in K[23]:
       if ([f(i[0]), f(i[1])]) not in K[23]:
                print('test23', f.__name__, i[0],i[1], f(i[0]), f(i[1]))

for f in spec_fun_3:
    for i in K[23]:
        for j in K[23]:
            for k in K[23]:
                if ([f(i[0], j[0], k[0]),
                     f(i[1], j[1], k[1])]) not in K[23]:
                    print('test23', f.__name__, i[0], j[0],k[0], i[1], j[1], k[1], f(i[0], j[0], k[0]), f(i[1], j[1], k[1]))


for f in spec_fun:
    for i in K[24]:
        for j in K[24]:
            if (f(i, j)) not in K[24]:
                print('test24', f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[24]:
        if (f(i)) not in K[24]:
              print('test24', f.__name__, i, f(i))


for f in spec_fun_3:
    for i in K[24]:
        for j in K[24]:
            for k in K[24]:
                if (f(i, j, k)) not in K[24]:
                    print('test24', f.__name__, i, j, k, f(i, j, k))


for f in spec_fun:
    for i in K[25]:
        for j in K[25]:
            if (f(i, j)) not in K[25]:
                print('test25', f.__name__, i, j, f(i,j))

for f in spec_fun_1:
    for i in K[25]:
        if (f(i)) not in K[25]:
                print('test25', f.__name__, i, f(i))


for f in spec_fun_3:
    for i in K[25]:
        for j in K[25]:
            for k in K[25]:
                if (f(i, j, k)) not in K[25]:
                    print('test25', f.__name__, i, j, k, f(i, j, k))