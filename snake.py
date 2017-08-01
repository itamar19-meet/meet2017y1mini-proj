import turtle
import random

turtle.tracer(1,0)
#map size
SIZE_X=800
SIZE_Y=600
turtle.setup(SIZE_X,SIZE_Y)

turtle.penup()
turtle.speed(0.5)
sq_size = 20
start_len = 7
#intialize lists
pos_list = []
stamp_list = []
food_pos = []
food_stamps = []

snake = turtle.clone()
snake.shape("square")
turtle.hideturtle()

for i in range(start_len):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[-1]
    x_pos = x_pos + sq_size
    my_pos = (x_pos , y_pos)
    snake.goto(x_pos , y_pos)
    pos_list.append(snake.pos)
    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)

UP_ARROW = "Up"
DOWN_ARROW = "Down"
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
TIME_STEP = "space"

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
def up():
    global direction
    direction = UP
    move_snake()
    print("you pressed up key")
def down():
    global direction
    direction = DOWN
    move_snake()
    print("you pressed down key")
def left():
    global direction
    direction = LEFT
    move_snake()
    print("you pressed left key")
def right():
    global direction
    direction = RIGHT
    move_snake()
    print("you pressed right key")
turtle.onkeypress(up , UP_ARROW)
turtle.onkeypress(down , DOWN_ARROW)
turtle.onkeypress(left , LEFT_ARROW)
turtle.onkeypress(right , RIGHT_ARROW)
turtle.listen()        

def move_snake():
    my_pos = snake.pos()
    x_pos = my_pos[0]
    y_pos = my_pos[1]

    if direction == RIGHT:
        snake.goto(x_pos + sq_size,y_pos)
    elif direction == LEFT:
        snake.goto(x_pos - sq_size , y_pos)
    if direction == UP:
        snake.goto(x_pos , y_pos + sq_size)
    elif direction == DOWN:
        snake.goto(x_pos , y_pos - sq_size)
        
    my_pos = snake.pos()
    pos_list.append(my_pos)
    new_stamp = snake.stamp()
    stamp_list.append(new_stamp)
    old_stamp = stamp_list.pop(0)
    snake.clearstamp(old_stamp)
    pos_list.pop(0)
    





























































































































































































































