import os 
import time as t 


board  =  [" "," "," "," "," "," "," "," "," "]

gamer = 1 


# ____________ Game OVer _______________


win = 1 
stop = 1
draw = -1
running  = 0

# ________________________________


game  = running
m_gamer = 'X'   # player mark

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

def checkWin () :
    global game
 # ____________- Horizontal - ______________
    if (board[1] == board[2] and board[2] == board[3] and board[1] != " ") : game = win
    elif (board[4] == board[5] and board[5] == board[6] and board[4] != " ") : game = win
    elif  (board[7] == board[8] and board[8] == board[9] and board[7] != ' ') : game = win