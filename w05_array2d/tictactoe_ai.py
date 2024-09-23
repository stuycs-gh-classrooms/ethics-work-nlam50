"""
1. Ask if they would like to play
2. Player O: Select your spot. First give us the row (1, 2, 3)
3. Player O: Then give us the column (1, 2, 3)
4. Display the board
5. Repeat steps 2 and 3 for player X
6. This continues until all the spots filled out without a winner or there is a winner where a set of threes appear 
"""

arr = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]

def make_board(): 
    for row in arr:
        print(row)

def place(row, col, player): #place an X or O if it can be placed (so if there is " ")
    if arr[row-1][col-1] == " ": #1 because we ask the player from 1-3, not 0-2
        if player == 0:
            arr[row-1][col-1] = "O"
            #print(arr[row-1][col-1])
        if player == 1:
            arr[row-1][col-1] = "X"
            #print(arr[row-1][col-1])
        return True
    else:
        print("That spot is taken. Choose another spot")
        return False
            
def run_game():
    while True:
        play = input("Do you want to play tic tac toe? (answer yes or no): ")
        if play == "yes":
            make_board()
            for i in range(9):# a range of 9 is the total number of times you can input X or O before the grid is full
            # player turns
                if (i % 2) == 0:
                    print("\nPlayer O: ")
                    player = 0
                else:
                    print("\nPlayer X: ")
                    player = 1 
                #row = int (input("Select your spot. First give us the row (1, 2, 3): "))
                #col = int (input("Then give us the column (1, 2, 3): "))
                
                # if spot taken
                while True:
                    row = int (input("Select your spot. First give us the row (1, 2, 3): "))
                    col = int (input("Then give us the column (1, 2, 3): "))
                    if place(row, col, player):
                        break
                # case where player provides invalid input for row/column not yet handled - also maybe separate functions
                
                make_board()
                
                # win returns
                if(win()):
                    if player == 0:
                        print("The winner is Player O")
                    else:
                        print("The winner is Player X")
                if(is_full()):
                    print("It is a tie. Do better")
                    break
        elif play == "no":
            print("Free will is an illusion. Answer yes")
        else:
            print("Invalid. Answer with yes or no")
        
        
            
def win(): #checks for a win - can loop too
    row1 = (arr[0][0] == arr[0][2] and arr[0][0] == arr[0][1] and arr[0][0] != " " )
    row2 = (arr[1][0] == arr[1][2] and arr[1][0] == arr[1][1] and arr[1][0] != " " )
    row3 = (arr[2][0] == arr[2][2] and arr[2][0] == arr[2][1] and arr[2][0] != " " )
    col1 = (arr[0][0] == arr[2][0] and arr[0][0] == arr[1][0] and arr[0][0] != " " )
    col2 = (arr[0][1] == arr[2][1] and arr[0][1] == arr[1][1] and arr[0][1] != " " )
    col3 = (arr[0][2] == arr[2][2] and arr[0][2] == arr[1][2] and arr[0][2] != " " )
    diagonal1 = (arr[0][0] == arr[1][1] and arr[2][2] != " " )
    diagonal2 = (arr[0][2] == arr[1][1] and arr[2][0] != " " )
    if (row1 or row1 or row3 or col1 or col2 or col3 or diagonal1 or diagonal2):
        return True
        
def is_full(): #check if the grid is full 
    for row in arr:
        for col in row: 
            if col == " ":
                return False 
    return True

run_game()