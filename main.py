#IMPORTS
import turtle
import pygame


#PYGAME INIT
pygame.init()

#TURTLE WINDOW
wn = turtle.Screen()
wn.title("PongDEMO")
wn.bgcolor("Black")
wn.setup(width=800,height=600)
wn.tracer(0)

#GAME OBJECTS:
    #PADDLES A:
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.color("white")
paddle_a.penup()
paddle_a.goto(-370,0)

    #PADDLES B:
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.color("white")
paddle_b.penup()
paddle_b.goto(370,0)

    #BALL
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.4
ball.dy = 0.4
        #BOUNCE SOUND
pygame.mixer.music.load('beep-02.wav')


    #SCORE
score_a=0
score_b=0

    #PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 | Player B: 0",align="center", font=("Courier",24,"normal"))



#GAME FUNCTIONS:
#FOR PADDLE A:
    #UP
def paddle_a_up():
    if(paddle_a.ycor()<240):
        y=paddle_a.ycor()
        y+=20
        paddle_a.sety(y)
    
    #DOWN
def paddle_a_down():
    if(paddle_a.ycor()>-240):
        y=paddle_a.ycor()
        y-=20
        paddle_a.sety(y)

#FOR PADDLE B:
    #UP
def paddle_b_up():
    if(paddle_b.ycor()<240):
        y=paddle_b.ycor()
        y+=20
        paddle_b.sety(y)
    
    #DOWN
def paddle_b_down():
    if(paddle_b.ycor()>-240):
        y=paddle_b.ycor()
        y-=20
        paddle_b.sety(y)
        




#KEYBOARD BINDING:
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")



#MAIN GAME RUNNER LOGIC:
while True:
    wn.update()

    #BALL PHYSICS
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)
    
        #BOUNCE:
    if ball.xcor()<-350 and ball.xcor()>-370 and ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50:
        ball.setx(-350)
        ball.dx*=-1
        pygame.mixer.music.play()

    if ball.xcor()>350 and ball.xcor()<370 and ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50:
        ball.setx(350)
        ball.dx*=-1
        pygame.mixer.music.play()

    #BORDER CHECKING
    if (ball.ycor()>280):
        ball.sety(280)
        ball.dy*=-1
        pygame.mixer.music.play()

    if (ball.ycor()<-280):
        ball.sety(-280)
        ball.dy*=-1
        pygame.mixer.music.play()

    if ball.xcor()>390:
        score_a+=1
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))

    
    if ball.xcor()<-390:
        score_b+=1
        ball.goto(0,0)
        ball.dx*=-1
        pen.clear()
        pen.write("Player A: {} | Player B: {}".format(score_a,score_b),align="center", font=("Courier",24,"normal"))

    
    if(score_a>4):
        ball.dx=0
        ball.dy=0
        pen.goto(0,0)
        pen.write("Game Over. \nA Wins the Game.",align="center", font=("Courier",24,"normal"))
        
    if(score_b>4):
        ball.dx=0
        ball.dy=0
        pen.goto(0,0)
        pen.write("Game Over. \nB Wins the Game.",align="center", font=("Courier",24,"normal"))