import random

#small board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#big board contains 9 small boards
bigBoard = [(board.copy(),"") for elem in range(9)]

mode = "P"          #mode of game
opponent = "O"      #opponent of player
player = "X"        #player that is playing now
gameRunning = True  #state of game
winner = None       #winner of the small board
bigWinner = None    #winner of the big board
previousS = 0       #previous small board
nowB = 0             #small board that is played now
winBoard = {"X":[],"O":[]}  #small boards that are won by X or O
blackList = []      #list of small boards that are already won or tied

#prints big board
def printBoard(bigBoard):
    print(bigBoard[0][0][0]+" "+bigBoard[0][0][1]+" "+bigBoard[0][0][2]+" | "+bigBoard[1][0][0]+" "+bigBoard[1][0][1]+" "+bigBoard[1][0][2]+" | "+bigBoard[2][0][0]+" "+bigBoard[2][0][1]+" "+bigBoard[2][0][2])
    print(bigBoard[0][0][3]+" "+bigBoard[0][0][4]+" "+bigBoard[0][0][5]+" | "+bigBoard[1][0][3]+" "+bigBoard[1][0][4]+" "+bigBoard[1][0][5]+" | "+bigBoard[2][0][3]+" "+bigBoard[2][0][4]+" "+bigBoard[2][0][5])
    print(bigBoard[0][0][6]+" "+bigBoard[0][0][7]+" "+bigBoard[0][0][8]+" | "+bigBoard[1][0][6]+" "+bigBoard[1][0][7]+" "+bigBoard[1][0][8]+" | "+bigBoard[2][0][6]+" "+bigBoard[2][0][7]+" "+bigBoard[2][0][8])
    print("---------------------")
    print(bigBoard[3][0][0]+" "+bigBoard[3][0][1]+" "+bigBoard[3][0][2]+" | "+bigBoard[4][0][0]+" "+bigBoard[4][0][1]+" "+bigBoard[4][0][2]+" | "+bigBoard[5][0][0]+" "+bigBoard[5][0][1]+" "+bigBoard[5][0][2])
    print(bigBoard[3][0][3]+" "+bigBoard[3][0][4]+" "+bigBoard[3][0][5]+" | "+bigBoard[4][0][3]+" "+bigBoard[4][0][4]+" "+bigBoard[4][0][5]+" | "+bigBoard[5][0][3]+" "+bigBoard[5][0][4]+" "+bigBoard[5][0][5])
    print(bigBoard[3][0][6]+" "+bigBoard[3][0][7]+" "+bigBoard[3][0][8]+" | "+bigBoard[4][0][6]+" "+bigBoard[4][0][7]+" "+bigBoard[4][0][8]+" | "+bigBoard[5][0][6]+" "+bigBoard[5][0][7]+" "+bigBoard[5][0][8])
    print("---------------------")
    print(bigBoard[6][0][0]+" "+bigBoard[6][0][1]+" "+bigBoard[6][0][2]+" | "+bigBoard[7][0][0]+" "+bigBoard[7][0][1]+" "+bigBoard[7][0][2]+" | "+bigBoard[8][0][0]+" "+bigBoard[8][0][1]+" "+bigBoard[8][0][2])
    print(bigBoard[6][0][3]+" "+bigBoard[6][0][4]+" "+bigBoard[6][0][5]+" | "+bigBoard[7][0][3]+" "+bigBoard[7][0][4]+" "+bigBoard[7][0][5]+" | "+bigBoard[8][0][3]+" "+bigBoard[8][0][4]+" "+bigBoard[8][0][5])
    print(bigBoard[6][0][6]+" "+bigBoard[6][0][7]+" "+bigBoard[6][0][8]+" | "+bigBoard[7][0][6]+" "+bigBoard[7][0][7]+" "+bigBoard[7][0][8]+" | "+bigBoard[8][0][6]+" "+bigBoard[8][0][7]+" "+bigBoard[8][0][8])
    

#prints small board of the winner
def printWinBoard(board,win):
    for i in range(len(board)):
        board[i] = " "
    board[4] = win

