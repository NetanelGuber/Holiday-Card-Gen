from turtle import *
from shapes import *
from random import randint, choice

def chrismas():
    hideturtle()

    speed(0)

    window = turtle.Screen()
    window.bgcolor("#69D9FF")

    num = 0
    a = 0
    b = 0
    
    # snow
    while num < 101:
        draw_circle(turtle, "white", a, b, 7)
        a = randint(-700, 700)
        b = randint(-500, 500)
        num += 1

    y = -100
    width = 300 # 240

    # stem
    draw_rectangle(turtle, "brown", -15, y - 40, 30, 40)

    # tree leaves
    while width > 20:
        width = width - randint(20, 30)
        height = randint(15, 35)
        x = 0 - width / 2
        draw_rectangle(turtle, "green", x, y, width, height)
        y = y + height

    # star on tree
    draw_star(turtle, "yellow", 4, y, 25)

    penup()
    color("red")
    goto(-100, -180)
    write("Merry Chrismas", font=("Arial", 20, "bold"))

    hideturtle()

def halloween():
    hideturtle()

    speed(0)

    window = turtle.Screen()
    window.bgcolor("black")

    num = 0
    a = 0
    b = 0

    # stars
    while num < 101:
        draw_star(turtle, "yellow", a, b, 7)
        a = randint(-700, 700)
        b = randint(-500, 500)
        num += 1


    # stem
    draw_rectangle(turtle, "green", -30, 0, 50, 275)

    # pumpkin
    draw_circle(turtle, "orange", 0, -125, 150)
    draw_circle(turtle, "orange", -65, -125, 150)
    draw_circle(turtle, "orange", 65, -125, 150)

    # nose
    draw_triangle(turtle, "black", -40, 0, 75)

    # eyes
    draw_triangle(turtle, "black", -115, 80, 75)
    draw_triangle(turtle, "black", 30, 80, 75)

    # mouth
    draw_rectangle(turtle, "black", -90, -75, 175, 30)
    draw_rectangle(turtle, "black", -90, -75, 25, 65)
    draw_rectangle(turtle, "black", 70, -75, 25, 65)

    # text
    penup()
    color("gray")
    goto(-125, -180)
    write("Happy Halloween", font=("Arial", 25, "bold"))

def new_year():
    hideturtle()

    speed(0)

    window = turtle.Screen()
    window.bgcolor("black")

    num = 0
    a = randint(-450, 450)
    b = randint(-1, 400)

    colors = ["blue", "yellow", "orange", "green", "red", "purple", "white", "pink"]
    chosen_color = choice(colors)

    # fireworks
    while num < 25:
        draw_star(turtle, chosen_color, a, b, 10)
        draw_rectangle(turtle, "white", a - 2, b - 45, 1, 35)
        a = randint(-450, 450)
        b = randint(-1, 400)
        chosen_color = choice(colors)
        num += 1

    # text
    penup()
    color("white")
    goto(-210, -180)
    write("Happy New Year", font=("Arial", 42, "bold"))

def birthday():
    hideturtle()

    speed(0)

    window = turtle.Screen()
    window.bgcolor("#69D9FF")

    num = 0
    num2 = 0
    a = randint(-450, 450)
    b = randint(-400, 400)

    colors = ["blue", "yellow", "orange", "green", "red", "purple", "white", "pink"]
    chosen_color = choice(colors)

    # stars
    while num < 50:
        draw_star(turtle, chosen_color, a, b, 10)
        a = randint(-450, 450)
        b = randint(-400, 400)
        chosen_color = choice(colors)
        num += 1

    # plate
    draw_rectangle(turtle, "white", -275, -205, 560, 25)

    # cake
    draw_round_rectangle(turtle, "#84563c", -250, -180, 530, 75, 10)
    draw_round_rectangle(turtle, "#F3E5AB", -225, -105, 475, 75, 10)
    draw_round_rectangle(turtle, "#84563c", -200, -30, 425, 75, 10)

    # candles
    red_fire = -182
    orange_fire = -177
    yellow_fire = -172

    candle = -165

    turtle.setheading(270)

    while num2 < 5:
        draw_rectangle(turtle, "white", candle, 120, 75, 15)
        draw_egg(turtle, "red", red_fire, 135, 25, 0)
        draw_egg(turtle, "orange", orange_fire, 130, 20, 0)
        draw_egg(turtle, "yellow", yellow_fire, 125, 15, 0)

        candle += 80

        red_fire += 80
        orange_fire += 80
        yellow_fire += 80

        num2 += 1

    turtle.setheading(0)

    penup()
    color("black")
    goto(-210, -275)
    write("Happy Birthday!", font=("Arial", 42, "bold"))
    

birthday()
input(" ")