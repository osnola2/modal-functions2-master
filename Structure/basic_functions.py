def conj(prop1, prop2):  # Here we define the basic operations of propositional modal logic. We call them basic because
    if prop1 == prop2:  # all other modal operations are defined in terms of these. Conj could be interpreted as the
        return prop1  # intersection of the subsets of a set of three elements, or the meet operation operations on the
    if prop1 == 0 or prop2 == 0:  # third-dimensional cube, or the conjunction relative to S5 models with three
        return 0                  # possible worlds.
    if prop1 == 1:                # box and neg (defined in lines 55 and 61) are pretty clear.
        return prop2              # The cube I'm referring to looks roughly like this:
    if prop2 == 1:                #                                1
        return prop1              #                           /    |    \
    if prop1 == 5 and prop2 == 4:  #                        6      4       9
        return 6
    if prop2 == 5 and prop1 == 4:  #                5              2              3
        return 6
    if prop1 == 5 and prop2 == 9:  #                               0
        return 2
    if prop2 == 5 and prop1 == 9:  # 1 is the three-elements set; 5, 4, 9 are the two-elements sets; 6, 2, 3 are the
        return 2                   # one-element sets, and 0 is the empty set.
    if prop1 == 5 and prop2 == 3:  # The complementarity relation is: 1, 0; 5, 3; 4, 2; 9, 6.
        return 0
    if prop2 == 5 and prop1 == 3:
        return 0
    if prop1 == 5 and prop2 in [6,2]:
        return prop2
    if prop2 == 5 and prop1 in [6,2]:
        return prop1
    if prop1 == 4 and prop2 == 9:
        return 3
    if prop2 == 4 and prop1 == 9:
        return 3
    if prop1 == 4 and prop2 == 2:
        return 0
    if prop2 == 4 and prop1 == 2:
        return 0
    if prop1 == 4 and prop2 in [6,3]:
        return prop2
    if prop2 == 4 and prop1 in [6,3]:
        return prop1
    if prop1 == 9 and prop2 == 6:
        return 0
    if prop2 == 9 and prop1 == 6:
        return 0
    if prop1 == 9 and prop2 in [2,3]:
        return prop2
    if prop2 == 9 and prop1 in [2,3]:
        return prop1
    if prop1 == 6 and prop2 in [2,3]:
        return 0
    if prop2 == 6 and prop1 in [2,3]:
        return 0
    if prop1 == 2 and prop2 == 3:
        return 0
    if prop2 == 2 and prop1 == 3:
        return 0

def box(prop1):
    if prop1 == 1:
        return 1
    else:
        return 0
    
def neg(prop1):
    if prop1 == 1:
        return 0
    if prop1 == 5:
        return 3
    if prop1 == 4:
        return 2
    if prop1 == 9:
        return 6
    if prop1 == 2:
        return 4
    if prop1 == 6:
        return 9
    if prop1 == 3:
        return 5
    if prop1 == 0:
        return 1

def diam(prop1):
    return(neg(box(neg(prop1))))

def falsum1(prop1):
    return 0

def verum1(prop1):
    return 1

atoms = [0, 2, 3, 4, 5, 6, 9, 1]
