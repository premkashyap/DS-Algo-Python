def print_matrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            print(matrix[i][j], end= ' ')
        print('\n')

def transpose(mtx):
    return [[mtx[j][i] for j in range(len(mtx))]  for i in range(len(mtx[0]))]

def spiral_traversal(matrix):
    row_start = column_start = 0
    row_end = len(matrix)-1
    column_end = len(matrix[0])-1

    while row_start <= row_end and column_start <= column_end:
        i = row_start
        j = column_start
        while j < column_end:
            print(matrix[i][j], end=' ')
            j+=1

        while i < row_end:
            print(matrix[i][j], end = ' ')
            i+=1
        
        while j > column_start:
            print(matrix[i][j], end=' ')
            j-=1

        while i > row_start:
            print(matrix[i][j], end = ' ')
            i-=1

        row_start+=1
        column_start+=1
        row_end-=1
        column_end-=1

def helical_traversal(mtx):
    rows = len(mtx)
    for counter in range(rows):
        j = 0
        i=counter
        while j <=counter:
            print(mtx[i][j], end = ' ')
            j+=1
            i-=1
    for counter in range(1, rows):
        j=counter
        i=rows-1
        while i>=counter:
            print(mtx[i][j], end = ' ')
            i-=1
            j+=1
        
def rotate90degree(matrix):
    n=len(matrix)
    i=0
    while i<n//2:
        j=i
        while j<n-1-i:
            temp = matrix[i][j]
            matrix[i][j] = matrix[n-j-1][i]
            matrix[n-j-1][i] = matrix[n-i-1][n-j-1]
            matrix[n-i-1][n-j-1]= matrix[j][n-i-1]
            matrix[j][n-i-1] = temp
            j+=1
        i+=1
    return matrix


if __name__ == '__main__':
    mtx1= []
    k=1
    for i in range(4):
        submtx=[]
        for j in range(4):
            submtx.append(k)
            k = k+1
        mtx1.append(submtx)
    print_matrix(mtx1)
    ##print_matrix(transpose(mtx1))
    ##spiral_traversal(mtx1)
    #print_matrix(rotate90degree(mtx1))
    helical_traversal(mtx1)
