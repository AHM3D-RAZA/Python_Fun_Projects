board = [' ' for x in range(10)]

def insert_letter(pos, letter):
    board[pos] = letter
    
def free_space(pos):
    return board[pos] == ' '

def print_board(board):
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print('---+---+---')
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print('---+---+---')
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    
def winner(board, letter):
    return ((board[1] == letter and board[2] == letter and board[3] == letter) or
    (board[4] == letter and board[5] == letter and board[6] == letter) or
    (board[7] == letter and board[8] == letter and board[9] == letter) or
    (board[1] == letter and board[4] == letter and board[7] == letter) or
    (board[2] == letter and board[5] == letter and board[8] == letter) or
    (board[3] == letter and board[6] == letter and board[9] == letter) or
    (board[1] == letter and board[5] == letter and board[9] == letter) or
    (board[3] == letter and board[5] == letter and board[7] == letter))
    
def board_full(board):
    return board.count(' ') == 1
    
def player_move():
    run = True
    while run:
        insert = input('Please enter a position to insert \'X\' (1-9): ')
        try:
            insert = int(insert)
            if(0 < insert < 10):
                if free_space(insert):
                    insert_letter(insert, 'X')
                    run = False
                else:
                    print('Position already occupied!')
            else:
                print('Invalid Range!')
        except:
            print('Please enter an integer!')

def comp_move():
    possible_moves = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    
    for letter in ['O', 'X']:
        for i in possible_moves:
            board_copy = board[:]
            board_copy[i] = letter
            if winner(board_copy, letter):
                move = i
                return move
    
    open_corners = []
    for i in possible_moves:
        if i in [1, 3, 7, 9]:
            open_corners.append(i)
    
    if len(open_corners) > 0:
        move = random_move(open_corners)
        return move
    
    if 5 in possible_moves:
        move = 5
        return move
    
    open_edges = []
    for i in possible_moves:
        if i in [2, 4, 6, 8]:
            open_edges.append(i)
    
    if len(open_edges) > 0:
        move = random_move(open_edges)
        return move

    return move

def random_move(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]
    
def main():
    print('I am an AI and being the superior one, I will let you go first!')
    print_board(board)
    
    while not(board_full(board)):
        if not(winner(board, 'O')):
            player_move()
            print_board(board)
        else:
            print('I won. Better luck next time :)')
            break
        
        if not(winner(board, 'X')):
            move = comp_move()
            if move == 0:
                break
            else:
                insert_letter(move, 'O')
                print('I placed an \'O\' at position', move)
                print_board(board)
        else:
            print('Congrats! You beat me!')
            break
    
    if(board_full(board)):
        print("It's a Tie!")
        
main()
