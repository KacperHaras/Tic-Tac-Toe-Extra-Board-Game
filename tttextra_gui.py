from tkinter import *
import random

root= Tk()
root.config(bg='black')
root.title('Tic-Tac-Toe-Extra')


mode = "P"          #Mode of game (Player vs Player or Player vs Computer)
opponent = "O"      #Symbol of opponent (X or O)
player = "X"        #Symbol of player (X or O)
gameRunning = True  #Flag which indicates if the game is running
winner = None       #Symbol of winner of small board (X or O)
bigWinner = None    #Symbol of winner of the overall game (X or O)
previousS = 0       #Number of small board in which the player has to play
nowB = 0            #Number of small board in which the player is playing
winBoard = {"X":[],"O":[]}  #Holds information about small boards won by X or O
labels_to_destroy = [] #List of labels which have to be destroyed after the game ends
blackList = []          #List of small boards which are won or tied
label_console = Label() #Label which holds the console text


#List which holds informations about contents of one small board
board = ["-","-","-",
         "-","-","-",
         "-","-","-"]

#List which holds informations about contents of small boards and information if they are won by someone 
bigBoard = [(board.copy(),"") for elem in range(9)]

#class which represents the small board
class Board_:
    def __init__(self, root,x,y):
        root.title("Tic-Tac-Toe-Extra")

        #Creates the buttons for the small board 
        self.but11 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but11))
        self.but11.grid(row=4*x+4, column=4*y+2,sticky=W+E)
        self.but12 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but12))
        self.but12.grid(row=4*x+4, column=4*y+3,sticky=W+E)
        self.but13 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but13))
        self.but13.grid(row=4*x+4, column=4*y+4,sticky=W+E)
        self.but14 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but14))
        self.but14.grid(row=4*x+5, column=4*y+2,sticky=W+E)
        self.but15 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but15))
        self.but15.grid(row=4*x+5, column=4*y+3,sticky=W+E)
        self.but16 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but16))
        self.but16.grid(row=4*x+5, column=4*y+4,sticky=W+E)
        self.but17 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but17))
        self.but17.grid(row=4*x+6, column=4*y+2,sticky=W+E)
        self.but18 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but18))
        self.but18.grid(row=4*x+6, column=4*y+3,sticky=W+E)
        self.but19 = Button(root, text=" ", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: self.clicked(self.but19))
        self.but19.grid(row=4*x+6, column=4*y+4,sticky=W+E)

        self.buttons = [self.but11, self.but12, self.but13, self.but14, self.but15, self.but16, self.but17, self.but18, self.but19]

    #Handles the button click event
    def clicked(self,butt):
        global player,announcement,label_console,previousS,nowB
        info = butt.grid_info()

        r = info['row'] - info['row']%4
        c = (info['column']+2) - (info['column']+3)%4 -1

        D = 3*((int(info['row']/4)-1)%3) + (int((info['column']+2)/4)-1)%3
        M = 3*( info['row']%4 - (int(info['row']/4)-1) + (((int(info['row']/4)-1)%3)) ) + (info['column']+2)%4 - (int(info['column']/5)) + (int((info['column']+2)/4)-1)%3
        
        if butt.cget("text") == " " and previousS != 0:
            if D+1 != previousS:
                consoleInput("You clicked wrong button...\nYou have to play in " + str(previousS) )
                return
                
        butt.config(text=player, padx=12, pady=10, state=DISABLED, disabledforeground='black')
        #printBoard(bigBoard)
        if  bigBoard[D][0][M] == "-":
            bigBoard[D][0][M] = player
            if M+1 not in blackList : 
                previousS = M+1
                nowB = D+1
            else:
                previousS = 0
                nowB = D+1

        if nowB != 0:
            checkWin(nowB,r,c)
        if nowB != 0:
            checkTie(nowB)

        checkBigWin()
        checkBigTie()
        switchPlayer()

        if gameRunning:
            if previousS != 0:
                consoleInput("You have to play in " + str(previousS) )
            else: 
                consoleInput("Play somewhere outside " + str(blackList) )

    def reset(self):
        for button in self.buttons:
            button.config(text=" ", state=NORMAL)



