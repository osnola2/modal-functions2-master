from Tesseract.tesseract import *  # This is exactly as binary functions, except that it imports tesseract
# instead of basic functions


def falsum(prop1, prop2):
    return 0


def verum(prop1, prop2):
    return 1


def disj(prop1, prop2):
    return neg(conj(neg(prop1), neg(prop2)))


def imp(prop1, prop2):
    return disj(neg(prop1), prop2)


def cimp(prop1, prop2):
    return imp(prop2, prop1)


def eq(prop1, prop2):
    return conj(imp(prop1, prop2), cimp(prop1, prop2))


def xor(prop1, prop2):
    return eq(neg(prop1), prop2)


def nimp(prop1, prop2):
    return neg(imp(prop1, prop2))


def ncimp(prop1, prop2):
    return neg(cimp(prop1, prop2))


def pr1(prop1, prop2):
    return prop1


def pr2(prop1, prop2):
    return prop2


def neg1(prop1, prop2):
    return neg(prop1)


def neg2(prop1, prop2):
    return neg(prop2)


def shef(prop1, prop2):
    return neg(conj(prop1, prop2))


def peir(prop1, prop2):
    return neg(disj(prop1, prop2))


tau2 = [falsum, peir, ncimp, neg1, nimp, neg2, xor, shef, conj, eq, pr2, imp, pr1, cimp, disj, verum]

K = [[0], [1], [[0, 1], [1, 0]], [[0, 0], [0, 1], [1, 1]],
     [[0, 0, 0, 0], [0, 0, 1, 1], [0, 1, 0, 1], [0, 1, 1, 0], [1, 0, 0, 1], [1, 0, 1, 0], [1, 1, 0, 0], [1, 1, 1, 1]],
     [6], [0, 66, 1], [6, 66], [[0, 0], [0, 6], [0, 66], [1, 1]], [[0, 0], [1, 6], [1, 66], [1, 1]],
     [[0, 0], [0, 6], [1, 66], [1, 1]], [[0, 0], [0, 6], [0, 66], [1, 6], [1, 66], [1, 1]],
     [[0, 0], [0, 6], [0, 66], [0, 1], [1, 0], [1, 1]], [[0, 0], [0, 1], [1, 0], [1, 6], [1, 66], [1, 1]],
     [[0, 0], [0, 1], [6, 6], [66, 66], [1, 0], [1, 1]],
     [[0, 0], [0, 1], [6, 6], [6, 66], [66, 6], [66, 66], [1, 0], [1, 1]],
     [[0, 0], [6, 6], [6, 66], [66, 6], [66, 66], [1, 1]],
     [[0, 0], [0, 6], [0, 66], [0, 1], [6, 0], [6, 1], [66, 0], [66, 1], [1, 0], [1, 6], [1, 66], [1, 1]],
     [[0, 0, 0], [0, 0, 1], [0, 6, 0], [0, 66, 0], [0, 1, 0], [0, 1, 1], [1, 0, 0], [1, 0, 1], [1, 6, 1], [1, 66, 1],
      [1, 1, 0], [1, 1, 1]],
     [[0, 0, 0], [0, 6, 0], [0, 6, 1], [0, 66, 0], [0, 66, 1], [0, 1, 0], [1, 0, 1], [1, 6, 0], [1, 6, 1], [1, 66, 0],
      [1, 66, 1], [1, 1, 1]],
     [0, 6, 33, 3, 66, 1], [[0, 0], [6, 66], [33, 66], [22, 66], [2, 6], [3, 6], [66, 6], [1, 1]],
     [[0, 0], [6, 6], [33, 3], [22, 2], [2, 22], [3, 33], [66, 66], [1, 1]],
     [[0, 0], [6, 66], [33, 2], [22, 3], [2, 33], [3, 22], [66, 6], [1, 1]],
     [0, 6, 88, 8, 66, 1], [0, 6, 7, 88, 8, 77, 66, 1]]
