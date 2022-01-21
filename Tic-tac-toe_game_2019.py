print("Welcome to Tic Tac Toe!")
#this function records what type of game the user wants to play
def menu():
    z=1
    while z==1:
        print("Select what you want to do from the menu below: ")
        print("1. Player 1 VS Player 2")
        print("2. Player VS Computer")
        try:
            choice = int(input("3. Load game to file\n"))
            #if the user inputs something not in the range, ask again
            if choice<1 or choice>3:
                print("Please enter a valid option.")
                z=1
            elif choice==1:
                z=2
                return choice
            elif choice==2:
                z=2
                return choice
            elif choice==3:
                z=2
                return choice
        #if the user inputs an invalid answer, ask again
        except ValueError:
            print("Please enter a valid option.")
            z=1
            
#this function lets player 1 to choose if they want to be "X" or "O"
def player1_choice_clarify(choice):
    j=1
    while j==1:
        if choice==1 or choice==2:
            player1_choice = input("Player 1: Do you want to be X or O?\n")
            if player1_choice == "x" or player1_choice == "X":
                j=2
                print("Player 1 will go first")
                return "X"
            elif player1_choice == "o" or player1_choice == "O":
                j=2
                print("Player 1 will go first")
                return "O"
            else:
                print("Please enter an X or an O: ")
                j=1
        else:
            pass
#this function the other symbol to computer based on player 1 choice
def computer_choice(go):
    if go=="X":
        return "O"
    else:
        return "X"
#this function gets the computer's move and checks to see if the move is valid
#if not, get a different computer move
def computer_move(move):
    from random import randint
    computer_move=randint(1,9)
    t=False
    while not t:
        computer_move=randint(1,9)
        if computer_move==1 and board[6]==" ":
            board[6]=move
            t = True
        elif computer_move==2 and board[7]==" ":
            board[7]=move
            t = True
        elif computer_move==3 and board[8]==" ":
            board[8]=move
            t = True
        elif computer_move==4 and board[3]==" ":
            board[3]=move
            t = True
        elif computer_move==5 and board[4]==" ":
            board[4]=move
            t = True
        elif computer_move==6 and board[5]==" ":
            board[5]=move
            t = True
        elif computer_move==7 and board[0]==" ":
            board[0]=move
            t = True
        elif computer_move==8 and board[1]==" ":
            board[1]=move
            t = True 
        elif computer_move==9 and board[2]==" ":
            board[2]=move
            t = True
        else:
            t = False
                
#this function assigns the other symbol to player 2 based on player 1's choice
def player2_choice(go):
    if go=="X":
        return "O"
    else:
        return "X"
    
#create a list of empty spaces
board = [" ", " ", " ",
                       " ", " ", " ",
                       " ", " ", " "]

#this function creates the tic-tac-toe board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    
#this function gets the player's move and checks to see if it's a valid move
def is_legal_move(get_move):
    t=False
    while not t:
        try:
            print(whose_turn + ":What is your next move? (1-9)")
            moves=int(input("[Choose 0 to save and exit the game]\n"))
            if moves==0:    
                t = True
                print("Okay, file saved.\nGoodbye")
                return 0
            elif moves==1 and board[6]==" ":
                board[6]=get_move
                t = True
            elif moves==2 and board[7]==" ":
                board[7]=get_move
                t = True
            elif moves==3 and board[8]==" ":
                board[8]=get_move
                t = True
            elif moves==4 and board[3]==" ":
                board[3]=get_move
                t = True
            elif moves==5 and board[4]==" ":
                board[4]=get_move
                t = True
            elif moves==6 and board[5]==" ":
                board[5]=get_move
                t = True
            elif moves==7 and board[0]==" ":
                board[0]=get_move
                t = True
            elif moves==8 and board[1]==" ":
                board[1]=get_move
                t = True 
            elif moves==9 and board[2]==" ":
                board[2]=get_move
                t = True
            #if move is not in the correct range, ask for input again
            elif moves<1 or moves>9:
                print("Please enter a valid choice. (1-9)")
                t =  False
            else:
                print("Please enter a valid choice. (1-9)")
                t = False
        #if move is not valid, ask for input again
        except ValueError:
            print("Please enter a valid choice. (1-9)")
            t = False

#this function saves the game including whose turn it is,
#player symbols, what spaces are taken and by whom, and
#what type of game is being player(player vs player or player vs computer)
def save_game(player1, board, whose_turn, player_choice):
    tic_tac_toe_file=open("game.txt", mode="w")
    for cell in board:
        tic_tac_toe_file.write(cell)
        tic_tac_toe_file.write("\n")
    tic_tac_toe_file.write("\n")
    tic_tac_toe_file.write(player1)
    tic_tac_toe_file.write("\n")
    tic_tac_toe_file.write(whose_turn)
    tic_tac_toe_file.write("\n")
    tic_tac_toe_file.write(str(player_choice))
    tic_tac_toe_file.close()

#this function reads the saved file and reassigns the values in the file
def load_game():
    tic_tac_toe_file = open("game.txt", mode="r")
    parts = tic_tac_toe_file.read().splitlines()
    board = parts[0:9]
    player1 = parts[10]
    whose_turn = parts[11]
    player_choice = int(parts[12])
    return [board, player1, whose_turn, player_choice]

