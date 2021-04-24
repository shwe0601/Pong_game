from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from score import Score
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.title("Python Ping Pong Game")
screen.bgcolor("black")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))

ball=Ball()
score=Score()

screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_on=True

while game_on:
    time.sleep(ball.moving_speed)
    screen.update()
    ball.move()
     #Detection of collision in wall
    if ball.ycor()>280 or ball.ycor()<-280:
        ball.bounce_y()
    #Detects collision in paddle
    if ball.distance(r_paddle)<40 and ball.xcor()>320 or ball.distance(l_paddle)<40 and ball.xcor()<-320:
        ball.bounce_x()

    #Detects when right paddle misses
    if ball.xcor() >380:
        ball.reset_position()
        score.l_point()

    #Detects when left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()
