def get_numeric(prompt):
    while True:
        try:
            res = int(input(prompt))
            break
        except (ValueError, NameError):
            print("Numbers only please!")
    return res


def print_matrix(matrix):
    print("==== Matrix ====")
    for i in range(len(matrix)):
        print(matrix[i])


def check_on_symetric(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            a = n - j - 1
            b = n - i - 1
            if matrix[i][j] != matrix[a][b]:
                print(matrix[i][j], matrix[a][b])
                return False

    return True


matrix_size = get_numeric("Entry matrix size: ")
matrix = []

is_correct_data = True

for i in range(matrix_size):
    row = input()
    items = row.split(" ")
    while len(items) != matrix_size:
        print("Incorrect data! Count of symbols must be same as matrix size!")
        row = input()
        items = row.split(" ")

    for j in range(len(items)):
        try:
            items[j] = int(items[j])
        except (ValueError, NameError):
            is_correct_data = False
            break

    if not is_correct_data:
        print("Element of data not a number!")
        break

    matrix.append(items)

if is_correct_data:
    print_matrix(matrix)
    print("Is symetric matrix: %r" % check_on_symetric(matrix))
