from Structure.modalprofile import *


def modaux(prop1, prop2):
    if modpro(prop1, prop2) in [[0, 0, 0, 1], [1, 1, 1, 0]]:
        return 0
    if modpro(prop1, prop2) in [[0, 0, 1, 0], [1, 1, 0, 1]]:
        return 1
    if modpro(prop1, prop2) in [[0, 1, 0, 0], [1, 0, 1, 1]]:
        return 2
    if modpro(prop1, prop2) in [[1, 0, 0, 0], [0, 1, 1, 1]]:
        return 3
    if modpro(prop1, prop2) in [[0, 0, 1, 1], [1, 1, 0, 0]]:
        return 4
    if modpro(prop1, prop2) in [[0, 1, 0, 1], [1, 0, 1, 0]]:
        return 5
    if modpro(prop1, prop2) in [[1, 0, 0, 1], [0, 1, 1, 0]]:
        return 6