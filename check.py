
board  =  [" 1","2 "," 3"," 4"," ","6 ","7 ","8 ","9 "]


def draw_tie ():
    for i in range (0,9):
        if (board[i] == " ") :
             return False
    else :
        return True



def d():
    for i in range(0,9) :
        lambda i : board[i] == " "
d()
print(d())