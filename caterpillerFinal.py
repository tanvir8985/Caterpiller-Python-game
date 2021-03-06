import random
import turtle as t


#___Main board___
t.bgcolor('crimson')
caterpillar = t.Turtle()
caterpillar.shape('square')
caterpillar.color('black')
caterpillar.speed(0)
caterpillar.penup()
caterpillar.hideturtle()

#___determine leaf shape___
leaf = t.Turtle()
leaf_shape = ((0, 0), (14, 2), (22, 5), (20, 20), (5, 22), (2, 14))
t.register_shape('leaf', leaf_shape)
leaf.shape('leaf')
leaf.color('green')
leaf.penup()
leaf.hideturtle()
leaf.speed(0)

#starting point
game_started = False
text_turtle = t.Turtle()
text_turtle.write("Press I to start & use W A S D to control caterpiller", align='center', font=('Futura', 20, 'bold'))
text_turtle.hideturtle()

score_turtle = t.Turtle()
score_turtle.hideturtle()
score_turtle.speed(0)

#start game function
def start_game():
    global game_started
    if game_started:
        return
    game_started = True
    
    score = 0
    text_turtle.clear()

    caterpillar_speed = 2
    caterpillar_length = 2
    caterpillar.shapesize(1, caterpillar_length, 1)
    caterpillar.showturtle()
    display_score(score)
    place_leaf()

    while True:
        caterpillar.forward(caterpillar_speed)
        if caterpillar.distance(leaf) < 20:
            place_leaf()
            caterpillar_length = caterpillar_length + .5
            caterpillar.shapesize(1, caterpillar_length, 1)
            caterpillar_speed = caterpillar_speed + .1
            score = score + 1
            display_score(score)
        if outside_window():
            game_over()
            break

#functions of the decision tree
def outside_window():
    left_wall = -t.window_width()/2
    right_wall = t.window_width()/2
    top_wall = t.window_height()/2
    bottom_wall = -t.window_height()/2
    (x,y) = caterpillar.pos()
    outside =  x < left_wall or x > right_wall or  y < bottom_wall or y > top_wall
    return outside


def game_over():
    caterpillar.color('black')
    leaf.color('green')
    t.penup()
    t.hideturtle()
    t.write('YOU ARE DEAD!!!', align='center', font=('Futura', 30, 'normal'))



#other in game functions
def display_score(current_score):
    score_turtle.clear()
    score_turtle.penup()
    x = (t.window_width()/2) - 40
    y = (t.window_height()/2) - 60
    score_turtle.setpos(x,y)
    score_turtle.write(str(current_score), align='center', font=('Futura', 45, 'italic'))

#using random module here
def place_leaf():
    leaf.ht()
    leaf.setx(random.randint(-200,200))
    leaf.sety(random.randint(-200,200))
    leaf.showturtle()



# caterpiller direction/movement functions        
def move_up():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(90)

def move_down():
    if caterpillar.heading() == 0 or caterpillar.heading() == 180:
        caterpillar.setheading(270)

def move_left():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(180)

def move_right():
    if caterpillar.heading() == 90 or caterpillar.heading() == 270:
        caterpillar.setheading(0)
# keypress events
t.onkey(start_game, 'i')
t.onkey(move_up, 'w')
t.onkey(move_down, 's')
t.onkey(move_right, 'd')
t.onkey(move_left, 'a')
t.listen()

#___start the loop___
t.mainloop()

