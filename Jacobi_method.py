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
    return np.array([col])


def check_convergence(matrix):
    for i in range(matrix.shape[0]):
        if matrix[i][i] > sum(matrix[i]) - matrix[i][i]:
            continue
        else:
            return False
    return True


def check_inequality(matrix_B, current_vector_X, prev_vector_X):
    difference = np.subtract(current_vector_X, prev_vector_X)
    difference = max(abs(difference))
    difference = difference[0]
    norm_B = np.linalg.norm(matrix_B, ord=np.inf)
    right_part = (1 - norm_B)
    right_part = right_part / np.linalg.norm(matrix_B, ord=np.inf)
    right_part = right_part * epsilon

    # if np.subtract(current_vector_X, prev_vector_X) <= (1-np.linalg.norm(matrix_B, ord=np.inf))/np.linalg.norm(matrix_B, ord=np.inf) * epsilon:
    if difference <= right_part:
        return False
    else:
        return True


def iterating(matrix_B, vector_of_free, current_vector_X, prev_vector_X):
    while check_inequality(matrix_B, current_vector_X, prev_vector_X):
        prev_vector_X = current_vector_X
        current_vector_X = np.dot(matrix_B, prev_vector_X)

        current_vector_X = current_vector_X + vector_of_free

    return current_vector_X


def is_convergence(matrix):
    for i in range(np.size(matrix, 0)):
        if sum(matrix[i]) - matrix[i][i] >= matrix[i][i]:
            print("Jacobi method don't convergence. Please enter another matrix")
            return False
    print("Jacobi method convergence")
    return True

def out_res_vector(res_vector):
    np.ndarray.tolist(res_vector)
    for i in range(np.size(res_vector)):
        print('x{} = {}'.format(i, res_vector[i]))

matrix = None
size = 0


def input_size_and_matrix():
    print("Enter the size of The matrix")
    global size
    size = int(input())
    print("Enter The matrix")
    global matrix
    matrix = input_matrix(size)
    matrix = np.array(matrix)


input_size_and_matrix()
method_is_convergencer = is_convergence(matrix)
if not method_is_convergencer:
    while not method_is_convergencer:
        input_size_and_matrix()

epsilon = 0.0001  # accuracy

print("Enter The free var columns")
free_var_columns = input_free_var_column(size)

matrix_D = np.diag(np.diag(matrix))
matrix_L = np.tril(matrix, -1)
matrix_R = np.triu(matrix, 1)

inv_mat_D = np.linalg.inv(matrix_D)
sum = matrix_L + matrix_R
matrix_B = np.dot(np.linalg.inv(matrix_D), (matrix_L + matrix_R))
matrix_B = np.dot(matrix_B, -1)
free_var_columns = np.transpose(free_var_columns)
vector_c = np.dot(inv_mat_D, free_var_columns)

norm_of_vector_c = max(abs(vector_c))
norm_of_matrix_B = np.linalg.norm(matrix_B, ord=np.inf)

vector_X = [0] * size
prev_vec = np.array([[0], [0]])

vector_X = np.dot(matrix_B, prev_vec) + vector_c
# res = \
res = iterating(matrix_B, vector_c, vector_X, prev_vec)
out_res_vector(res)
