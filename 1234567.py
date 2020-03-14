import numpy as np

def outprint_matrix(matrix):
    for i in range(matrix.len):
        for j in range(matrix.len):
            print(matrix[i][j], end=" ")
        print()


def input_matrix(size):
    return [list(map(int, input().split())) for i in range(size)]


def input_free_var_column(size):
    col = []
    for i in range(size):
        col.append(int(input()))
    return col


def check_convergence(matrix):
    for i in range(matrix.shape[0]):
        if matrix[i][i] > sum(matrix[i]) - matrix[i][i]:
            continue
        else:
            return False
    return True

def iterating(matrix_B, vector_of_free, current_vector_X, prev_vector_X):
    while True:


size = int(input())
matrix = input_matrix(size)
matrix = np.array(matrix)

print(np.linalg.norm(matrix, ord=np.inf))
free_var_columns = np.array(input_free_var_column(size))
print(free_var_columns, free_var_columns.shape,  end='\n\n')
print(np.transpose(free_var_columns), np.transpose(free_var_columns).shape,  end='\n\n')
print(np.dot(matrix, free_var_columns), end='\n\n')
print(np.dot(matrix, np.transpose(free_var_columns)), end='\n')
print(matrix.shape)
free_var_columns = free_var_columns.reshape(2, 1)


matrix_D = np.diag(np.diag(matrix))
matrix_L = np.tril(matrix, -1)
matrix_R = np.tril(matrix, 1)
matrix_B = (-1) * np.dot(np.linalg.inv(matrix_D) * (matrix_L + matrix_R))
vector_c = np.dot(np.linalg.inv(matrix_D), free_var_columns)

norm_of_vector_c = max(vector_c)
norm_of_matrix_B = np.linalg.norm(matrix_B, ord=np.inf)

vector_X = [0]*size


