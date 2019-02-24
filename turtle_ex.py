#1
def hello():
    print("Hello world")
hello()
hello()
hello()    
#2
x = int(input("X = "))
y = int(input("Y = "))
def add(x ,y):
    print(x+y)
#3
from turtle import*
def draw_square(length,color):
    for i in range(4):
        speed(5)
        pencolor(color)
        forward(length)
        left(90)
draw_square(200,"blue")   
mainloop()   
#4
from turtle import *
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()
#5
def draw_star(x,y,length):
    import turtle
    t=turtle.Turtle()
    t.penup()
    t.goto(x,y)
    t.pendown()
    for i in range(5):
        t.left(144)
        t.forward(length)
    
draw_star(0,45,200)
#6
from turtle import *
speed(0)
color('blue')
for i in range(10):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(30, 100)
    draw_star(x, y, length)