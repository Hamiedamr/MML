import numpy as np
import matplotlib.pyplot as plt
A = np.array([[-2,4,-2,-1,4],
              [4,-8,3,-3,1],
              [1,-2,1,-1,1],
              [1,-2,0,-3,4],
              ])
B = np.random.randint(-1,2,(3,2))
C = np.zeros((2,2 ))

def row_method_mat_mul_steps(A,B):
     for i in range(A.shape[0]):
         for j in range(B.shape[1]):
            C[i,j] = np.dot(A[i],B[:,j])
         print("a{},: * B = {}".format(i+1,C))  
         
def inverse_matrix_gauss_jordan(A):
    col = A.shape[1]
    A = np.concatenate((A,np.eye(A.shape[0])),axis=1) 
    for i in range(A.shape[0]):
        if i != A.shape[0]-1 :
            if A[i,i] == 0:
                A[i],A[i+1] = A[i+1],A[i]
            ratio = -A[i+1,i] / A[i,i]
            A[i+1] =  A[i]*ratio + A[i+1]
        if i != 0:
            if A[i,i] == 0:
                A[i],A[i+1] = A[i+1],A[i]
            ratio = -A[i-1,i] / A[i,i]
            A[i-1] =  A[i]*ratio + A[i-1]
    for i in range(A.shape[0]):
        A[i] /= A[i,i]
    rref(A)
    return A[:,col:].astype(np.float16)

def multiply_scalar_distributivity(lambd,phi,C):
    A = ([['' for i in range(C.shape[1])] for i in range(C.shape[0])])
    B = ([['' for i in range(C.shape[1])] for i in range(C.shape[0])])
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
          A[i][j] += "{} * {}" .format(lambd,C[i,j])
    for i in range(C.shape[0]):
        for j in range(C.shape[1]):
          B[i][j] += "{} * {}" .format(phi,C[i,j])
    print("{} + {} = {}".format(np.array(A),np.array(B),(lambd+phi)*C))

def Row_Echelon_Form(A,start_row=0,start_col=0,pivots = []):
    if start_row == A.shape[0]-1:
        for start_row,start_col in pivots:
             A[start_row] = A[start_row] / A[start_row,start_col]
        return
    B = A
    B = B[start_row:,start_col:]
    row=1
    while B[0,0] == 0 and row != B.shape[0]:
        B[0],B[row] = B[row],B[0]
        row += 1
    if B[0,0] == 0:
        raise Exception("Singular Matrix :(!")
    for i in range(1,B.shape[0]):
        ratio = -B[i,0] /B[0,0]
        B[i] = B[0]*ratio + B[i]
    pivots.append((start_row,start_col))
    start_row +=1
    start_col += 1
    if not(start_col >=  A.shape[1] or start_row >=  A.shape[0]):
        while(start_row != A.shape[0] and A[start_row,start_col] == 0 ) :
            # print(A[start_row,start_col])
            start_col+= 1
            if start_col >=  A.shape[1]:
                break
    pivots.append((start_row,start_col))
    Row_Echelon_Form(A,start_row,start_col,pivots)
   
def rref(A):
     pivots = []
     Row_Echelon_Form(A,pivots = pivots)
     for start_row,start_col in pivots:
         for i in range(start_row):
             ratio = -A[i,start_col] /A[start_row,start_col]
             A[i] = A[start_row]*ratio + A[i]
     return set(pivots)
def null_soln(A):
    A_rref = A.copy()
    pivots = rref(A_rref)
    i = 0
    while i < A.shape[0]:
        if A[i,i] == 0:
           c = np.zeros(A.shape[1])
           c[i] = -1
           A = np.insert(A,i,c,axis=0)
        i += 1
    while A.shape != (A.shape[1],A.shape[1]):
           c = np.zeros(A.shape[1])
           c[-(A.shape[1] - A.shape[0])] = -1
           A = np.concatenate( (A,c.reshape(1,A.shape[1])),axis=0)
    pivots = [j for i,j in pivots ]
   
    non_pivots = [i for i in range(A.shape[1]) if i not in pivots]
    return A[:,non_pivots]
        
            
A = plt.imread("test.jpg").copy()
rref(A)
plt.imshow(A)


