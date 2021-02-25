import math

diameter = 0.06
height = [1.2]
unit_weight = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
phi = [45]
ko = 0.42
f = 0.60
nqh = [65]     # Bearing capacity factor can be obtained from a graph. So need to input it manually.
Tu = 0

res = [[i, j, k] for i in height
       for j in unit_weight
       for k in phi]

for item in res:
    print(item)
for i in height:
    print('H/D= ')
    print(i/diameter)
for item in res:
    print('[Depth, Unit weight, Friction angle] ')
    print(item)
    if (item[1] < 13):
        pu_temp = 1000 * diameter * item[1] * item[0]
        for i in nqh:
            Pu = pu_temp * i
            print('Pu: ')
            print(Pu)

    if (item[1] >= 13):
        pu_temp = 1000 * diameter * item[1] * item[0]
        for i in nqh:
            Pu = 1.17203 * pu_temp * i
            print('Pu: ')
            print(Pu)
    Tu = 7.78586 * math.pi * 1000 * diameter * item[1] * item[0] * (1 + ko) / 2 * math.tan(math.radians(f * item[2]))
    print('Tu: ')
    print(Tu)