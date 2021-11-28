from turtle import Turtle

Starting_postions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE=20
UP=90
DOWN=270
RIGHT=0
LEFT=180
class Snake:

   def __init__(self):
       self.segment=[]
       self.creat_snake()
       self.head=self.segment[0]

   def creat_snake(self):
        for postion in Starting_postions:
          self.add_segment(postion)
   def add_segment(self,postion):
       new_segment = Turtle(shape="square")
       new_segment.color("White")
       new_segment.penup()
       new_segment.goto(postion)
       self.segment.append(new_segment)

   def extend(self):
       self.add_segment(self.segment[-1].position())
   def move(self):
        for seg_num in range(len( self.segment) - 1, 0, -1):
           new_x = self.segment[seg_num - 1].xcor()
           new_y = self.segment[seg_num - 1].ycor()
           self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)
   def up (self):
     if self.head.heading()!=DOWN:
          self.head.setheading(UP)

   def down(self):
      if self.head.heading()!=UP:
        self.head.setheading(DOWN)
   def right(self):
       if self.head.heading ()!=LEFT:
         self.head.setheading(RIGHT)
   def left(self):
       if self.head.heading() !=RIGHT:
           self.head.setheading(LEFT)