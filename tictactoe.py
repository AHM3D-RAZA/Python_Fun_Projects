def row_check(row):
    check_element = row[0]
    if check_element == " ":
        return False
    for i in range(len(row)):
        if check_element != row[i]:
            return False
    return True
    
def row_winner(board):
    
    for row in board:
        if row_check(row):
            return True
    return False
    
def column_winner(board):
    
    for i in range(len(board)):
        new_row = []
        for j in range(len(board)):
            new_row.append(board[j][i])
        if row_check(new_row):
            return True
    return False
    
def diagonal_winner(board):
    left_diagonal = []
    right_diagonal = []
    for i in range(len(board)):
        left_diagonal.append(board[i][i])
        right_diagonal.append(board[i][-i-1])
    return row_check(left_diagonal) or row_check(right_diagonal)
    
def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)
    
def print_winner(player):
    print(f'{player} wins!')
    
def game_draw():
    print('The Game eneded in a Draw!')

def format_board(board):
    first_row = '  '
    line = ''
    for i in range(len(board)):
        first_row += str(i + 1) + ' '
        line += '-'
    display_board = [first_row]
    for i in range(len(board)):
        joined_row = str(i + 1) + ' ' + '|'.join(board[i])
        display_board.append(joined_row)
    line = '  ' + '+'.join(line)
    return f'\n{line}\n'.join(display_board)
    
def make_board(size):
    board = []
    for _ in range(size):
        row = []
        for _ in range(size):
            row.append(" ")
        board.append(row)
    return board
 
def play_move(board, player):
    print(f'{player} to play:')
    row = int(input()) - 1
    col = int(input()) - 1
    board[row][col] = player
    print(format_board(board))
    
def play_game(player1, player2):
    board_size = (int(input('What size board you want to play on?: ')))
    board = make_board(board_size)
    print(format_board(board))
    
    i = 0
    player1_up = True
    while(i < board_size * board_size):
        if player1_up:
            play_move(board, player1)
            player1_up = False
            if(winner(board)):
                print_winner(player1)
                break
        else:
            play_move(board, player2)
            player1_up = True
            if(winner(board)):
                print_winner(player2)
                break
        i += 1
        
    game_draw()
   
   
   
play_game('X', 'O')