#this function checks to see if a tie has occurred
def is_tie(board):
    if board[0]==" ":
        return False
    elif board[1]==" ":
        return False
    elif board[2]==" ":
        return False
    elif board[3]==" ":
        return False
    elif board[4]==" ":
        return False
    elif board[5]==" ":
        return False
    elif board[6]==" ":
        return False
    elif board[7]==" ":
        return False
    elif board[8]==" ":
        return False
    else:
        return True

#this function asks if user wants to play again and records their answer
def player_play_again():
    y=1
    while y==1:
        try:
            play_again=input("Do you want to play again? (yes or no)\n")
            if play_again=="Yes" or play_again=="yes":
                print("Okay, starting game over")
                y=2
                return False
            elif play_again=="No" or play_again=="no":
                y=2
                return True
            else:
                print("Please enter a valid response")
                y=1
        #if the user does not enter a valid response, ask for input again
        except ValueError:
            print("Please enter a valid response")
            y=1

#this function checks to see if there's a winner
def winner(player):
    if board[0]==board[1]==board[2] and board[0]==player:
        return True            
    if board[3]==board[4]==board[5] and board[3]==player:
        return True           
    if board[6]==board[7]==board[8] and board[6]==player:
        return True         
    if board[0]==board[3]==board[6] and board[0]==player:
        return True         
    if board[1]==board[4]==board[7] and board[1]==player:
        return True
    if board[2]==board[5]==board[8] and board[2]==player:
        return True
    if board[0]==board[4]==board[8] and board[0]==player:
        return True
    if board[6]==board[4]==board[2] and board[6]==player:
        return True
    else:
        return False
 
x=1
while x==1:
    game_over=False
    #print out the options and let player choose what to do
    player_choice=menu()
    #if the player wants to play an old game, reload it
    if player_choice==3:
        board, player1, whose_turn, player_choice = load_game()
        player2=player2_choice(player1)
        computer=computer_choice(player1)
    #if the player wants to play a new game of player vs player,
    #clear the board...
    elif player_choice==1:
        board = [" ", " ", " ",
                       " ", " ", " ",
                       " ", " ", " "]
        #let player 1 pick their symbol
        player1=player1_choice_clarify(player_choice)
        #assign player 2's symbol
        player2=player2_choice(player1)
        #let player 1 go first
        whose_turn="player 1"
    #if the player wants to play a new game of player vs computer,
    #clear the board...
    elif player_choice==2:
        board = [" ", " ", " ",
                       " ", " ", " ",
                       " ", " ", " "]
        #let player 1 pick their symbol
        player1=player1_choice_clarify(player_choice)
        #assign computer's symbol
        computer=computer_choice(player1)
        #let player 1 go first
        whose_turn="player 1"
    else:
        pass
    #start nested while loop that plays the player1 vs player2 game
    while not game_over and player_choice==1:
        if whose_turn=="player 1":
            display_board(board)
            #check if legal move
            test=is_legal_move(player1)
            if test==0:
                #if player wants to save game,
                #record status of game and end game
                save_game(player1, board, whose_turn, player_choice)
                game_over=True
            elif winner(player1):
                #if player 1 wins, tell them and end the game
                display_board(board)
                print("Hooray! Player 1 you have won the game!")
                game_over=True
            else:
                #alternate whose turn it is
                whose_turn="player 2"
        else:
            display_board(board)
            #check if legal move
            test2=is_legal_move(player2)
            if test2==0:
                #if player wants to save game,
                #record status of game and end game
                save_game(player1, board, whose_turn, player_choice)
                game_over=True
            elif winner(player2):
                #if player 1 wins, tell them and end the game
                display_board(board)
                print("Hooray! Player 2 you have won the game!")
                game_over=True
            else:
                #alternate whose turn it is
                whose_turn="player 1"
        #if no one wins, check if tie,
        #if yes, tell the players and end the game
        if not game_over and is_tie(board):
            display_board(board)
            print("It's a tie.")
            game_over = True
    #start nested while loop that plays the player vs computer game
    while not game_over and player_choice==2:
        if whose_turn=="player 1":
            display_board(board)
            #check if legal move
            test=is_legal_move(player1)
            if test==0:
                #if player wants to save game,
                #record status of game and end game
                save_game(player1, board, whose_turn, player_choice)
                game_over=True
            elif winner(player1):
                #if player 1 wins, tell them and end the game
                display_board(board)
                print("Hooray! Player 1 you have won the game!")
                game_over=True
            else:
                #alternate whose turn it is
                whose_turn="computer"
        else:
            #check if legal move
            computer_move(computer)
            if winner(computer):
                #if computer wins, tell user and end the game
                display_board(board)
                print("The computer won the game.")
                game_over=True
            else:
                #alternate whose turn it is
                whose_turn="player 1"
        #if no one wins, check if tie,
        #if yes, tell the player and end the game
        if not game_over and is_tie(board):
            display_board(board)
            print("It's a tie.")
            game_over = True
    try:
        #if user wants to save the game, exit immediately
        if test==0:
            x=2
        elif test2==0:
            x=2
        #if someone won of there was a tie, ask if user wants to play again
        #if yes, loop again
        elif player_play_again():
            #if no, end loop
            print("Okay, goodbye")
            x=2
    except:
        pass
