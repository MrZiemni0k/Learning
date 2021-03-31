from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape('turtle')
screen = Screen()
screen.colormode(255)
def figure(distance,sides,degrees):
    print(sides,degrees)
    timmy.pencolor((random.randint(1,255)),
                   (random.randint(1,255)),
                   (random.randint(1,255)))
                   
    for _ in range(sides):
        timmy.forward(distance)
        timmy.right(180-degrees)

def random_colour():
    return timmy.pencolor((random.randint(1,255)),
                          (random.randint(1,255)),
                          (random.randint(1,255)))
def dash_line(distance,gap):

    total_distance = distance
    for _ in range(int(distance/2)%gap):
        timmy.forward(10)
        total_distance -= 10
        timmy.penup()
        timmy.forward(10)
        timmy.pendown()
        total_distance -= 10
    timmy.forward(total_distance)

def draw_figures():
    for x in range(3,9):
        
        figure(100,x,(180*(x-2))/x)

def random_walk(steps,distance):
    timmy.speed("fast")
    timmy.pensize(5)
    x = [0,90,180,270]
    for _ in range(steps):
        timmy.pencolor((random.randint(1,255)),
                (random.randint(1,255)),
                (random.randint(1,255)))
        timmy.setheading(random.choice(x))
        timmy.forward(distance)

def spirograph(distance,degree):

    for _ in range(int(360/degree)):
        print("jestem")
        random_colour()
        timmy.left(degree)
        timmy.circle(distance)
timmy.speed("fastest") 
spirograph(100,20)

screen.exitonclick()