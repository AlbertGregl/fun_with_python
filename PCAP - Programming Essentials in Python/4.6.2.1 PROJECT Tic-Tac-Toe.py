from random import randrange
import time

# BOARD[row][column]
BOARD = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def display_board(board):
    # The function accepts one parameter containing the board's current status
    # and prints it out to the console.
    print(("+"+"-------+"*3)+("\n|"+"       |"*3))
    print(f"|   {board[0][0]}   |   {board[0][1]}   |   {board[0][2]}   |")
    print(("|"+"       |"*3)+("\n+"+"-------+"*3)+("\n|"+"       |"*3))
    print(f"|   {board[1][0]}   |   {board[1][1]}   |   {board[1][2]}   |")
    print(("|"+"       |"*3)+("\n+"+"-------+"*3)+("\n|"+"       |"*3))
    print(f"|   {board[2][0]}   |   {board[2][1]}   |   {board[2][2]}   |")
    print(("|"+"       |"*3)+("\n+"+"-------+"*3))


def enter_move(board):
    # The function accepts the board current status, asks the user about their move, 
    # checks the input and updates the board according to the user's decision.
    move = int(input("Enter your move Human: "))
    # check for correct usage
    while move < 1 or move > 9:
        move = int(input("Enter your move Human (from 1 - 9): "))
    # find the field and check if the field is free
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == move:
                # update the board
                BOARD[i][j] = "O"                
                display_board(BOARD)
                victory_for(BOARD, "O")
                # Python's move:
                draw_move(BOARD)


#def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.


def victory_for(board, sign):
    # The function analyzes the board status in order to check if 
    # the player using 'O's or 'X's has won the game
    if (board[0][0] == sign and board[0][1] == sign) and board[0][2] == sign:
        exit_program(sign)
    if (board[1][0] == sign and board[1][1] == sign) and board[1][2] == sign:
        exit_program(sign)
    if (board[2][0] == sign and board[2][1] == sign) and board[2][2] == sign:
        exit_program(sign)
    if (board[0][0] == sign and board[1][0] == sign) and board[2][0] == sign:
        exit_program(sign)
    if (board[0][1] == sign and board[1][1] == sign) and board[2][1] == sign:
        exit_program(sign)
    if (board[0][2] == sign and board[1][2] == sign) and board[2][2] == sign:
        exit_program(sign)
    if (board[0][0] == sign and board[1][1] == sign) and board[2][2] == sign:
        exit_program(sign)
    if (board[0][2] == sign and board[1][1] == sign) and board[2][0] == sign:
        exit_program(sign)


def draw_move(board):
    # The function draws the computer's move and updates the board.
    move = randrange(1, 10)
    field = False
    while field == False:
        for i in range(len(board)):
            for j in range(len(board)):
                if BOARD[i][j] == move:
                    # update the board
                    BOARD[i][j] = "X"
                    # exit the while loop
                    field = True
        move = randrange(1, 10)
        print(".")
        time.sleep(1) # just for fun
    # Human's turn
    display_board(BOARD)
    victory_for(BOARD, "X")
    enter_move(BOARD)


def exit_program(sign):
    # prints the Winner and exits the program
    if sign == "O":
        name = "Human"
    else:
        name = "Python"
    print(f"=== '{sign}' ({name}) is the Winner!!! ===")
    exit()


# PROJECT's Heading
print("\n<<<<< = 4.6.2.1 PROJECT: Tic-Tac-Toe = >>>>>")
print("=> Python plays the 'X'")
print("=> Human plays the 'O'\n")

# Computer's initial move...
print("Python makes the move ...")
BOARD[1][1] = "X"
display_board(BOARD)

# Human Player starts the move:
enter_move(BOARD)
