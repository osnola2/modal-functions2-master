def val_to_num(seq):
    if seq == [1, 1, 1, 1]:
        return 15
    if seq == [0, 1, 1, 1]:
        return 14
    if seq == [1, 1, 1, 0]:
        return 13
    if seq == [0, 1, 1, 0]:
        return 12
    if seq == [1, 6, 9, 1]:
        return 11
    if seq == [0, 6, 9, 1]:
        return 10
    if seq == [1, 6, 9, 0]:
        return 9
    if seq == [0, 6, 9, 0]:
        return 8
    if seq == [1, 9, 6, 1]:
        return 7
    if seq == [0, 9, 6, 1]:
        return 6
    if seq == [1, 9, 6, 0]:
        return 5
    if seq == [0, 9, 6, 0]:
        return 4
    if seq == [1, 0, 0, 1]:
        return 3
    if seq == [0, 0, 0, 1]:
        return 2
    if seq == [1, 0, 0, 0]:
        return 1
    if seq == [0, 0, 0, 0]:
        return 0

