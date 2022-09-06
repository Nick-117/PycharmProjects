import turtle
from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()



# code above is the object for the score keeping text


screen.listen()

screen.onkey(key="Up", fun=snake.up)
screen.onkey(key="Down", fun=snake.down)
screen.onkey(key="Left", fun=snake.left)
screen.onkey(key="Right", fun=snake.right)

# results = scoreboard.point_tracker()
# text.write(f"Score: {results}", align="center", move=False, font=("Arial", 10, "normal"))

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    # Detect collision with tail
    # if head collides with any segment in the tail:
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()
    #     trigger game over




    # results = scoreboard.point_tracker()
    # text.write(f"Score: {results}", align="center", move=False, font=("Arial", 10, "normal"))



    #detect collision with food
    #add a point from the scoreboard


screen.exitonclick()









    # code below gets snake to move forward by twenty paces.
    # for seg in segments:
    #     seg.forward(20)





# new_block = Turtle()
# new_block.penup()
# new_block.color("green")
# new_block.shape("square")
# new_block.setpos(x=-60, y=0)
#
# new_hack = Turtle()
# new_hack.penup()
# new_hack.color("red")
# new_hack.shape("square")
# new_hack.setpos(x=-40, y=0)





screen.exitonclick()