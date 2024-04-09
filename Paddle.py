from turtle import Turtle
class Paddle(Turtle):
    def  __init__(self,xcor,ycor):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.color("white")
        self.penup()
        self.goto(xcor,ycor)
        # self.speed("fastest")
    def move_up(self):
        new_y = self.ycor() + 20  # Increase the y-coordinate by 20
        self.goto(self.xcor(), new_y)  # Move the turtle to the new position
    
    def move_down(self):
        new_y = self.ycor() - 20  # Decrease the y-coordinate by 20
        self.goto(self.xcor(), new_y)  # Move the turtle to the new position


        
            
    
        
        