#prints small board of the tie
def printTieBoard(board):
    for i in range(len(board)):
        #if board[i]=="X": board[i]="x"
        #elif board[i]=="O": board[i]="o"
        board[i] = " "

#switches player
def switchPlayer():
    global player,opponent
    if player == "X":
        opponent = "X"
        player = "O"
    else: 
        player = "X"
        opponent = "O"

#player input to console
def playerInput(bigBoard):
    global previousS, nowB
    printBoard(bigBoard)
    if previousS != 0: print(f"You have to play in {previousS}")
    elif not blackList  : print("Play wherever you want")
    else: print(f"Play somewhere out of {blackList}")

    inp = input("What's your move? -> ")

    while inp.isnumeric() == False:
        print("It's not a number...")
        inp = input("What's your move? -> ")

    inp=int(inp)
    D = int(inp/10)
    M = inp%10

    if previousS != 0:
        while (D <1 or D >9) or (M <1 or M >9) or D != previousS:
            printBoard(bigBoard)
            print("Wrong input...")
            print(f"You have to play in {previousS}")
            inp = input("What's your move? -> ")
            while inp.isnumeric() == False:
                printBoard(bigBoard)
                print("It's not a number...")
                print(f"You have to play in {previousS}")
                inp = input("What's your move? -> ")
            
            inp = int(inp)
            D = int(inp/10)
            M = inp%10
    else:
        while (D <1 or D >9) or (M <1 or M >9):
            printBoard(bigBoard)
            print("Wrong input...")
            inp = input("What's your move? -> ")
            while inp.isnumeric() == False:
                printBoard(bigBoard)
                print("It's not a number...")
                inp = input("What's your move? -> ")
            inp = int(inp)
            D = int(inp/10)
            M = inp%10

    if  bigBoard[D-1][0][M-1] == "-":
        bigBoard[D-1][0][M-1] = player
        if M not in blackList:
            previousS = M
            nowB = D
        else:
            previousS = 0
            nowB = D
    else:
        print("This place is occupied...")
        playerInput(bigBoard)


#checks if there is a horizontal win
def checkHoriz(board):
    global winner       
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#checks if there is a vertical win
def checkVert(board):
    global winner       ##globalnie sie zmieni winner jesli zmieni sie w tej funkcji
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#check if there is a diagonal win
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


#check if there is a win in small board
def checkWin(zagrany):
    global previousS, nowB
    if checkDiag(bigBoard[zagrany-1][0]) or checkVert(bigBoard[zagrany-1][0]) or checkHoriz(bigBoard[zagrany-1][0]):
        print(f"W {zagrany} wygrywa {winner}")
        printWinBoard(bigBoard[zagrany-1][0],winner)
        winBoard[winner].append(zagrany)
        blackList.append(zagrany)
        previousS = 0
        nowB = 0


#check if there is a tie in small board
def checkTie(zagrany):
    global bigBoard, previousS, nowB
    if "-" not in bigBoard[zagrany-1][0]:
        print(f"W {zagrany} mamy remis :o")
        printTieBoard(bigBoard[zagrany-1][0])
        blackList.append(zagrany)
        previousS = 0
        nowB = 0

#check if there is a win in big board
def checkBigWin():
    global winBoard, bigWinner, gameRunning # Assuming winBoard is a dictionary like {"X":[],"O":[]}

    win_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    for combo in win_combinations:
        if all(cell in winBoard["X"] for cell in combo):
            bigWinner = "X"
            break
        elif all(cell in winBoard["O"] for cell in combo):
            bigWinner = "O"
            break

    if bigWinner is not None:
        printBoard(bigBoard)
        print(f"Mecz wygrał {bigWinner}")
        gameRunning = False

#check if there is a tie in big board
def checkBigTie():
    global gameRunning
    if blackList == [1,2,3,4,5,6,7,8,9]:
        print("Wyrownany pojedynek. Nikt nie wygral.")
        print("Zapraszam na rewanz")
        gameRunning = False


