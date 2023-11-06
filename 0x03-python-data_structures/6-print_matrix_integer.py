#!/user/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        length = 1
        for coloumn in row:
            if length == len(row):
                print("{:d}".format(coloumn), end="")
            else:
                print("{:d}".format(coloumn), end=" ")
        print()
