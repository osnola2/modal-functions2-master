def conj(prop1, prop2):
    if prop1 == prop2:
        return prop1
    if prop1 == 0 or prop2 == 0:
        return 0
    if prop1 == 1:
        return prop2
    if prop2 == 1:
        return prop1
    if prop1 == 2 and prop2 == 3:
        return 6
    if prop2 == 2 and prop1 == 3:
        return 6
    if prop1 == 2 and prop2 == 4:
        return 7
    if prop2 == 2 and prop1 == 4:
        return 7
    if prop1 == 2 and prop2 == 5:
        return 8
    if prop2 == 2 and prop1 == 5:
        return 8
    if prop1 == 2 and prop2 in [6, 7, 8]:
        return prop2
    if prop2 == 2 and prop1 in [6, 7, 8]:
        return prop1
    if prop1 == 2 and prop2 == 88:
        return 55
    if prop2 == 2 and prop1 == 88:
        return 55
    if prop1 == 2 and prop2 == 77:
        return 44
    if prop2 == 2 and prop1 == 77:
        return 44
    if prop1 == 2 and prop2 == 66:
        return 33
    if prop2 == 2 and prop1 == 66:
        return 33
    if prop1 == 2 and prop2 in [55, 44, 33]:
        return prop2
    if prop2 == 2 and prop1 in [55, 44, 33]:
        return prop1
    if prop1 == 2 and prop2 == 22:
        return 0
    if prop2 == 2 and prop1 == 22:
        return 0
    if prop1 == 3 and prop2 == 4:
        return 88
    if prop2 == 3 and prop1 == 4:
        return 88
    if prop1 == 3 and prop2 == 5:
        return 77
    if prop2 == 3 and prop1 == 5:
        return 77
    if prop1 == 3 and prop2 in [6, 88, 77]:
        return prop2
    if prop2 == 3 and prop1 in [6, 88, 77]:
        return prop1
    if prop1 == 3 and prop2 == 7:
        return 55
    if prop2 == 3 and prop1 == 7:
        return 55
    if prop1 == 3 and prop2 == 8:
        return 44
    if prop2 == 3 and prop1 == 8:
        return 44
    if prop1 == 3 and prop2 == 66:
        return 22
    if prop2 == 3 and prop1 == 66:
        return 22
    if prop1 == 3 and prop2 in [55, 44, 22]:
        return prop2
    if prop2 == 3 and prop1 in [55, 44, 22]:
        return prop1
    if prop1 == 3 and prop2 == 33:
        return 0
    if prop2 == 3 and prop1 == 33:
        return 0
    if prop1 == 4 and prop2 == 5:
        return 66
    if prop2 == 4 and prop1 == 5:
        return 66
    if prop1 == 4 and prop2 in [7, 88, 66]:
        return prop2
    if prop2 == 4 and prop1 in [7, 88, 66]:
        return prop1
    if prop1 == 4 and prop2 == 6:
        return 55
    if prop2 == 4 and prop1 == 6:
        return 55
    if prop1 == 4 and prop2 == 8:
        return 44
    if prop2 == 4 and prop1 == 8:
        return 44
    if prop1 == 4 and prop2 == 77:
        return 22
    if prop2 == 4 and prop1 == 77:
        return 22
    if prop1 == 4 and prop2 in [55, 33, 22]:
        return prop2
    if prop2 == 4 and prop1 in [55, 33, 22]:
        return prop1
    if prop1 == 4 and prop2 == 44:
        return 0
    if prop2 == 4 and prop1 == 44:
        return 0
    if prop1 == 5 and prop2 in [8, 77, 66]:
        return prop2
    if prop2 == 5 and prop1 in [8, 77, 66]:
        return prop1
    if prop1 == 5 and prop2 == 6:
        return 44
    if prop2 == 5 and prop1 == 6:
        return 44
    if prop1 == 5 and prop2 == 7:
        return 33
    if prop2 == 5 and prop1 == 7:
        return 33
    if prop1 == 5 and prop2 == 88:
        return 22
    if prop2 == 5 and prop1 == 88:
        return 22
    if prop1 == 5 and prop2 in [44, 33, 22]:
        return prop2
    if prop2 == 5 and prop1 in [44, 33, 22]:
        return prop1
    if prop1 == 5 and prop2 == 55:
        return 0
    if prop2 == 5 and prop1 == 55:
        return 0
    if prop1 == 6 and prop2 == 7:
        return 55
    if prop2 == 6 and prop1 == 7:
        return 55
    if prop1 == 6 and prop2 == 8:
        return 44
    if prop2 == 6 and prop1 == 8:
        return 44
    if prop1 == 6 and prop2 == 88:
        return 55
    if prop2 == 6 and prop1 == 88:
        return 55
    if prop1 == 6 and prop2 == 77:
        return 44
    if prop2 == 6 and prop1 == 77:
        return 44
    if prop1 == 6 and prop2 == 66:
        return 0
    if prop2 == 6 and prop1 == 66:
        return 0
    if prop1 == 6 and prop2 in [55, 44]:
        return prop2
    if prop2 == 6 and prop1 in [55, 44]:
        return prop1
    if prop1 == 6 and prop2 == 33:
        return 0
    if prop2 == 6 and prop1 == 33:
        return 0
    if prop1 == 6 and prop2 == 22:
        return 0
    if prop2 == 6 and prop1 == 22:
        return 0
    if prop1 == 7 and prop2 == 8:
        return 33
    if prop2 == 7 and prop1 == 8:
        return 33
    if prop1 == 7 and prop2 == 88:
        return 55
    if prop2 == 7 and prop1 == 88:
        return 55
    if prop1 == 7 and prop2 == 77:
        return 0
    if prop2 == 7 and prop1 == 77:
        return 0
    if prop1 == 7 and prop2 == 66:
        return 33
    if prop2 == 7 and prop1 == 66:
        return 33
    if prop1 == 7 and prop2 in [55, 33]:
        return prop2
    if prop2 == 7 and prop1 in [55, 33]:
        return prop1
    if prop1 == 7 and prop2 == 44:
        return 0
    if prop2 == 7 and prop1 == 44:
        return 0
    if prop1 == 7 and prop2 == 22:
        return 0
    if prop2 == 7 and prop1 == 22:
        return 0
    if prop1 == 8 and prop2 == 88:
        return 0
    if prop2 == 8 and prop1 == 88:
        return 0
    if prop1 == 8 and prop2 == 77:
        return 44
    if prop2 == 8 and prop1 == 77:
        return 44
    if prop1 == 8 and prop2 == 66:
        return 33
    if prop2 == 8 and prop1 == 66:
        return 33
    if prop1 == 8 and prop2 in [44, 33]:
        return prop2
    if prop2 == 8 and prop1 in [44, 33]:
        return prop1
    if prop1 == 8 and prop2 == 55:
        return 0
    if prop2 == 8 and prop1 == 55:
        return 0
    if prop1 == 8 and prop2 == 22:
        return 0
    if prop2 == 8 and prop1 == 22:
        return 0
    if prop1 == 88 and prop2 == 77:
        return 22
    if prop2 == 88 and prop1 == 77:
        return 22
    if prop1 == 88 and prop2 == 66:
        return 22
    if prop2 == 88 and prop1 == 66:
        return 22
    if prop1 == 88 and prop2 in [55, 22]:
        return prop2
    if prop2 == 88 and prop1 in [55, 22]:
        return prop1
    if prop1 == 88 and prop2 == 44:
        return 0
    if prop2 == 88 and prop1 == 44:
        return 0
    if prop1 == 88 and prop2 == 33:
        return 0
    if prop2 == 88 and prop1 == 33:
        return 0
    if prop1 == 77 and prop2 == 66:
        return 22
    if prop2 == 77 and prop1 == 66:
        return 22
    if prop1 == 77 and prop2 in [44, 22]:
        return prop2
    if prop2 == 77 and prop1 in [44, 22]:
        return prop1
    if prop1 == 77 and prop2 == 55:
        return 0
    if prop2 == 77 and prop1 == 55:
        return 0
    if prop1 == 77 and prop2 == 33:
        return 0
    if prop2 == 77 and prop1 == 33:
        return 0
    if prop1 == 66 and prop2 == 55:
        return 0
    if prop2 == 66 and prop1 == 55:
        return 0
    if prop1 == 66 and prop2 == 44:
        return 0
    if prop2 == 66 and prop1 == 44:
        return 0
    if prop1 == 66 and prop2 in [33, 22]:
        return prop2
    if prop2 == 66 and prop1 in [33, 22]:
        return prop1
    if prop1 == 55 and prop2 in [44, 33, 22]:
        return 0
    if prop2 == 55 and prop1 in [44, 33, 22]:
        return 0
    if prop1 == 44 and prop2 in [33, 22]:
        return 0
    if prop2 == 44 and prop1 in [33, 22]:
        return 0
    if prop1 == 33 and prop2 == 22:
        return 0
    if prop2 == 33 and prop1 == 22:
        return 0


def box(prop1):
    if prop1 == 1:
        return 1
    else:
        return 0


def neg(prop1):
    if prop1 == 0:
        return 1
    if prop1 == 1:
        return 0
    if prop1 == 2:
        return 22
    if prop1 == 3:
        return 33
    if prop1 == 4:
        return 44
    if prop1 == 5:
        return 55
    if prop1 == 6:
        return 66
    if prop1 == 7:
        return 77
    if prop1 == 8:
        return 88
    if prop1 == 88:
        return 8
    if prop1 == 77:
        return 7
    if prop1 == 66:
        return 6
    if prop1 == 55:
        return 5
    if prop1 == 44:
        return 4
    if prop1 == 33:
        return 3
    if prop1 == 22:
        return 2



def diam(prop1):
    return (neg(box(neg(prop1))))


atoms = [0, 2, 3, 4, 5, 6, 7, 8, 88, 77, 66, 55, 44, 33, 22, 1]