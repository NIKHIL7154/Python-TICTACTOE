import sys, subprocess, os, time
from termcolor import colored
def clear():
    subprocess.run("cls",shell=True)
clear()
def instructions():
    print("Welcome to Tic-Tac-Toe")
    print("Below are instructions about the game.")
    print("""Here is the game grid
 1 | 2 | 3 
-----------
 4 | 5 | 6 
-----------
 7 | 8 | 9 

In this game you have to select the number in which
you want to place your turn it can be either X or O.
You already know the rules of TIC-TAC-TOE so let's play.""")

alist=["0"," "," "," "," "," "," "," "," "," "]

linemaker=[1,2,3]

reflist=["0",1,2,3,4,5,6,7,8,9]
winlogic=[[1,2,3],[4,5,6],[7,8,9],[1,5,9],[7,5,3],[1,4,7],[2,5,8],[3,6,9]]
g_input =1

turnvar="X"

def gridwithref():
    print(f"""
 {alist[1]} | {alist[2]} | {alist[3]}     {reflist[1]} | {reflist[2]} | {reflist[3]}
-----------   -----------
 {alist[4]} | {alist[5]} | {alist[6]}     {reflist[4]} | {reflist[5]} | {reflist[6]}
-----------   -----------
 {alist[7]} | {alist[8]} | {alist[9]}     {reflist[7]} | {reflist[8]} | {reflist[9]}
""")

def displaygrid():
    print(f"""
 {alist[1]} | {alist[2]} | {alist[3]}
-----------
 {alist[4]} | {alist[5]} | {alist[6]}
-----------
 {alist[7]} | {alist[8]} | {alist[9]}
""")

def printmsg(msg):
    for i in msg:
            sys.stdout.write(i)
            sys.stdout.flush()
            time.sleep(0.05)

def takeinput():
    global g_input
    g_input=input("\nChoose the number from grid in which you want to put your turn: ")
    if(g_input.isnumeric()):
        g_input=int(g_input)
        if (g_input<1 or g_input>9):
            return False
        else:
            if (alist[g_input]=="X" or alist[g_input]=="O"):
                return False
            else:
                return True
    else:
        return False

def drawgame():
    clear()
    displaygrid()
    print("Game is draw. No one wins the game.")
    playagainmode()

def updatedata():
    alist[g_input]=turnvar
    reflist[g_input]=" "

def loopstarted():
    global turnvar
    clear()
    if(wincheck()):
        winner()
    else:
        
        if(drawchecker()):
            if (turnvar=="X"):
                turnvar="O"
            else:
                turnvar="X"
            mainlogic()
        else:
            drawgame()

def playagainmode():
    global alist
    global reflist
    msg="If you want to play again please enter 'y' in input otherwise game will end."
    printmsg(msg)
    x=input("\nEnter input: ")
    if(x=="y"):
        clear()
        alist=["0"," "," "," "," "," "," "," "," "," "]
        reflist=["0",1,2,3,4,5,6,7,8,9]
        instructions()
        mainlogic()
    else:
        printmsg("Game ended here. Thanks for playing.")
        return

def winner():
    global alist
    clear()
    for j in linemaker:
        alist[j]=colored(f"{alist[j]}",'red')
    displaygrid()
    print(f"Winner is {turnvar}")
    playagainmode()

def wincheck():
    global linemaker
    for i in winlogic:
        x="a"
        y="b"
        p="c"
        for j in i:
            if (x=="a"):
                x=alist[j]
            elif(y=="b"):
                y=alist[j]
            else:
                p=alist[j]
        if(x==y==p=="X")or(x==y==p=="O"):
            linemaker=i
            return True
    return False

def drawchecker():
    for i in alist:
        if(i==" "):
            return True
    return False

def mainlogic():
    gridwithref()
    
    printmsg((f"Its {turnvar}'s turn"))
    
    if(takeinput()):
        updatedata()
        loopstarted()
        
    else:
        clear()
        print("Entered input is not available. Please choose available numbers from grid.")
        msg="You have to enter input again:"
        printmsg(msg)
        mainlogic()

instructions()
mainlogic()






