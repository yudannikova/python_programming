string = input()
matrix = []
out_matrix = []
while string != 'end':
    row = [int(ix) for ix in string.split()]
    matrix.append(row)
    out_matrix.append([0] * len(row))
    string = input() 

num_rows = len(matrix)
num_cols = len(matrix[0])
for row_ix in range(num_rows):
    for col_ix in range(num_cols):
        out_matrix[row_ix][col_ix] = matrix[row_ix][col_ix - 1] + matrix[row_ix][(col_ix + 1) % num_cols] + matrix[row_ix - 1][col_ix] + matrix[(row_ix + 1) % num_rows][col_ix]
    
for row_ix in range(num_rows):
    for col_ix in range(num_cols):
        print(out_matrix[row_ix][col_ix], end=' ')
    print()   




