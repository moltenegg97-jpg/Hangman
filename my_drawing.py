import turtle

print (turtle.position())

def draw_main_frame():
    turtle.teleport(0, -100)

    turtle.left(180)
    turtle.forward(50)
    turtle.teleport(0, -100)
    turtle.left(180)
    turtle.forward(50)
    turtle.teleport(15, -100)
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.forward(80)
    turtle.left(90)
    turtle.forward(25)

def draw_head():
    turtle.right(90)
    turtle.circle(20)
    turtle.left(90)
    turtle.teleport(-65, 85)

def draw_body():
    turtle.forward(90)
    print (turtle.position())
    turtle.teleport(-65, 55)
    turtle.right(125)
    

def draw_left_arm():
    turtle.forward(50)
    turtle.teleport(-65, 55)
    turtle.right(110)

def draw_right_arm():
    turtle.forward(50)
    turtle.teleport(-65, -5)
    turtle.left(55)
    turtle.right(160)

def draw_right_leg():
    turtle.forward(55)
    turtle.teleport(-65, -5)
    turtle.left(160)
    turtle.left(160)

def draw_left_leg():
    turtle.forward(55)

draw_main_frame()
draw_head()
draw_body()
draw_left_arm()
draw_right_arm()
draw_right_leg()
draw_left_leg()

turtle.mainloop()