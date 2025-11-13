import turtle

#print (turtle.position())
class DrawingHangman:
    def __init__(self):
        self.used_argument = set()

    def draw_main_frame(self):
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

    def draw_head(self):
        turtle.right(90)
        turtle.circle(20)
        turtle.left(90)
        turtle.teleport(-65, 85)

    def draw_body(self):
        turtle.forward(90)
        print (turtle.position())
        turtle.teleport(-65, 55)
        turtle.right(125)
    

    def draw_left_arm(self):
        turtle.forward(50)
        turtle.teleport(-65, 55)
        turtle.right(110)

    def draw_right_arm(self):
        turtle.forward(50)
        turtle.teleport(-65, -5)
        turtle.left(55)
        turtle.right(160)

    def draw_right_leg(self):
        turtle.forward(55)
        turtle.teleport(-65, -5)
        turtle.left(160)
        turtle.left(160)

    def draw_left_leg(self):
        turtle.forward(55)
    
    
    def partial_drawing(self, mistake):
        print(self.used_argument)
        print(f'вызвана функция с mistake = {mistake}')
        if mistake not in self.used_argument:
            self.used_argument.add(mistake)
            if mistake == 0:
                self.draw_main_frame()
            if mistake == 1:
                self.draw_head()
            if mistake == 2:
                self.draw_body()
            if mistake == 3:
                self.draw_left_arm()
            if mistake == 4:
                self.draw_right_arm()
            if mistake == 5:
                self.draw_right_leg()
            if mistake == 6:
                self.draw_left_leg()
