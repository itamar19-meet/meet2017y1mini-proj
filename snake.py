import turtle
import random

turtle.tracer(1,0)
#map size
SIZE_X=1000
SIZE_Y=700
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
snake.shape("circle")
turtle.hideturtle()

snake.color("red")
for i in range(start_len):
    x_pos = snake.pos()[0]
    y_pos = snake.pos()[-1]
    x_pos = x_pos + sq_size
    my_pos = (x_pos , y_pos)
    snake.goto(x_pos , y_pos)
    pos_list.append(snake.pos)
    stamp_ID = snake.stamp()
    stamp_list.append(stamp_ID)
#directions
UP_ARROW = "Up"
DOWN_ARROW = "Down"
LEFT_ARROW = "Left"
RIGHT_ARROW = "Right"
TIME_STEP = 100

UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
direction = UP
UP_EDGE = SIZE_Y/2
DOWN_EDGE = -SIZE_Y/2
RIGHT_EDGE = SIZE_X/2
LEFT_EDGE = -SIZE_X/2
def up():
    global direction
    direction = UP
    
    print("you pressed up key")
def down():
    global direction
    direction = DOWN
    
    print("you pressed down key")
def left():
    global direction
    direction = LEFT
   
    print("you pressed left key")
def right():
    global direction
    direction = RIGHT
    print("you pressed right key")
turtle.onkeypress(up , UP_ARROW)
turtle.listen()    
turtle.onkeypress(down , DOWN_ARROW)
turtle.listen()    
turtle.onkeypress(left , LEFT_ARROW)
turtle.listen()    
turtle.onkeypress(right , RIGHT_ARROW)
turtle.listen()        
#fjdjiokbuyfgyuiokjihugyuojihuhhhhhhhhhhhhhhhh-----------------------------------------------
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
    new_pos = snake.pos()
    new_x_pos = new_pos[0]
    new_y_pos = new_pos[1]
    if new_x_pos >= RIGHT_EDGE:
        print("you lose :(")
        quit()
    if new_x_pos <= LEFT_EDGE:
        print("you lose :(")
        quit()
    
    if new_y_pos >= UP_EDGE:
        print("you lose :(")
        quit()
    if new_y_pos <= DOWN_EDGE:
        print("you lose :(")
        quit()    

    if pos_list[-1] in pos_list[0:-1]:

        print("dont hit yourself!!!!")
        quit()

################################################################################################1
#specialllll!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    global food_stamps , food_pos
    if snake.pos() in food_pos:
        food_ind = food_pos.index(snake.pos())
        food.clearstamp(food_stamps[food_ind])
        food_pos.pop(food_ind)
        food_stamps.pop(food_ind)
        print("you ate a turtle!!!!")
        makefood()


    turtle.ontimer(move_snake,TIME_STEP)     
move_snake()
#food
count = 0
food = turtle.clone()
food.color("green")
food.shape("turtle")
food_pos = [(100,100) , (-100,100) , (-100, -100) , (100,-100)]
for this_food_pos in food_pos:
    food.goto(this_food_pos[0], this_food_pos[1])
    stamp_number = food.stamp()
    food_stamps.append(stamp_number)
def snake_grow():
    stamp_list.append(snake.stamp())
    pos_list.append(snake.pos())
    
count = 0
def counter():
    turtle.goto(280,270)
    turtle.clear()
    turtle.write("score: " + str(count) , font =( "Arial" , 16 , "normal"))
    turtle.ontimer(counter,1000)
    turtle.color("white")
def makefood():
    global count
    min_x = -int(SIZE_X/2/sq_size)+1
    max_x = int(SIZE_X/2/sq_size)-1
    min_y = -int(SIZE_Y/2/sq_size)+1
    max_y = int(SIZE_Y/2/sq_size)-1
    food_x = random.randint(min_x,max_x)*sq_size
    food_y = random.randint(min_y,max_y)*sq_size
    food.goto(food_x,food_y)
    stood = food.stamp()
    food_stamps.append(stood)
    food_pos.append(food.pos())
    snake_grow()
    count = count + 1
    print(count)
    counter()
turtle.bgcolor("black")

#if #int(count) == 50:
   #print("omg you are so goooooood!!!!!!!!")
   # good = turtle.write("omg you are so goof!!" , font =( "Arial" , 16 , "normal"))
    #good.clear()



























