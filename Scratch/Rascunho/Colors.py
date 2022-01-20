a = []
b = []

# for i in range(51):
#     for j in range(51):
#         for k in range(51):
#             if i*5 + j*5 + k*5 == 255*2:
#                 if 255-i >= 0:
#                     if 255 - j >= 0:
#                         if 255 - k >= 0:
#                             a.append(i*5 + j*5 + k*5)
#                             print('if (int(number) ==', len(a), '){')
#                             print('fill', (i*5, j*5, k*5, 220))
#                             print('circle', (100, 100, 120))
#                             print('fill', (255 - i*5, 255 - j*5, 255 - k*5, 220))
#                             print('circle', (100, 200, 120))
#                             print('}')

for i in range(256):
    for j in range(256):
        for k in range(256):
            if i + j + k == (255*3):
                a.append(i + j + k)
                print('if (int(number) ==', len(a), '){')
                print('fill', (i, j, k, 220))
                print('circle', (100, 100, 120))
                print('fill', (255 - i, 255 - j, 255 - k, 220))
                print('circle', (100, 200, 120))
                print('}')



