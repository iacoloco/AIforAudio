#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 25 13:57:19 2025

@author: armandoiachini
"""
"Solve the exercises of Week 1 using numpy (np):"
"1. Solve the linear system using np.linalg.solve"
import numpy as np

A = np.array([
    [1, 3, -5],
    [3, 11, -9],
    [-1, 1, 6]
])
b = np.array([2, 4, 5])


x = np.linalg.solve(A,b)
print("exercise 1 result= " , x)


"Exercise 2"

x1= np.array([
    [5],[3], [2]
    ])

x2= np.array([
    [2], [2], [1]
    ])

"Find x1x2T"

x1x2T = x1@x2.T

"Moltiply the vector using .dot"
x1Timesx2 = np.dot(x1.T,x2)

print("Exercise2 .outer = ", x1x2T)

print("Exercise2  = ",  x1Timesx2)

"Exercise 3: Crete the reverse matrix and multiply using np.dot"

RM = np.array([
    [0,0,1],
    [0,1,0],
    [1,0,0]
    ])

Rx1 = np.dot(RM,x1)

print("Reverse x1= " , Rx1)

"Exercise linal.log norm 1 (mahatta"
x1Norm1 = np.linalg.norm(x1,ord=1)

print("Ex3 norm 1= ", x1Norm1)

x1Nom2 = np.linalg.norm(x1, ord=2)
print("x1 norm2= " , x1Nom2)









