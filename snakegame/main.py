from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen =Screen()
screen.tracer(0)
screen.setup(width=600, height=600)
screen.bgcolor("black")

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.new_score()
        snake.extend()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()


    for asghar in snake.asghars[1:]:
        if snake.head.distance(asghar) < 10 :
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()