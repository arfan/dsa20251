matrix = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 0],
    [1, 0, 0, 0],
]

sparse_matrix = dict()

def print_matrix(board):
    for row in board:
        print(row)


def convert_to_sparse(m):
    sparse_matrix = dict()

    for index_row, row in enumerate(m):
        for index_col, cell in enumerate(row):
            if cell:
                # print(f"({index_row}, {index_col}): {cell}")

                sparse_matrix[(index_row, index_col)] = cell
    
    return sparse_matrix


print_matrix(matrix)

sparse_matrix = convert_to_sparse(matrix)
print(sparse_matrix)
