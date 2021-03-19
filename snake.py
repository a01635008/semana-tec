"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import update, clear, ontimer, onkey, tracer, listen, hideturtle
from turtle import done, setup, bgcolor
from random import randrange
import random
from freegames import square, vector

colors = ['#8c00fc', '#3500ff', '#01fe01', '#fffe37', '#ff8600']
color_snake = random.choice(colors)
color_square = random.choice(colors)
food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)
bgcolor("black")

def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y


def inside(head):
    "Return True if head inside boundaries."
    return -201 < head.x < 191 and -201 < head.y < 191


def move():
    "Move snake forward one segment."
    head = snake[-1].copy()
    head.move(aim)

    if not inside(head) or head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-20, 19) * 10
        food.y = randrange(-20, 19) * 10
    else:
        snake.pop(0)

    clear()

    for body in snake:
        square(body.x, body.y, 9, random.choice(colors))

    square(food.x, food.y, 9, color_square)
    update()
    ontimer(move, 100)


setup(420, 420, 370, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()
