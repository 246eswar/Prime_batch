def m_add(a,b):
    return [[a[i][j]+b[i][j]for j in range(len(a[0]))]for i in range(len(a))]
#list comprehension with in a list comprehension'''for rows and coloumns and for addition a[i][j]+b[i][j]'''
a = [[1,2,3],[4,5,6]]#list taken so taken len(a)
b = [[7,8,9],[10,11,12]]
c=m_add(a,b)
print("Matrix Addition: ")
for row in c:
    print (row)
