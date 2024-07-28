import turtle
from turtle import Screen
import time
import SnakeBody
import food
import score


Screen().setup(width=600, height=600)
Screen().bgcolor("black")
Screen().title("Snake Game")
Screen().tracer(0)
snake = SnakeBody.Snake()
food = food.Food()
snake.create_snake()
score = score.Score()


Screen().listen()
Screen().onkey(snake.up,"Up")
Screen().onkey(snake.down,"Down")
Screen().onkey(snake.left,"Left")
Screen().onkey(snake.right,"Right")

game_is_on = True
while game_is_on:
    Screen().update()
    time.sleep(0.1)
    snake.move()
    #Detect Food Collision
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()
    #Detect Wall Collision
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        game_is_on = False
        score.game_over()
    #Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            score.game_over()

Screen().exitonclick()
