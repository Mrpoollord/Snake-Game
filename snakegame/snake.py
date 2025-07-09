from turtle import Turtle, Screen
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE =20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.asghars = []
        self.creating_snake()
        self.head = self.asghars[0]

    def creating_snake(self):
        for position in STARTING_POSITION:
            self.add_asghar(position)

    def add_asghar(self, position):
        asghar = Turtle("square")
        asghar.color("white")
        asghar.penup()
        asghar.goto(position)
        self.asghars.append(asghar)

    def extend(self):
        self.add_asghar(self.asghars[-1].pos())

    def move(self):
        for asg_num in range(len(self.asghars) - 1, 0, -1):
            new_x = self.asghars[asg_num - 1].xcor()
            new_y = self.asghars[asg_num - 1].ycor()
            self.asghars[asg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
