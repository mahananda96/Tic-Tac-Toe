def display_board(board):
    print(board[6],"|",board[7],"|",board[8])
    print("---------")
    print(board[3],"|",board[4],"|",board[5])
    print("---------")
    print(board[0],"|",board[1],"|",board[2])
    

def player_input(marker):
    pos=int(input("Choose your next position"))
    place_marker(test_board, marker,pos)

    
def place_marker(board, marker, pos):
    if(space_check(board,pos)):
        test_board[pos-1]=marker
    else:
        print("position is already filled")
        if(i==1):
            i=2
        else:
            i=1

def space_check(board, position):
    return(position==board[position-1])

def win_check(board):
    return((board[0]==board[1]==board[2]) or (board[3]==board[4]==board[5]) or
           (board[6]==board[7]==board[8]) or (board[0]==board[6]==board[3]) or
            (board[4]==board[1]==board[7]) or (board[2]==board[5]==board[8]) or
            (board[0]==board[4]==board[8]) or (board[2]==board[4]==board[6]))
    

def full_board_check(board):
    for j in range(len(board)):
        if(board[j]==j+1):
            return False
    return True


test_board=[1,2,3,4,5,6,7,8,9]
display_board(test_board)
marker=['*','o','o']
marker[1]=input("Player!! Please chose a mark between X or O").lower()
if(marker[1]=='x'):
      marker[2]='o'
else:
     marker[2]='x'
i=int(input("Which player will start first!!!1 or 2"))
while(True):
    if(not(full_board_check(test_board))):   
        player_input(marker[i])
        display_board(test_board)
        status=win_check(test_board)
        if(status== True):
            print("Player",i,"wins")
            break;
        if(i==1):
           i=2
        else:
           i=1
    else:
       print("Board is full1 No one wins!!!")
       break;
    
    
