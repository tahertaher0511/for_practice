# global variables
game_still_going = True
winner = None
count_x = 0
count_o = 0
board = list(input('Enter cells: ').replace('_', ' '))


def display_board():
    print('-' * 9)
    print('| ' + board[0] + ' ' + board[1] + ' ' + board[2] + ' |')
    print('| ' + board[3] + ' ' + board[4] + ' ' + board[5] + ' |')
    print('| ' + board[6] + ' ' + board[7] + ' ' + board[8] + ' |')
    print('-' * 9)


for i in board:
    if i == 'X':
        count_x += 1
    elif i == 'O':
        count_o += 1
if count_x > count_o:
    current_player = 'O'
else:
    current_player = 'X'


def play_game():
    display_board()
    while game_still_going:
        process_input()
        check_if_game_over()
        flip_player()
        # the game has ended.
    if winner is None and ' ' not in board:
        print('Draw')
    elif winner == 'X' or winner == 'O':
        print(winner, "wins")
    elif winner is None and ' ' in board:
        print('Game not finished')


def flip_player():
    global current_player
    global count_o
    global count_x
    for current_player in board:
        if current_player == 'X':
            count_x += 1
        elif current_player == 'O':
            count_o += 1
    if count_x > count_o:
        current_player = 'O'
    elif count_o > count_x:
        current_player = 'X'


def check_if_game_over():
    check_if_win()
    check_if_tie()
    game_not_finished()


def check_if_win():
    global winner
    rows_winner = check_rows()
    col_winner = check_col()
    diagonal_winner = check_diagonals()
    if rows_winner:
        winner = rows_winner
    elif col_winner:
        winner = col_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None


def check_rows():
    global game_still_going
    row_1 = board[0] == board[1] == board[2] != ' '
    row_2 = board[3] == board[4] == board[5] != ' '
    row_3 = board[6] == board[7] == board[8] != ' '
    if row_1 or row_2 or row_3:
        game_still_going = False
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]


def check_col():
    global game_still_going
    col_1 = board[0] == board[3] == board[6] != ' '
    col_2 = board[1] == board[4] == board[7] != ' '
    col_3 = board[2] == board[5] == board[8] != ' '
    if col_1 or col_2 or col_3:
        game_still_going = False
    if col_1:
        return board[0]
    elif col_2:
        return board[1]
    elif col_3:
        return board[2]


def check_diagonals():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != ' '
    diagonal_2 = board[2] == board[4] == board[6] != ' '
    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]


def check_if_tie():
    global game_still_going
    if ' ' not in board:
        game_still_going = False


def game_not_finished():
    global game_still_going
    if ' ' in board and winner is None:
        game_still_going = False


def process_input():
    global current_player
    while True:
        try:
            coordinates_input = input('Enter the coordinates: ').split()
            if coordinates_input[0].isnumeric() is False or coordinates_input[1].isnumeric() is False:
                print('You should enter numbers!')
            else:
                x = int(coordinates_input[0])
                y = int(coordinates_input[1])
                if 1 <= x <= 3 and 1 <= y <= 3:
                    if board[(3 - y) * 3 + (x - 1)] == ' ':
                        board[(3 - y) * 3 + (x - 1)] = current_player
                        display_board()
                        break
                    else:
                        print('This cell is occupied! Choose another one!')
                else:
                    print('Coordinates should be from 1 to 3!')
        except IndexError or NameError or ValueError:
            print('Coordinates should be from 1 to 3!')


play_game()
