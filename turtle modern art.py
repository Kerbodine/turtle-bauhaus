from turtle import *
import random
from tkinter import *
from math import sqrt

turtle = Turtle()

turtle.shape("arrow")
turtle.speed(0)
turtle.pensize(5)
colormode(255)

screen = Screen()

grid_width = 12
grid_height = 12
size = 40

# screen.setup(grid_width * size, grid_height * size)
turtle.penup()
turtle.goto((grid_width * size) / 2, (-grid_height * size) / 2)

tracer(0, 0)

# Inkscape scaling, 240% -> 400%
# Final resolution: 5120, 5120

# color_list = ["CornflowerBlue", "IndianRed", "gold", "SeaGreen"]
# color_list = ["LightSteelBlue", "CornflowerBlue", "RoyalBlue", "MediumBlue", "Navy"]
# color_list = [(30,54,83), (44,87,141), (82,161,153), (239,209,95), (216,89,59)]
color_list = [(255,159,28), (255,191,105), (255,255,255), (203,243,240), (46,196,182)]
# color_list = [(185,214,242), (6,26,64), (3,83,164), (0,109,170), (0,53,89)]
# color_list = [(255,255,255), (59,65,60), (157,181,178), (218,240,238), (148,209,190)]
# color_list = []
# for _ in range(5):
#     r = random.randint(1,255)
#     g = random.randint(1,255)
#     b = random.randint(1,255)
#     color_list.append((r,g,b))

functions_list = ["circle", "square", "diamond", "horizontal_bars", "vertical_bars", "square_grid", "semi", "triangle"]

list_of_shapes = []
for _ in range(100):
    list_of_shapes.append("a")

def draw_circle(circle_count):
    turtle.penup()
    turtle.forward(size / 2)
    turtle.setheading(90)
    turtle.forward(size / 2)
    for i in range(circle_count):
        color = random.choice(color_list)
        shape_size = (4 - i) * (size / 4)
        turtle.dot(shape_size, color)
    turtle.setheading(270)
    turtle.forward(size / 2)
    turtle.setheading(0)
    turtle.forward(size / 2)

def draw_square(square_count):
    turtle.penup()
    starting_cor = turtle.pos()
    for i in range(square_count):
        color = random.choice(color_list)
        turtle.color(color)

        turtle.goto(starting_cor)
        shape_size = (4 - i) * size / 4
        gutter = (size - shape_size) / 2
        turtle.forward(gutter)
        turtle.left(90)
        turtle.forward(gutter)
        turtle.right(90)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(shape_size)
            turtle.left(90)
        turtle.end_fill()
    turtle.goto(starting_cor)
    turtle.forward(size)

def draw_diamond(diamond_count):
    turtle.penup()
    starting_cor = turtle.pos()
    for i in range(diamond_count):
        color = random.choice(color_list)
        turtle.color(color)

        turtle.goto(starting_cor)
        turtle.setheading(0)
        turtle.forward(size / 2)
        turtle.left(90)
        turtle.forward(size / 2)
        turtle.left(90)
        shape_size = (4 - i) * size / 4
        gutter = (size - shape_size)
        line_length = sqrt(((shape_size / 2) ** 2) + ((shape_size / 2) ** 2))
        turtle.forward(shape_size / 2)
        turtle.right(135)
        turtle.begin_fill()
        for _ in range(4):
            turtle.forward(line_length)
            turtle.right(90)
        turtle.end_fill()
    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.forward(size)

def draw_horizontal_rect(divisions):
    turtle.penup()
    starting_cor = turtle.pos()
    division_width = size / divisions
    for i in range(divisions):
        color = random.choice(color_list)
        turtle.color(color)

        turtle.goto(starting_cor)
        turtle.forward((i + 1) * division_width)
        turtle.begin_fill()
        for _ in range(2):
            turtle.left(90)
            turtle.forward(size)
            turtle.left(90)
            turtle.forward(division_width)
        turtle.end_fill()
    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.forward(size)

def draw_vertical_rect(divisions):
    turtle.penup()
    division_width = size / divisions
    starting_cor = turtle.pos()
    for i in range(divisions):
        color = random.choice(color_list)
        turtle.color(color)

        turtle.goto(starting_cor)
        turtle.left(90)
        turtle.forward((i + 1) * division_width)
        turtle.begin_fill()
        for _ in range(2):
            turtle.right(90)
            turtle.forward(size)
            turtle.right(90)
            turtle.forward(division_width)
        turtle.end_fill()
        turtle.setheading(0)
    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.forward(size)

