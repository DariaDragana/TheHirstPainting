# import colorgram

# rgb_colors = []
# colors = colorgram.extract('image.jpg', 30)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
from turtle import Turtle
from turtle import Screen

screen = Screen()
screen.colormode(255)

color_list = [(182, 65, 34), (213, 149, 97), (14, 24, 42), (239, 208, 94), (237, 62, 33), (157, 26, 19), (72, 29, 32),
              (84, 94, 115), (166, 141, 66), (67, 41, 35), (120, 32, 37), (183, 85, 94), (135, 152, 164), (49, 52, 127),
              (229, 175, 161), (165, 64, 70), (167, 141, 150), (98, 113, 112), (160, 168, 165), (189, 190, 196),
              (217, 174, 180), (15, 25, 24), (79, 70, 43), (183, 196, 189), (119, 121, 147), (248, 196, 4)]

t = Turtle()
t.pensize(10)
t.penup()
t.setpos(-200, -200)


def change_color():
    random_color = random.choice(color_list)
    return random_color


def new_position():
    x, y = t.position()
    t.sety(y + 50)
    t.setx(x + -500)


def movement(space, x):
    for _ in range(x):
        for pos in range(x):
            t.pencolor(change_color())
            t.dot()
            t.forward(space)
        t.teleport(new_position())


movement(50, 10)



screen.exitonclick()