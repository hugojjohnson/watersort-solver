import sys
sys.setrecursionlimit(1000000)

# Passes in v1, the first vial, and v2, the second vial.
def pour(board, v1, v2):
    v1_empty_spots, v1_colour, v1_count = vial_info(board[v1])
    v2_empty_spots, v2_colour, v2_count = vial_info(board[v2])

    if v1_empty_spots == 4:
        # print("Vial is empty.")
        return False
    
    if v2_colour != v1_colour and v2_colour != 0:
        # print("Colour mismatch.")
        return False

    if v2_empty_spots < v1_count:
        # print("Not enough space.")
        return False
    
    # It doesn't make sense to pour one of one colour into an empty one.
    if v2_empty_spots == 4 and v1_count + v1_empty_spots == 4:
        return False

    # print(f"You could pour {v1} into {v2}!")
    # print(range((v1_count - 1), (v1_empty_spots)))
    for i in range((v1_empty_spots), (v1_empty_spots + v1_count)):
        board[v1][i] = 0
    for i in range((v2_empty_spots - v1_count), (v2_empty_spots)):
        board[v2][i] = v1_colour
    if board in past_boards:
        return False
    # print("The new board position is:")
    print(board)
    past_boards.append(board)
    return True


def vial_info(vial):
    colour = 0
    count = 0
    empty_spots = 0
    for i in range (4):
        if vial[i] == 0:
            empty_spots += 1
            continue
        if colour == 0:
            colour = vial[i]
            count = 1
            continue
        if vial[i] != colour:
            break
        count += 1

    return ((empty_spots, colour, count))

def make_move(our_board):
    if game_is_won(our_board):
        return True

    for i in range(len(our_board)):
        for j in range(len(our_board)):
            if j == i:
                continue
            board2 = [row[:] for row in our_board]
            if pour(board2, i, j) != False:
                results = make_move(board2)
                if results == True:
                    print(f"pour {i+1} into {j+1}")
                    return True
    return False

def game_is_won(board):
    for vial in board:
        vial_colour = vial_info(vial)[1]

        for i in range(len(vial)):
            if vial[i] != vial_colour and vial[i] != 0:
                return False
    return True

if __name__ == "__main__":
    """
    black 0
    red 1
    orange 2
    yellow 3
    lime 4
    light green 5
    dark green 6
    light blue 7
    dark blue 8
    navy 9
    pink 10
    purple 11
    grey 12
    brown 13
    """
    
    example_board = [[1, 4, 10, 10], [5, 4, 11, 2], [1, 3, 1, 13], [12, 7, 12, 6], [7, 2, 1, 2], [8, 6, 8, 4], [11, 4, 12, 13], [5, 3, 7, 6], [13, 8, 7, 5], [10, 12, 8, 5], [3, 2, 6, 10], [13, 11, 3, 11], [0, 0, 0, 0], [0, 0, 0, 0]]

    #example_board = [[1, 2, 3, 1], [1, 2, 3, 3], [2, 3, 1, 2], [0, 0, 0, 0], [0, 0, 0, 0]]
    past_boards = []
    make_move(example_board)

    # winning_board = [[0, 0, 0, 0], [0, 0, 2, 2], [0, 0, 0, 0], [0, 0, 1, 1]]
    # print(game_is_won(winning_board))



