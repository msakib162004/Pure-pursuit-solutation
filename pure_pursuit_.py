# -*- coding: utf-8 -*-
"""Pure pursuit .ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Ir-XOGuhRsa_L2zbA-AKE-Me4-0oimOJ
"""

import numpy as np
import matplotlib.pyplot as plt

position_of_a = [0, 0]
position_of_b = [10000, 10000]
va = 60
attack_distance = 1000
time_limit = 300
deltaT = 2
vb = 50
deltaS = va*deltaT
aX = []
aY = []
bX = []
bY = []
aX.append(position_of_a[0])
aY.append(position_of_a[1])
bX.append(position_of_b[0])
bY.append(position_of_b[1])
while time_limit != 0:
    point1 = np.array((position_of_a[0], position_of_a[1]))
    point2 = np.array((position_of_b[0], position_of_b[1]))
    dist = np.linalg.norm(point1 - point2)
    print(position_of_a)
    print(position_of_b)
    print(f'========Distance: {dist}======')
    if dist <= attack_distance:
        print("A attacked B")
        break
    cos_theta = (position_of_b[0] - position_of_a[0]) / dist
    sin_theta = (position_of_b[1] - position_of_a[1]) / dist
    delta_X = cos_theta*deltaS
    delta_Y = sin_theta*deltaS

    aX.append(position_of_a[0]+((position_of_b[0] - position_of_a[0]) / dist)*va*deltaT)
    aY.append(position_of_a[1]+((position_of_b[1] - position_of_a[1]) / dist)*va*deltaT)

    bX.append(position_of_b[0]+(vb*deltaT))
    bY.append(position_of_b[1])

    position_of_a[0] = position_of_a[0]+delta_X
    position_of_a[1] = position_of_a[1]+delta_Y

    position_of_b[0] = position_of_b[0] - (vb*deltaT)
    #position_of_b[1] = position_of_b[1]

    time_limit = time_limit - 2


print(aX)
print(aY)
print(bX)
print(bY)


plt.scatter(aX, aY)
plt.scatter(bX, bY)

import numpy as np
import matplotlib.pyplot as plt

position_of_a = [0, 1000]
position_of_b = [12000, 2000]
position_of_c = [10000, 10000]
position_of_d = [5000, 15000]
va = 60
vb = 60
vc = 60
vd = 60
attack_distance = 1000
time_limit = 300
deltaT = 2

deltaS = va*deltaT
aX = []
aY = []
bX = []
bY = []

cX = []
cY = []
dX = []
dY = []


aX.append(position_of_a[0])
aY.append(position_of_a[1])
bX.append(position_of_b[0])
bY.append(position_of_b[1])
cX.append(position_of_c[0])
cY.append(position_of_c[1])
dX.append(position_of_d[0])
dY.append(position_of_d[1])

flag = True

while time_limit != 0:
    point1 = np.array((position_of_a[0], position_of_a[1]))
    point2 = np.array((position_of_b[0], position_of_b[1]))
    dist = np.linalg.norm(point1 - point2)

    point3 = np.array((position_of_b[0], position_of_b[1]))
    point4 = np.array((position_of_c[0], position_of_c[1]))
    dist1 = np.linalg.norm(point3 - point4)

    point5 = np.array((position_of_c[0], position_of_c[1]))
    point6 = np.array((position_of_d[0], position_of_d[1]))
    dist2 = np.linalg.norm(point5 - point6)

    print(position_of_a)
    print(position_of_b)
    print(position_of_c)
    print(position_of_d)

    print(f'========Distance A to B: {dist}======')
    print(f'========Distance B to C: {dist1}======')
    print(f'========Distance C to D: {dist2}======')
    if dist <= attack_distance:
        print("A attacked B")
        flag = False
        break
    elif dist1 <= attack_distance:
        print("B attacked C")
        flag = False
        break
    elif dist2 <= attack_distance:
        print("C attacked D")
        flag = False
        break
    cos_theta = (position_of_b[0] - position_of_a[0]) / dist
    sin_theta = (position_of_b[1] - position_of_a[1]) / dist
    delta_X = cos_theta*deltaS
    delta_Y = sin_theta*deltaS

    aX.append(position_of_a[0]+((position_of_b[0] - position_of_a[0]) / dist)*va*deltaT)
    aY.append(position_of_a[1]+((position_of_b[1] - position_of_a[1]) / dist)*va*deltaT)

    position_of_a[0] = position_of_a[0]+delta_X
    position_of_a[1] = position_of_a[1]+delta_Y

    position_of_b[0] = position_of_b[0] + ((position_of_c[0] - position_of_b[0]) / dist1)*(deltaT*vb)
    position_of_b[1] = position_of_b[1] + ((position_of_c[1] - position_of_b[1]) / dist1)*(deltaT*vb)

    bX.append(position_of_b[0] + ((position_of_c[0] - position_of_b[0]) / dist1)*(deltaT*vb))
    bY.append(position_of_b[1] + ((position_of_c[1] - position_of_b[1]) / dist1)*(deltaT*vb))

    position_of_c[0] = position_of_c[0] + ((position_of_d[0] - position_of_c[0]) / dist2) * (deltaT * vc)
    position_of_c[1] = position_of_c[1] + ((position_of_d[1] - position_of_c[1]) / dist2) * (deltaT * vc)

    cX.append(position_of_c[0] + ((position_of_d[0] - position_of_c[0]) / dist2) * (deltaT * vc))
    cY.append(position_of_c[1] + ((position_of_d[1] - position_of_c[1]) / dist2) * (deltaT * vc))

    position_of_d[0] = position_of_d[0] - (deltaT * vd)

    dX.append(position_of_d[0] - (deltaT * vd))
    dY.append(position_of_d[1])

    #position_of_d[1] = position_of_b[1] + ((position_of_b[1] - position_of_c[1]) / dist1) * (deltaT * vb)

    time_limit = time_limit - 2


print(aX)
print(aY)
print(bX)
print(bY)
print(cX)
print(cY)
print(dX)
print(dY)

if flag:
  print("Out of attack range. Attack not possiable from A to B or B to C or C to D.")

plt.scatter(aX, aY)
plt.scatter(bX, bY)
plt.scatter(cX, cY)
plt.scatter(dX, dY)