#i = 0
#matrix1 = [[i*3+j for j in range(1,5)] for i in range(4)]
# matrix2 = [j*3+i for j in range(4) for i in range(4)]

# print(matrix1)
# print(matrix2)


def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end= ' ')
        print('\n')


mtx1= []
k=1
for i in range(4):
    submtx=[]
    for j in range(4):
        submtx.append(k)
        k = k+1
    mtx1.append(submtx)

print_matrix(mtx1)
transpose = [[mtx1[j][i] for j in range(len(mtx1))]  for i in range(len(mtx1[0]))]

print_matrix(transpose)




# mtx2= []
# for j in range(4):
#     for i in range(4):
#         mtx2.append(j*3+i)

# print(mtx2)