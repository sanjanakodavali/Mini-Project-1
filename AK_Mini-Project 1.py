def dis_board(board):
    print("-"*17)
    print("|R\C| 0 | 1 | 2 |")
    print("-"*17)
    for i in range(3):
        print(f"| {i} | {board[i][0]} | {board[i][1]} | {board[i][2]} |")
        print("-"*17)

def validateInput(i,j, board):
    if not 0<=i<3:
        
           
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1, or 2.\n")
        return False
                
        
    if not 0<=j<3:
                
        print("Invalid entry: try again.")
        print("Row & column numbers must be either 0, 1, or 2.\n")
        
    if board[i][j]!= " ":
               
                
        print("That cell is already taken.")
        print("Please make another selection.\n")
        return False
    return True
    

def check(board,player):
    win  =0
    for i in range(3):
        
        if board[i][0]==board[i][1]==board[i][2]==player:
            win = 1
            #print(f"{player} IS THE WINNER!!!")
            
            
        elif board[0][i]==board[1][i]==board[2][i]==player:
            win=1
            #print(f"{player} IS THE WINNER!!!")
            
            
        elif board[0][0]==board[1][1]==board[2][2]==player:
            win=1
            #print(f"{player} IS THE WINNER!!!")
          

        elif board[0][2]==board[1][1]==board[2][0]==player:
            win=1
            #print(f"{player} IS THE WINNER!!!")
            
            
    return win


def main():
    repeat="y"
    while repeat[0].lower()=="y":
        turns = 0
        board=[[" "," "," "],[" "," "," "],[" "," "," "]]
        print("New Game : X goes first.")
        print()
        dis_board(board)
        player="X"
        while True:
            print()
            print(f"{player}'s turn.")
            print(f"Where do you want your {player}  placed?")
            i,j=list(map(int,input("Please enter row number and column number separated by a comma.\n").split(",")))
            print(f"You have entered row #{i}")
            print(f"          and column #{j}")
        
            if not validateInput(i,j,board):
                
                continue
                
            
            
            print("Thank you for your selection.")
            board[i][j]=player
            turns += 1
            v=check(board,player)
            dis_board(board)

            if v==1:
                print(f"{player} IS THE WINNER!!!")
                break
            elif turns == 9:
                print("DRAW NOBODY WINS!")
                break
        
           
            if player=="X":
                player="O"
            elif player=="O":
                player="X"
        print()
        repeat=input("Another game? Enter Y or y for yes.\n")
    print("Thank you for playing")
    
main()


    
