# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
A = np.array([[1,2,3],[3,2,1]])
B = np.random.randint(-1,2,(3,2))
C = np.zeros((2,2 ))
def row_method_mat_mul_steps(A,B):
     result = "A = {} \n B = {}".format(A,B)
   #  print(result)
     for i in range(A.shape[0]):
         for j in range(B.shape[1]):
            C[i,j] = np.dot(A[i],B[:,j])
            #print( "C{},{} = {}".format(i,j,C[i,j]),end =" ",sep='\n')
         print("a{},: * B = {}".format(i+1,C))      
def inverse_matrix_gauss_jordan(A):
    col = A.shape[1]
    A = np.concatenate((A,np.eye(A.shape[0])),axis=1) 
   # print(A)
    for i in range(A.shape[0]):
        if i != A.shape[0]-1 :
            if A[i,i] == 0:
                A[i,:],A[i+1:] = A[i+1,:],A[i:]
            ratio = -A[i+1,i] / A[i,i]
            A[i+1] =  A[i]*ratio + A[i+1]
        if i != 0:
            if A[i,i] == 0:
                A[i,:],A[i+1:] = A[i+1,:],A[i:]
            ratio = -A[i-1,i] / A[i,i]
            A[i-1] =  A[i]*ratio + A[i-1]
    for i in range(A.shape[0]):
        A[i] /= A[i,i]
    
    return A[:,col:]
def multiply_scalar_distributivity(lambd,phi,C):
    A = ([['' for i in range(C.shape[1])] for i in range(C.shape[0])])
    B = ([['' for i in range(C.shape[1])] for i in range(C.shape[0])])
   # print("(lambd + phi)C = ({} + {}){}".format(lambd,phi,C))
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
          A[i][j] += "{} * {}" .format(lambd,C[i,j])
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
          B[i][j] += "{} * {}" .format(phi,C[i,j])
    print("{} + {} = {}".format(np.array(A),np.array(B),(lambd+phi)*C))
