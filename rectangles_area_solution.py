matrix = []
rows = 0
col = 0
num_rect = 0
total_area = 0
upper_left_container = []

def get_inputs():
    global matrix
    global rows
    global col

    rows, col = input().split()
    rows = int(rows)
    col = int(col)

    for row in range(rows):
        new_row = input().split()
        matrix.append(new_row)

    return matrix


def start_corner_finder():

    for y in range(rows-1):
        for x in range(col-1):
            if matrix[y][x] == "1":
                find_borders(y, x)


def find_borders(y1,x1):
    up = 1
    bottom = 1
    left = 0
    right = 1

    for y in range(y1, rows):
        if matrix[y][x1] == "1":
            left += 1
        else:
            break

    for x in range(x1+1, col):
        if matrix[y1][x] == "1":
            up += 1
        else:
            break

    if up > 2 and left > 2:
        for y in range(y1+1, rows):
            if matrix[y][x1+up-1] == "1":
                right += 1
            else:
                break
        for x in range(x1+1, col):
            if matrix[y1+left-1][x] == "1":
                bottom += 1
            else:
                break

    get_parameters(up,bottom,left, right)


def get_parameters(up, bottom, left, right):
    global num_rect
    global total_area

    if up > 2 and left > 2:
        if up == bottom and left == right:
            num_rect += 1
            area = (up-2)*(left-2)
            total_area += area


get_inputs()
start_corner_finder()
print(num_rect, total_area)