#Obiect of board to play
bigBoard_ = [Board_(root, i // 3, i % 3) for i in range(9)]

announcement = "Choose mode"
label_console = Label(root, text=announcement, bd=10, highlightthickness=2, bg='grey65', font=("Helvetica", 15))
label_console.grid(row=0, column=2, columnspan=11, pady=15, sticky=W+E)

but_mode1 = Button(root, text="Player vs Player", padx=15, pady=10, bd=5, highlightthickness=3, bg='grey65', command=lambda: set_mode(but_mode1))
but_mode1.grid(row=1, column=3, columnspan=4, sticky=W+E)

but_mode2 = Button(root, text="Player vs Computer", padx=15, pady=10, bd=5, highlightthickness=3, bg='grey65', command=lambda: set_mode(but_mode2))
but_mode2.grid(row=1, column=8, columnspan=4, sticky=W+E)

if announcement == "Let's play!":
    label_console.grid(row=0, column=2, columnspan=11, rowspan=3, pady=15, sticky=W+E)

label1 = Label(root, text=" ",bd=4, bg='black').grid(row=3,column=1,columnspan=11)
label2 = Label(root, text=" ",bd=4, bg='black').grid(row=4,column=1,rowspan=11)
label3 = Label(root, text=" ",bd=4, bg='black').grid(row=7,column=1,columnspan=11)
label4 = Label(root, text=" ",bd=4, bg='black').grid(row=3,column=5,rowspan=11)
label5 = Label(root, text=" ",bd=4, bg='black').grid(row=11,column=1,columnspan=11)
label6 = Label(root, text=" ",bd=4, bg='black').grid(row=3,column=9,rowspan=11)
label7 = Label(root, text=" ",bd=4, bg='black').grid(row=15,column=1,columnspan=11)
label8 = Label(root, text=" ",bd=4, bg='black').grid(row=3,column=13,rowspan=11)
label8 = Label(root, text=" ",bd=4, bg='black').grid(row=17,column=2,rowspan=11)




'''to debug
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
'''

#Handles the selection of game mode (Player vs Player or Player vs Computer) and the first player symbol (X or O)
def set_mode(button):
    global mode,player,opponent,but_mode1,but_mode2,announcement,label_console
    if announcement == "Choose mode":
        if button.cget("text") == "Player vs Player":
            mode = "P"
        elif button.cget("text") == "Player vs Computer":
            mode = "C"
        announcement = "Choose your player"
        label_console.config(text=announcement)

        but_mode1.config(text="X",padx=12,pady=10)
        but_mode2.config(text="O",padx=12,pady=10)

    elif announcement == "Choose your player":
        if button.cget("text") == "X":
            player = "X"
            opponent = "O"
        elif button.cget("text") == "O":
            player = "O"
            opponent = "X"

        announcement = "Let's play!"
        label_console.config(text=announcement)
        but_mode1.config(state="disabled")
        but_mode2.config(state="disabled")
        label_console = Label(root, text=announcement, bd=10, highlightthickness=10, bg='grey65', font=("Helvetica", 15))
        label_console.grid(row=0, column=2, columnspan=11, rowspan=4, pady=15, sticky=NSEW)

#Updates the console label with the provided text
def consoleInput(text):
    announcement = text
    label_console = Label(root, text=announcement, bd=10, highlightthickness=10, bg='grey65', font=("Helvetica", 15))
    label_console.grid(row=0, column=2, columnspan=11, rowspan=4, pady=15, sticky=NSEW)

#Switches the current player (X to O or vice versa)
def switchPlayer():
    global player,opponent
    if player == "X":
        opponent = "X"
        player = "O"
    else: 
        player = "X"
        opponent = "O"

#Checks for a horizontal win on small Tic-Tac-Toe board
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
    
#Checks for a vertical win on small Tic-Tac-Toe board
def checkVert(board):
    global winner   
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#Checks for a diagonal win on small Tic-Tac-Toe board
def checkDiag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True

#Checks if a player has won on a small board
def checkWin(played, r, c):
    global previousS, nowB
    if checkDiag(bigBoard[played-1][0]) or checkVert(bigBoard[played-1][0]) or checkHoriz(bigBoard[played-1][0]):
        winBoard[winner].append(played)
        blackList.append(played)
        previousS = 0
        nowB = 0
        
        if player == "X":
            label_win_x = Label(root, text="x",font = ("Helvetica", 40),padx=41,pady=31,bd=4, highlightthickness=16,bg='grey65')
            label_win_x.grid(row=r,column=c,rowspan=3,columnspan=3)
            labels_to_destroy.append(label_win_x)
        else:
            label_win_o = Label(root, text="o",font = ("Helvetica", 40),padx=40,pady=31,bd=4, highlightthickness=16,bg='grey65')
            label_win_o.grid(row=r,column=c,rowspan=3,columnspan=3)
            labels_to_destroy.append(label_win_o)
            
#Checks for a tie on a small board 
def checkTie(played):
    global bigBoard, previousS, nowB
    if "-" not in bigBoard[played-1][0]:
        blackList.append(played)
        previousS = 0
        nowB = 0

#Checks if a player has won the overall game 
def checkBigWin():
    global winBoard, bigWinner, gameRunning
    win_combinations = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]

    for combo in win_combinations:
        if all(cell in winBoard["X"] for cell in combo):
            bigWinner = "X"
            break
        elif all(cell in winBoard["O"] for cell in combo):
            bigWinner = "O"
            break

    if bigWinner is not None:
        consoleInput("Mecz wygrał " + str(bigWinner) + "\nGRATULACJE!" )
        '''
        #to be corected

        but_res = Button(root, text="Wanna play again?", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command= restartGame)
        but_res.grid(row=16, column=4, columnspan=7, sticky=W+E)
        '''
        gameRunning = False

#Checks if the overall game has ended in a tie
def checkBigTie():
    global gameRunning
    if blackList == [1,2,3,4,5,6,7,8,9]:
        consoleInput("It's a tie.\nLet's play a rematch!" )
        '''
        but_res = Button(root, text="Wanna play again?", padx=15, pady=10, bd=5, highlightthickness=3,bg='grey65', command=lambda: restart(bigBoard_))
        but_res.grid(row=16, column=4, columnspan=7, sticky=W+E)
        '''
        gameRunning = False

root.mainloop()

'''
#to be corrected
def restartGame():
    global gameRunning, bigBoard, winBoard, blackList, previousS, nowB, bigWinner, announcement, label_console, labels_to_destroy
    for b in bigBoard_:
        b.reset()
    for label in labels_to_destroy:
            label.destroy()

    bigBoard = [(board.copy(),"") for elem in range(9)]
    winBoard = {"X":[],"O":[]}
    previousS = 0
    nowB = 0
    winner = None 
    bigWinner = None
    blackList = []
    labels_to_destroy = []
    announcement = "Choose mode"
    consoleInput(announcement)
    label_console.grid(row=0, column=2, columnspan=11, rowspan=1, pady=15, sticky=W+E)
    printBoard(bigBoard)
    gemRunning = True
'''

'''
def computer():             
    global bigBoard, previousS, nowB
    while True:
        
        if previousS == 0:
            pD = random.randint(1,9)
            
        else: pD=previousS
        print(pD)
        if allFree(bigBoard[pD-1][0]) == True : 
            pM = random.randint(1,9)-1
        else:
            print("findBM")
            pM = findBestMove(bigBoard[pD-1][0]) 
        print("pM:")
        print(pM+1)
        print(pM)
        if bigBoard[pD-1][0][pM] == "-" and pD == previousS:
            print(f"komputer musi grac w {previousS}")
            bigBoard[pD-1][0][pM] = "O"
            bigBoard_[(pD-1)].buttons[pM].config(text="O", padx=12, pady=10, state=DISABLED, disabledforeground='black')
            if pM+1 not in blackList: 
                previousS = pM+1
                nowB = pD
            else: 
                previousS = 0
                nowB = pD
            switchPlayer()
            print("braek---iii----->")
            break
        elif  bigBoard[pD-1][0][pM] == "-" and previousS == 0 and pD not in blackList:
            print(f"komputer musi grac poza {blackList}")
            bigBoard[pD-1][0][pM] = "O"
            bigBoard_[(pD-1)].buttons[pM].config(text="O", padx=12, pady=10, state=DISABLED, disabledforeground='black')
            if pM+1 not in blackList: 
                previousS = pM+1
                nowB = pD
            switchPlayer()
            print("braek-------->")
            break
        else:
            print("--")
            computer()
'''







