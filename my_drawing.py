import turtle
import tkinter



class MainWindow:
    
    def __init__(self):
            self.window = tkinter.Tk()  #не работает
            self.canvas1 = tkinter.Canvas(self.window, width=600, height=600)
            self.canvas1.grid(column=1, row=1)

            self.message_text = tkinter.StringVar()
            self.message_box = tkinter.Label(self.window, textvariable = self.message_text)
            self.message_text.set('message box')
            self.message_box.grid(column=1, row=2)

            self.word_text = tkinter.StringVar()
            self.word_box = tkinter.Label(self.window, textvariable = self.word_text)
            self.word_text.set('word_box')
            self.word_box.grid(column=1, row=3)

            self.used_letters_text = tkinter.StringVar()
            self.used_letters_box = tkinter.Label(self.window, textvariable = self.used_letters_text)
            self.used_letters_text.set('used_letters_text')
            self.used_letters_box.grid(column=1, row=4)
   
            self.screen = turtle.TurtleScreen(self.canvas1)
            self.test_turtle = turtle.RawTurtle(self.screen)
            self.entry_window_text = tkinter.StringVar()
            self.entry_window = tkinter.Entry(self.window, textvariable = self.entry_window_text)
            self.entry_window.grid(column=1, row=5)

            
    def return_value(event, self):
        return self.entry_window_text
    
                
        
    #print (turtle.position())
class DrawingHangman:
    
    def __init__(self, turtle_instance):
        self.used_argument = set()
        self.turtle = turtle_instance        
        
    def draw_main_frame(self):
        self.turtle.teleport(0, -100)

        self.turtle.left(180)
        self.turtle.forward(50)
        self.turtle.teleport(0, -100)
        self.turtle.left(180)
        self.turtle.forward(50)
        self.turtle.teleport(15, -100)
        self.turtle.left(90)
        self.turtle.forward(250)
        self.turtle.left(90)
        self.turtle.forward(80)
        self.turtle.left(90)
        self.turtle.forward(25)

    def draw_head(self):
        self.turtle.right(90)
        self.turtle.circle(20)
        self.turtle.left(90)
        self.turtle.teleport(-65, 85)

    def draw_body(self):
        self.turtle.forward(90)
        print (self.turtle.position())
        self.turtle.teleport(-65, 55)
        self.turtle.right(125)
    

    def draw_left_arm(self):
        self.turtle.forward(50)
        self.turtle.teleport(-65, 55)
        self.turtle.right(110)

    def draw_right_arm(self):
        self.turtle.forward(50)
        self.turtle.teleport(-65, -5)
        self.turtle.left(55)
        self.turtle.right(160)

    def draw_right_leg(self):
        self.turtle.forward(55)
        self.turtle.teleport(-65, -5)
        self.turtle.left(160)
        self.turtle.left(160)

    def draw_left_leg(self):
        self.turtle.forward(55)
    
    
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

# test_window = MainWindow()

# test_drawing = DrawingHangman(test_window.test_turtle)
# test_drawing.partial_drawing(0)