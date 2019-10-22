#Veronica Stureborg
#Project 7

from graphics import *
import math

def arrows(p, ring):
    x = p.getX() - ring.getCenter().getX()
    y = p.getY() - ring.getCenter().getY()
    dist= math.sqrt(x*x + y*y)

    return dist <= ring.getRadius()

def main():

    win= GraphWin('Target')
#prints white circle
    white= Circle(Point(100,100), 100)
    white.setOutline("black")
    white.setFill("white")
    white.draw(win)
#prints black circle
    black= Circle(Point(100,100), 80)
    black.setOutline("black")
    black.setFill("black")
    black.draw(win)
#prints blue circle
    blue= Circle(Point(100,100), 60)
    blue.setOutline("black")
    blue.setFill("blue")
    blue.draw(win)
#prints red circle
    red= Circle(Point(100,100), 40)
    red.setOutline("black")
    red.setFill("red")
    red.draw(win)
#prints yellow circle
    yellow= Circle(Point(100,100), 20)
    yellow.setOutline("black")
    yellow.setFill("yellow")
    yellow.draw(win)

     



#gets the clicks for the arrows thrown
    totalscore = 0
    for i in range (5):
        p=win.getMouse()

        if (arrows(p, yellow)):
            totalscore= totalscore+9
        elif (arrows(p, red)):
           totalscore= totalscore+7
        elif (arrows(p, blue)):
            totalscore=totalscore+5
        elif (arrows(p, black)):
            totalscore= totalscore + 3
        elif (arrows(p, white)):
            totalscore=totalscore+1
        else:
            totalscore=totalscore+0

        print(totalscore)
       
#prints score
    print("The total score is: ", totalscore)
#closes the window
    message= Text(Point(win.getWidth()/2,20), "Click Again to Quit")
    message.draw(win)
    win.getMouse()
    win.close()
main()
