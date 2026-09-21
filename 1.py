import turtle
import colorsys

screen=turtle.Screen()
screen.bgcolor("black")
screen.title("heart mandala")
screen.tracer(5)
t=turtle.Turtle()
t.hideturtle()
t.speed(0)

def draw_heart(size):
    start_pos=t.pos()
    t.pendown()
    t.left(50)
    t.forward(size)
    t.circle(size*0.375,200)
    t.right(140)
    t.circle(size*0.375,200)
    t.forward(size)
    t.penup()
    t.goto(start_pos)

centre_y=-40
t.penup()
t.width(1.5)

