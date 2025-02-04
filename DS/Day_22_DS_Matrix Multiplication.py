#Do in online compiler because of import
'''import numpy as S
a=S.array([[1,2],[3,4]])
b=S.array([[5,6],[7,8]])
c=S.dot(a,b)#multiplication
print("Matrix Multiplication: ",c)'''

 #do above with out using numpy
def m_mul(a,b):
    row_a=len(a)
    col_a=len(a[0])
    row_b=len(b)
    col_b=len(b[0])
    c = [[0 for j in range(col_b)]for i in range(row_a)]
    #first rows
    #for j is create the matrix initial 0 or None anythin you take and replace it
    for k in range(row_a):
        for l in range(col_b):
            #coloum of a is also need
            for m in range(col_a):
                c[k][l] = c[k][l] + a[k][m] *b[m][l]
    return c                
a=[[1,2],[3,4]]
b=[[5,6],[7,8]]
#print(m_mul(a,b)) or
print("Mul: ")
d= m_mul(a,b)
for row in d:
    print(row)
