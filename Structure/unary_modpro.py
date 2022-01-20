from special_functions import *

def pr1(prop1):
    return prop1

tau1 = [falsum1, neg, pr1, verum1]
full = {0, 1, 2, 3}
subsets = []

subsets.append(list(full))
for b in full:
    subsets.append(list(full-{b}))


for b in full:
    for c in full:
        if b != c:
            subsets.append(full-{b, c})

for b in full:
    subsets.append([b])


print(subsets)




def mod(f1, f2, prop1):
    if not rigid(prop1):
        return f1(prop1)
    if rigid(prop1):
        return f2(prop1)