#checks if all fields of small board are free
def allFree(board) :  
    for i in range(3) : 
        for j in range(3) : 
            if (board[3*i+j] == '-') : continue
            else: return
    return True 

#checks if there is a move left in small board
def isMoveLeft(board) :  
    for i in range(3) : 
        for j in range(3) : 
            if (board[3*i+j] == '-') : 
                return True 
    return False
  
#evaluate posible moves (for minmax algorithm)
def evaluate(b):
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  
        [0, 4, 8], [2, 4, 6]            
    ]

    for combo in winning_combinations:
        if b[combo[0]] == b[combo[1]] == b[combo[2]] and (b[combo[0]] == player or b[combo[0]] == opponent):
            return 10 if b[combo[0]] == player else -10

    return 0


#minimax algorithm
def minimax(board, depth, isMax):
    score = evaluate(board.copy())
    
    if score == 10:
        return score

    if score == -10:
        return score

    if not isMoveLeft(board.copy()):
        return 0

    if isMax is True:
        best = -1000

        for i in range(3):
            for j in range(3):
                if board[3 * i + j] == '-':
                    board[3 * i + j] = player
                    best = max(best, minimax(board, depth + 1, not isMax))
                    
                    board[3 * i + j] = '-'
        return best

    elif isMax is False:
        best = 1000

        for i in range(3):
            for j in range(3):
                if board[3 * i + j] == '-':
                    board[3 * i + j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[3 * i + j] = '-'

        return best
    
#finds best move for computer
def findBestMove(board) :  
    bestVal = -1000 
    bestMove = -1  

    for i in range(3) :      
        for j in range(3):

            if (board[3*i+j] == '-'):
                board[3*i+j] = player 
                moveVal = minimax(board, 0, False)  
                board[3*i+j] = '-' 

                if (moveVal > bestVal) :                 
                    bestMove = (3*i+j) 
                    bestVal = moveVal 
    
    return bestMove 

  
#computer move
def computer():             
    global bigBoard, previousS, nowB
    while True:
        if previousS == 0:
            pD = random.randint(1,9)
        else: pD=previousS

        if allFree(bigBoard[pD-1][0]) == True : 
            pM = random.randint(1,9)-1
        else:
            #print("findBM")
            pM = findBestMove(bigBoard[pD-1][0]) 
        #print("pM:")
        #print(pM+1)
        #print(pM)
        if bigBoard[pD-1][0][pM] == "-" and pD == previousS:
            print(f"Computer has to play outside {previousS}")
            bigBoard[pD-1][0][pM] = "O"
            if pM+1 not in blackList: 
                previousS = pM+1
                nowB = pD
            else: 
                previousS = 0
                nowB = pD
            switchPlayer()
            #print("braek---I----->")
            break
        elif  bigBoard[pD-1][0][pM] == "-" and previousS == 0 and pD not in blackList:
            print(f"Computer has to play outside {blackList}")
            bigBoard[pD-1][0][pM] = "O"
            if pM+1 not in blackList: 
                previousS = pM+1
                nowB = pD
            switchPlayer()
            #print("braek-------->")
            break
        else:
            #print("......")
            computer()



#game loop
print("Are you playing with with your friend or computer?")
mode = input("P / C ->").upper()
if mode == "P":
    print("Choose your champion ;)")
    player = input("X / O ->")    
    while gameRunning:
        playerInput(bigBoard)
        if nowB != 0:
            checkWin(nowB)
        if nowB != 0:
            checkTie(nowB)
        checkBigWin()
        checkBigTie()
        switchPlayer()
elif mode == "C":
    while gameRunning:       
        playerInput(bigBoard)
        if nowB != 0:
            checkWin(nowB)
        if nowB != 0:
            checkTie(nowB)
        checkBigWin()
        checkBigTie()
        switchPlayer()
        computer()
        if nowB != 0:
            checkWin(nowB)
        if nowB != 0:
            checkTie(nowB)
        checkBigWin()
        checkBigTie()