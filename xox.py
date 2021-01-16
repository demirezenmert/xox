import os  as os
import time as t


board  =  [" "," "," "," "," "," "," "," "," "," "]


player = 1


# ____________ Game OVer _______________


win = 1
stop = 1
draw = -1
running  = 0

# ________________________________


game  = running
Mark = 'X'   # player mark

def DrawBoard():
    print(" %c | %c | %c " % (board[1],board[2],board[3]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[4],board[5],board[6]))
    print("___|___|___")
    print(" %c | %c | %c " % (board[7],board[8],board[9]))
    print("   |   |   ")



#  Check Station of board

def check_board (x) :
    if board[x] == " " : return True
    else  : return False
def draw_tie ():
    for i in range (1,10):
        if (board[i] == " ") :
             return False
    else :
        return True
def checkWin () :
    global game
 # ____________- Horizontal - ______________
    if (board[1] == board[2] and board[2] == board[3] and board[1] != " ") : game = win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != " ") : game = win
    elif  (board[7] == board[8] and board[8] == board[9] and board[7] != ' ') : game = win

# ____________- Vertical - ______________
    elif (board[1] == board[4] and board[4] == board[7] and board[1] != " ") : game = win
    elif (board[2] == board[5] and board[5] == board[8] and board[2] != " ") : game = win
    elif (board[3] == board[6] and board[6] == board[9] and board[3] != " ") : game = win
# ____________- Diagonal - ______________
    elif (board[1] == board[5] and board[5] == board[9] and board[1] != " ") : game = win
    elif (board[3] == board[5] and board[5] == board[7] and board[3] != " ") : game = win

# ____________- Tie or Draw - _____________
    elif (draw_tie() == True): game = draw

    else : game = running

while (game == running):
    os.system("clear")
    DrawBoard()
    if (player % 2 != 0) :
        print("Player 1's : ")
        Mark = "X"
    else :
        print("Player 2's : ")
        Mark = "O"
    choice = int(input("Enter the position between [1-9] where you want to mark : "))

    if (check_board(choice)) :
        board[choice] = Mark
        player += 1
        checkWin()

os.system('clear')
DrawBoard()
if game == draw :
    print('Game Draw...')
elif game == win :
    player -= 1
    if (player % 2 != 0) :
        print("Player 1's Won...")
    else :
        print("Player 2's Won...")
