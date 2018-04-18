import sys
import random

board = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

#String that is printed out in the beginning as a reference for the user
board_template = "1|2|3\n-----\n4|5|6\n-----\n7|8|9"

#Gamemode 0 = Player v Player
#Gamemode 1 - Player v AI
gamemode = 0

turn = "X"

#Wait for a player's move
def wait_input():
    global turn

    while True:
        print "Turn: " + turn
        input = raw_input("> ")
       
        #Just a temp variable
        val = 0
    
        #Accept the user input and make sure its valid
        try:
            val = int(input)
        except ValueError:
            print "Invalid input"
            continue
        else:
            if val > 9 or val < 0:
                print "Enter a number according to this key:"
                print board_template
                continue
    
        #Calculate the position of the piece on the board
        val -= 1
    
        #One more error check
        if board[val / 3][val % 3] != ' ':
            print "A piece is already there!"
            continue
    
        board[val / 3][val % 3] = turn
    
        #Switch to the next turn
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"
        break    

#Check if a player has won
def check_board():
    #strip the board into diagonals, columns, and rows
    
    #strips the rows
    strips = []
    for i in range(0,3):
        strips.append(board[i])

    #strips the columns
    for i in range(0,3):
        strip = []
        for k in range(0,3):
            strip.append(board[k][i])
        strips.append(strip)

    #strips the diagonals
    strips.append([board[0][0], board[1][1], board[2][2]])
    strips.append([board[0][2], board[1][1], board[2][0]])


    #Print out the result
    for strip in strips:
        if strip == ['X','X','X']:
            draw_board()
            print "GAME OVER!\nX WINS!"
            sys.exit(0)
        elif strip == ['O','O','O']:
            draw_board()
            print "GAME OVER!\nO WINS!"
            sys.exit(0)
    
    spots = 0
    for row in board:
        for column in row:
            if column != " ":
                spots += 1
    if spots == 9:
        draw_board()
        print "TIE!"
        sys.exit(0)


def draw_board():
    print "\n\n"
    for i in range(0,3):
        print board[i][0] + "|" + board[i][1] + "|" + board[i][2]
        if i < 2:
            print "-----"


def ask_gamemode():
    global gamemode

    print "1) Player V Player\n2) Player V Random AI"
    input = raw_input("> ")
   
    #Just a temp variable
    gm = 0

    #Accept the user input and make sure its valid
    try:
        gm = int(input)
    except ValueError:
        print "Invalid input"
        return
    else:
        if gm > 3:
            print "Invalid integer input"
            sys.exit(0)

    gamemode = gm


def dumb_ai_move():
    global turn

    #Generates a random value until a valid number occurs
    #Could be more efficient
    while True:
        val = random.choice(range(0, 9))

        #One more error check
        if board[val / 3][val % 3] != ' ':
            continue

        board[val / 3][val % 3] = turn

        #Switch to the next turn
        if turn == "X":
            turn = "O"
        elif turn == "O":
            turn = "X"

        break




def main():
    ask_gamemode()
    
    print "NOTE: Enter input for X's and O's corresponding to this key" 
    print board_template


    if gamemode == 1:
        while True:
            draw_board()
            wait_input()
            check_board()
    elif gamemode == 2:
        while True:
            draw_board()
            wait_input()
            check_board()
            dumb_ai_move()
            check_board()

if __name__ == "__main__":
    main()


