#!/usr/bin/env python
# coding: utf-8

import numpy as np


# Kronecker delta $\delta_{ij}$

d = np.eye(3)

# Permutation or Levi-Cevita symbol $\epsilon_{ijk}$ 

e = np.array([[[0,0,0],[0,0,1],[0,-1,0]],[[0,0,-1],[0,0,0],[1,0,0]],[[0,1,0],[1,0,0],[0,0,0]]])


# Taking the original second rank tensor, axis of rotation and angle of rotation as inputs

print("Enter the entries of the second rank tensor in a single line (separated by space): ")
entries = list(map(float, input().split()))
T = np.array(entries).reshape(3, 3)
print(T)


print("Enter the entries of the unit vector about which this tensor is rotated in a single line (separated by space): ")
entries1 = list(map(float, input().split()))
n = np.array(entries1).reshape(3)
print(n)


thetaDegree = float(input("Enter the angle of rotation (in degrees) :"))
theta = ((np.pi)/180.0)*thetaDegree
print(theta)


# Transformation of reference frames obtained by rotating about a unit vector n by an angle $\theta$ is written in a compact form as $Q$

Q = np.cos(theta)*d + (n*n.reshape(-1,1))*(1 - np.cos(theta)) + np.einsum('ijk,k->ij',e,n)*np.sin(theta)


# Tensor T in the new reference frame

Tnew = np.einsum('pi,qj,ij->pq', Q, Q, T)
print("Tensor T in the new reference frame is ")
print(Tnew)


