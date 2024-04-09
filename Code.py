from turtle import Screen;
import time
from Paddle import Paddle
from Ball import Ball
from ScoreBorad import ScoreBoard
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("black")
screen.title("Pong Game")
screen.listen()
screen.tracer(0)

#CREATION OF PADDLES AND BALLS
paddle_right = Paddle(350,0)
paddle_left = Paddle(-350,0)
ball = Ball()
scoreboard = ScoreBoard()


#MOVEMENT OF PADDLES 
screen.onkey(fun=paddle_right.move_up,key="Up")
screen.onkey(fun=paddle_right.move_down,key="Down")
screen.onkey(fun=paddle_left.move_up,key="w")
screen.onkey(fun=paddle_left.move_down,key="s")

#Game Logic
game_is_on = True
while game_is_on:
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    
    ## detect collision 
    
    if ball.ycor() > 280 or ball.ycor()< -280:
        ball.bounce()

    
    ## detect collision at right paddle 
    
    if ball.distance(paddle_right) <50  and ball.xcor()>320 or ball.distance(paddle_left) <50  and ball.xcor()<-320:
        ball.bouncePeddle()
        ball.movespeed *= 0.9
    
    #ball miss on right
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
        ball.movespeed = 0.1
    #ball miss on left
    if  ball.xcor()< -380:
        ball.reset_position()
        scoreboard.r_point()
        ball.movespeed = 0.1
    
screen.exitonclick()
