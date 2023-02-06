#!/usr/bin/env python
# coding: utf-8

#Reference: https://www.brown.edu/Departments/Engineering/Courses/EN224/anis_general/anis_general.htm

import numpy as np

thetaDegree = float(input("Enter the angle of rotation (in degrees) (counterclockwise is positive) :"))
theta = ((np.pi)/180.0)*thetaDegree
print(theta)

c = np.cos(theta)
s = np.sin(theta)

K1 = np.zeros((6,6))
K2 = np.zeros((6,6))
K3 = np.zeros((6,6))

K1[0,0] = 1
K1[1,1] = c**2
K1[1,2] = s**2
K1[1,3] = 2*c*s
K1[2,1] = s**2
K1[2,2] = c**2
K1[2,3] = -2*c*s
K1[3,1] = -c*s
K1[3,2] = c*s
K1[3,3] = c**2 - s**2
K1[4,4] = c
K1[4,5] = -s
K1[5,4] = s
K1[5,5] = c

K2[0,0] = c**2
K2[0,2] = s**2
K2[0,4] = 2*c*s
K2[1,1] = 1
K2[2,0] = s**2
K2[2,2] = c**2
K2[2,4] = -2*c*s
K2[3,3] = c
K2[3,5] = -s
K2[4,0] = -c*s
K2[4,2] = c*s
K2[4,4] = c**2 - s**2
K2[5,3] = s
K2[5,5] = c

K3[0,0] = c**2
K3[0,1] = s**2
K3[0,5] = 2*c*s
K3[1,0] = s**2
K3[1,1] = c**2
K3[1,5] = -2*c*s
K3[2,2] = 1
K3[3,3] = c
K3[3,4] = s
K3[4,3] = -s
K3[4,4] = c
K3[5,0] = -c*s
K3[5,1] = c*s
K3[5,5] = c**2 - s**2

K = K1@K2@K3

c11 = float(input("Enter C11 of the cubic system :"))
c12 = float(input("Enter C12 of the cubic system :"))
c44 = float(input("Enter C44 of the cubic system :"))

c = np.zeros((6,6))
c[0,0] = c11
c[1,1] = c[2,2] = c[0,0]
c[3,3] = c44
c[4,4] = c[5,5] = c[3,3]
c[0,1] = c[1,0] = c12
c[1,0] = c[1,2] = c12
c[2,0] = c[2,1] = c12

c_transformed = K@c@np.transpose(K)

print("Stiffness tensor in the new reference frame is ")
print(c_transformed)