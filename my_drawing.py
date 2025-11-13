import turtle

#print (turtle.position())

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

def partial_drawing(mistake):
    print(f'вызвана функция с mistake = {mistake}')
    if mistake == 0:
        draw_main_frame()
    if mistake == 1:
        draw_head()
    if mistake == 2:
        draw_body()
    if mistake == 3:
        draw_left_arm()
    if mistake == 4:
        draw_right_arm()
    if mistake == 5:
        draw_right_leg()
    if mistake == 6:
        draw_left_leg()

#turtle.mainloop()