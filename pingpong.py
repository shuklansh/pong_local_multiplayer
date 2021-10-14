#ping pong game with player 1 and 2

import turtle

wn = turtle.Screen()
wn.title("ping pong by ansh shukla")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

#leftpaddle
paddle_l=turtle.Turtle()
paddle_l.speed(0)
paddle_l.shape("square")
paddle_l.color("cyan")
paddle_l.shapesize(stretch_len=1,stretch_wid=5)
paddle_l.penup()
paddle_l.goto(-350,0)
#rightpaddle
paddle_r=turtle.Turtle()
paddle_r.speed(0)
paddle_r.shape("square")
paddle_r.color("cyan")
paddle_r.shapesize(stretch_len=1,stretch_wid=5)
paddle_r.penup()
paddle_r.goto(350,0)
#ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.shapesize(stretch_len=1,stretch_wid=1)
ball.penup()
ball.goto(0,0)
ball.dx = 0.7
ball.dy = 0.7
#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("player 1: 0       player 2: 0",align ="center",font =("courier",24,"normal"))
#score
score_1=0
score_2=0

#function
def paddle_l_up():
    y = paddle_l.ycor()
    y=y+20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y = y-20
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y=y+20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y = y-20
    paddle_r.sety(y)
#keyboard bind
wn.listen()
wn.onkeypress(paddle_l_up,"w")  
wn.onkeypress(paddle_l_down,"s")  

wn.onkeypress(paddle_r_up,"8")  
wn.onkeypress(paddle_r_down,"5")

#main
while True:
    wn.update()

    #moveball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border check
    if ball.ycor() >290:
        ball.sety(290)
        ball.dy *= -1
    if ball.ycor() <-290:
        ball.sety(-290)
        ball.dy *= -1
    if ball.xcor() >390:
        ball.goto(0,0)
        ball.dx *= -1 
        score_1 = score_1 + 1
        pen.clear()
        pen.write("player 1:{}       player 2:{}".format(score_1,score_2),align ="center",font =("courier",24,"normal"))
   
    if ball.xcor() <-390:
        ball.goto(0,0)
        ball.dx *= -1        
        score_2 = score_2 + 1
        pen.clear()
        pen.write("player 1:{}       player 2:{}".format(score_1,score_2),align ="center",font =("courier",24,"normal"))
   
    #paddle n ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_r.ycor() +50 and ball.ycor() > paddle_r.ycor() -50):
        ball.setx(340)
        ball.dx *= -1
    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_l.ycor() +50 and ball.ycor() > paddle_l.ycor() -50):
        ball.setx(-340)
        ball.dx *= -1
