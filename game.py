#!/usr/bin/env python
# coding: utf-8

# In[3]:


import turtle
import random


## Taking inputs
NumberOfRows = 0
NumberOfRows = turtle.numinput("enter number of rows : ", "NumberOfRows",minval = 1, maxval = 6)

NumberOfRows = int(NumberOfRows)

NumberOfColumns = 0
NumberOfColumns = turtle.numinput("enter number of rows : ", "NumberOfColumns", minval = 2,maxval = 10)


    
NumberOfColumns = int(NumberOfColumns)
def SetScreen():     #ccreating screen
    screen = turtle.Screen() 
    screen.title("Turtle Game")
    screen.setup(1000, 800,startx=100,starty=10)
    canvas = screen.getcanvas()
    return screen, canvas

#initalizing values

Game_score = 0  #initial score 0
box_pos = 0
count = 0
pen = turtle.Turtle()
brd = []

def Creating_start_button():
    pen = turtle.Turtle()  #constructor for clas turtle
    pen.hideturtle()  #removing turtle cursor
    pen.color("yellow", "blue") #Button-color 
    pen.begin_fill()
    pen.penup()
    x = 130  #setting x,y coordinates
    y = 300
    pen.goto(x,y)
    pen.pendown()
    for i in range (2):     #creating-button
        pen.forward(160)
        pen.left(90)
        pen.forward(30)
        pen.left(90)
    pen.end_fill()
    pen.penup()
    pen.goto(x+(30),y+(5))
    pen.write("START GAME", font=("Arial",13)) #text for start game button
    




def click(tur):  #click_event 
    global Game_score
    if brd.index(tur) == box_pos and tur.color()[1] == "black":
        Game_score += 1
        tur.color("black","blue") #changing color to blue if user click in box
        screen.update()
    else:
        Game_score -=1
  
    score()
def MakeBoard():   #making Gameboard 
    brd = []
    for i in range(NumberOfRows): #loop for rows ceation
        for j in range(NumberOfColumns):  #lop for columns creating
            tur = turtle.Turtle(shape="square")
            tur.setheading(90)
            brd.append(tur)
            tur.penup()
            tur.shapesize(80 / 20)
            tur.color("black","white")    #setting grid colors
            tur.onclick(lambda x, y, tur=tur: click(tur))
            x = -NumberOfColumns / 2 * 80 + j * 80 + 80 / 2 #making grid on rows,columns input
            y = NumberOfRows / 2 * 80 - i * 80 - 80 / 2
            tur.goto(x, y)
    return brd

def BoxToggle(tur):#setting bxtoggle
    global color
    if tur.color()[1] == "white":
        color = tur.color()
        tur.shapesize(80  / 20)
        tur.color("black","black") 
    else:
        tur.color("black","white")
    tur.onclick(lambda x, y, tur=tur: click(tur))
    screen.update()


def score(): #printing score to the board
    pen.clear()
    pen.write(f"Score: {Game_score}   Attempt #: {count} ", font=("Arial", 16, "normal"))


def reset(Start = False):
    global brd, count, box_pos, pen, Game_score

    screen.clear()  #clear board screen
    screen.bgcolor("green") #setting background color to green
    screen.tracer(0)  #to hide  board creation view
    brd = MakeBoard()
    box_pos = 0
        # Score
    Game_score = 0
    pen = turtle.Turtle()  #constructor for class turtle
    pen.hideturtle()
    pen.penup()
    pen.goto(-150, 300)
    score()
    turtle.onscreenclick(start,1)
    if (Start == False):
        Creating_start_button()
    count = 0
    screen.update()
  

def start(x,y):
    global box_pos
    if(x > 130 and x < 230 and y > 300 and y < 330):
        reset(True)
        BoxToggle(brd[box_pos])
        screen.update()
        MainGame()
    
def EndGame(): #ending the game after maxium tries.
    pen.goto(-50, -20)
    pen.color("RED")
    pen.write("GAME-OVER", font=("Arial", 20, "normal")) #printing game over in red color


def MainGame(): #main execution of the game

    global box_pos, count
    BoxToggle(brd[box_pos])
    box_pos = random.randrange(NumberOfRows * NumberOfColumns)#random numbr for next box position
    BoxToggle(brd[box_pos])
    count += 1
    score()  #updating score
    if count > 10:  #total attempts 10
        box_pos = -999  
        EndGame()
        return  #  Condition to verify  loop.
    screen.ontimer(MainGame, 1500)
screen, canvas = SetScreen()
reset()
turtle.done()


# In[ ]:




