board = [
    [7, 8, 0, 4, 0, 0, 1, 2, 0],
    [6, 0, 0, 0, 7, 5, 0, 0, 9],
    [0, 0, 0, 6, 0, 1, 0, 7, 8],
    [0, 0, 7, 0, 4, 0, 2, 6, 0],
    [0, 0, 1, 0, 5, 0, 9, 3, 0],
    [9, 0, 4, 0, 6, 0, 0, 0, 5],
    [0, 7, 0, 3, 0, 0, 0, 1, 2],
    [1, 2, 0, 0, 0, 7, 4, 0, 0],
    [0, 4, 9, 2, 0, 6, 0, 0, 7],
]

def solve(boa):

    # Find empty slot
    find = find_empty(boa)
    if not find:
        return True
    else:
        row, col = find
        for i in range(1, 10):
            if valid(boa, i, (row, col)):
                boa[row][col] = i
                if solve(boa):
                    return True
                # Resets value to 0
                boa[row][col] = 0
    # Triggers backtracking
    return False

def valid(boa, num, pos):

    # Check for rows
    for i in range(len(boa[0])):
        if boa[pos[0]][i] == num and pos[1] != i:
            return False
    
    # Check for columns
    for i in range(len(boa)):
        if boa[i][pos[1]] == num and pos[0] != i:
            return False
    
    # Check boxes
    box_x = pos[0] // 3 
    box_y = pos[1] // 3

    for i in range(box_x*3, box_x*3 + 2):
        for j in range(box_y*3, box_y*3 + 2):
            if boa[i][j] == num and pos != (i, j):
                return False

    return True


def display_board(boa):

    for i in range(len(boa)):
        if i % 3 == 0 and i != 0:
            print('- - - - - - - - - - - -')
        for j in range(len(boa[0])):
            if j % 3 == 0 and j != 0:
                print('|', end=" ") 
            if j == 8:
                print(boa[i][j])
            else:
                print(boa[i][j], end=" ")

def find_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j] == 0:
                #return position of row and column
                return (i, j)   

    return None


display_board(board)
solve(board)
print('------------------Solved-----------------')
display_board(board)
