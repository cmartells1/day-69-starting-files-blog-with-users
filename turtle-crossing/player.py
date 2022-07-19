from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.player_start()
        #self.y_move = MOVE_DISTANCE


    def player_start(self):
        self.shape("turtle")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):
        # new_y = self.ycor() + self.y_move
        # self.sety(new_y)
        self.forward(MOVE_DISTANCE)

    def reached_finish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False