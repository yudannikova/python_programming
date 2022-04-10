string = input()
matrix = []
out_matrix = []
while string != 'end':
    matrix.append([int(i) for i in string.split()])
    out_matrix = [[0 for k in range(len(string))] for p in range(len(matrix))]
    string = input() 

for ix in range(len(matrix)):
    for jx in range(len(matrix[0])):
        out_matrix[ix][jx] = [matrix[ix][jx - 1] + matrix[ix][(jx + 1) % len(matrix[0])] + matrix[ix - 1][jx] + matrix[(ix + 1) % len(matrix)][jx]]
    
for ix in range(len(matrix)):
    for jx in range(len(matrix[0])):
        print(*(out_matrix[ix][jx]), end=' ')
    print()   




