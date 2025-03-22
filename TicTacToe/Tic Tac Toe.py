# Tic Tac Toe 

import random

# Function to display a message in '#' characters
def display_message_in_hash(message):
    border = '#' * (len(message) + 4)
    print(border)
    print(f"# {message} #")
    print(border)

# Message to be displayed
message = "Welcome to TIC TAC TOE"

# Display the message
display_message_in_hash(message)
#test_board = ['#','X','O','X','O','X','O','X','O','X']
#print('\n'* 100)
#display_board(test_board)

#DISPLAY BOARD
def display_board(board):
    print("   |   |   ")
    print(f' {board[1]} | {board[2]} | {board[3]} ')
    print("   |   |   ")
    print('-----------')
    print("   |   |   ")
    print(f' {board[4]} | {board[5]} | {board[6]} ')
    print("   |   |   ")
    print('-----------')
    print("   |   |   ")
    print(f' {board[7]} | {board[8]} | {board[9]} ')
    print("   |   |   ")

#print('\n'* 100)

def player_choice(players):

    first_player = goes_first(players)
    players.remove(first_player)
    second_player = ''.join(players)

    marker = ''
    while marker.upper() not in ('X', 'O'):
        marker = input(f"{first_player}, Please choose a marker: 'X' or 'O': ").upper()
        if marker not in ('X', 'O'):
            print("INVALID MARKER! Please choose between 'X' or 'O'.")
    
    if marker.upper() == 'X':
        print(f"{first_player} chooses 'X', so {second_player} is 'O'.")
        return ('X', 'O')
    else:
        print(f"{first_player} chooses 'O', so {second_player} is 'X'.")
        return ('O', 'X')
    

def place_marker(board, position, mark):
    board[position] = mark

def space_check(board, position):
    return board[position] == ' '

def player_turn(board, player):
    position = 0

    while position not in [1,2,3,4,5,6,7,8,9]: # or not space_check(board, position):
        position = input(f'{player}, Choose your next position (1-9): ')
        if position.isdigit():
            if space_check(board, int(position)):
                return int(position)
            else:
                print('Position is not empty, Try again.')
                print('\n'*10)
                display_board(test_board)
        else:
            print('INVALID INPUT! Please try again.')


#def win_check(board, player_marker):
    
    #win_list = [[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]]
    #mark_list = []

    #for i in range(0, len(board)):
        #if board[i] == player_marker:
            #mark_list.append(i)

    #return mark_list in win_list

def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or # across the top
    (board[4] == mark and board[5] == mark and board[6] == mark) or # across the middle
    (board[1] == mark and board[2] == mark and board[3] == mark) or # across the bottom
    (board[7] == mark and board[4] == mark and board[1] == mark) or # down the middle
    (board[8] == mark and board[5] == mark and board[2] == mark) or # down the middle
    (board[9] == mark and board[6] == mark and board[3] == mark) or # down the right side
    (board[7] == mark and board[5] == mark and board[3] == mark) or # diagonal
    (board[9] == mark and board[5] == mark and board[1] == mark)) # diagonal

def check_full_board(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True


def goes_first(players):
    
    #first_player = random.choice(['Player 1', 'Player 2'])
    #print(f'{first_player} goes first.')
    return random.choice(players)

def play_again():
    continue_playing = input('Do you want to play again? (Y/N): ')
    if continue_playing.lower()[0] == 'y':
        return True
    else:
        return False
    
def get_player_names(player_number):
    name = input(f"Please enter name of Player {player_number} (Default: 'Player {player_number}'): ")
    if not name:
        name = f"Player {player_number}"
    
    return name

game_on = False
first_game = True
while True:

    if not game_on:
    
        #Ask players if they are ready to play
        ready = input('Ready to play? (Y/N): ')
        if ready.lower()[0] == 'y':
            game_on = True
            #Ask for player names
            player1 = get_player_names(1)
            player2 = get_player_names(2)
        else:
            break

    #Ask players to choose their marker, by default Player 1 chooses
    player1_marker, player2_marker = player_choice([player1, player2])

    #Choose a player randomly to start the game
    player = goes_first([player1, player2])
    print(f'{player} goes first.')

    test_board = [' '] * 10

    while game_on:
        if player == 'Player 1':

            #Display the board
            if first_game:
                print('\n')
            else:
                print('\n'*10)
            display_board(test_board)

            position = 0
            #Ask player 1 to choose a position for his/her marker
            position = player_turn(test_board, player)

            #Place the marker in entered position
            place_marker(test_board,position, player1_marker)

            #Check if the player has won
            if win_check(test_board, player1_marker):
                print('\n'*10)
                display_board(test_board)
                print('\nPlayer 1 WINS!')
                game_on = False
            else:
            #Check if any position is available, if not end the current game.
                if check_full_board(test_board):
                    print("\nIt's a draw.")
                    break
                else:
                    player = 'Player 2'
        
        else:

            #Display the board
            if first_game:
                print('\n')
            else:
                print('\n'*10)
            display_board(test_board)

            position = 0
            #Ask player 1 to choose a position for his/her marker
            position = player_turn(test_board, player)

            #Place the marker in entered position
            place_marker(test_board,position, player2_marker)

            #Check if the player has won
            if win_check(test_board, player2_marker):
                print('\n'*10)
                display_board(test_board)
                print('\nPlayer 2 WINS!')
                game_on = False
            else:
            #Check if any position is available, if not end the current game.
                if check_full_board(test_board):
                    print('\n'*10)
                    display_board(test_board)
                    print("\nIt's a draw.")
                    break
                else:
                    player = 'Player 1'
        
        first_game = False
            

    if play_again():
        game_on = True
    else:
        game_on = False
        break