def draw_square_grid():
    turtle.penup()
    starting_cor = turtle.pos()

    def draw_square_split():
        for _ in range(4):
            turtle.right(90)
            turtle.forward(size / 2)

    for i in range(4):
        color = random.choice(color_list)
        turtle.color(color)

        if i + 1 == 1:
            turtle.left(90)
            turtle.forward(size / 2)
        elif i + 1 == 2:
            turtle.left(90)
            turtle.forward(size)
        elif i + 1 == 3:
            turtle.forward(size / 2)
            turtle.left(90)
            turtle.forward(size / 2)
        elif i + 1 == 4:
            turtle.forward(size / 2)
            turtle.left(90)
            turtle.forward(size)
        
        turtle.begin_fill()
        draw_square_split()
        turtle.end_fill()
        turtle.goto(starting_cor)
        turtle.setheading(0)
    turtle.forward(size)

def draw_horizontal_semicircle():
    turtle.penup()
    starting_cor = turtle.pos()

    color1, color2 = 0,0
    while color1 == color2:
        color1 = random.choice(color_list)
        color2 = random.choice(color_list)

    turtle.color(color1)
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.circle(size / 2, 180)
    turtle.end_fill()

    turtle.color(color2)
    turtle.begin_fill()
    turtle.circle(size / 2, 180)
    turtle.left(90)
    turtle.forward(size)
    turtle.end_fill()

    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.forward(size)

def draw_vertical_semicircle():
    turtle.penup()
    starting_cor = turtle.pos()

    color1, color2 = 0,0
    while color1 == color2:
        color1 = random.choice(color_list)
        color2 = random.choice(color_list)

    turtle.color(color1)
    turtle.begin_fill()
    turtle.forward(size / 2)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(90)
    turtle.circle(size / 2, 180)
    turtle.end_fill()

    turtle.color(color2)
    turtle.begin_fill()
    turtle.circle(size / 2, 180)
    turtle.left(90)
    turtle.forward(size)
    turtle.end_fill()

    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.forward(size)

def draw_triangle_left():
    turtle.penup()
    starting_cor = turtle.pos()

    color1, color2 = 0,0
    while color1 == color2:
        color1 = random.choice(color_list)
        color2 = random.choice(color_list)

    turtle.color(color1)
    turtle.left(90)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.right(90)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(sqrt((size ** 2) + (size ** 2)))
    turtle.end_fill()

    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.color(color2)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(135)
    turtle.forward(sqrt((size ** 2) + (size ** 2)))
    turtle.end_fill()

    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.forward(size)

def draw_triangle_right():
    turtle.penup()
    starting_cor = turtle.pos()

    color1, color2 = 0,0
    while color1 == color2:
        color1 = random.choice(color_list)
        color2 = random.choice(color_list)

    turtle.color(color1)
    turtle.begin_fill()
    turtle.left(90)
    turtle.forward(size)
    turtle.right(135)
    turtle.forward(sqrt((size ** 2) + (size ** 2)))
    turtle.right(135)
    turtle.forward(size)
    turtle.end_fill()

    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.color(color2)
    turtle.forward(size)
    turtle.left(90)
    turtle.begin_fill()
    turtle.forward(size)
    turtle.left(90)
    turtle.forward(size)
    turtle.left(135)
    turtle.forward(sqrt((size ** 2) + (size ** 2)))
    turtle.end_fill()

    turtle.goto(starting_cor)
    turtle.setheading(0)
    turtle.forward(size)

pattern_list = []
for i in range(grid_width * grid_height):
    pattern_list.append(random.choice(functions_list))

turtle.penup()
turtle.hideturtle()

for i in range(grid_width * grid_height):
    if i % grid_width == 0:
        turtle.forward(size)
        turtle.left(90)
        turtle.forward(size)
        turtle.left(90)
        turtle.forward((grid_width + 1) * size)
        turtle.left(180)
    division = random.randint(1,4)
    if pattern_list[i] == "circle":
        draw_circle(division)
    elif pattern_list[i] == "square":
        draw_square(division)
    elif pattern_list[i] == "diamond":
        draw_diamond(division)
    elif pattern_list[i] == "horizontal_bars":
        draw_horizontal_rect(division)
    elif pattern_list[i] == "vertical_bars":
        draw_vertical_rect(division)
    elif pattern_list[i] == "square_grid":
        draw_square_grid()
    elif pattern_list[i] == "semi":
        option = random.randint(0,1)
        if option == 0:
            draw_horizontal_semicircle()
        else:
            draw_vertical_semicircle()

    elif pattern_list[i] == "triangle":
        option = random.randint(0,1)
        if option == 0:
            draw_triangle_left()
        else:
            draw_triangle_right()

update()

ts = turtle.getscreen()
ts.getcanvas().postscript(file="art.eps")

screen.exitonclick()
