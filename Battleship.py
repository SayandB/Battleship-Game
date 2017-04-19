from random import randint
flag = 0
board = []
for i in range(10):
    board.append(["-"]*10)
def print_board(board):
    for i in board:
        print " ".join(i)
print_board(board)
def random_row(board):
    return randint(0,len(board)-1)
def random_col(board):
    return randint(0,len(board)-1)
sub_row = random_row(board)
sub_col = random_col(board)
carr_row = random_row(board)
carr_col = random_col(board)
if carr_col%2==0:
    if (carr_col+2)>9:
        carr_pos = range(carr_row-2,)
    else:
        carr_pos = [carr_col,carr_col+2]
else:
    if (carr_row+2)>9:
        carr_pos = range(carr_row-2,)
    else:
        carr_pos = [carr_row,carr_row+2]
def check_carr(x,y):
    if x==carr_pos[0] or y==carr_pos[1]:
        return True
    else:
        return False

print"Let's begin... You have 10 chances to find the ship(s)!"
for i in range(1,10):
    guess_row = int(raw_input("Guess row:"))
    guess_col = int(raw_input("Guess column:"))
    if board[guess_row][guess_col]=="X" or board[guess_row][guess_col]=="O":
        print "You've already hit that once!"
    elif (guess_row==sub_row and guess_col==sub_col) or (check_carr(guess_row, guess_col)):
        board[guess_row][guess_col]="X"
        flag+=1
    elif guess_row>9 or guess_col>9:
        print "Out of bounds!"
    else:
        board[guess_row][guess_col]="O"
    print "You have %d chances left"%(10-i)
    print_board(board)
    if flag==3:
        print "You've Won!"
        break
else:
    print "You've lost :("

