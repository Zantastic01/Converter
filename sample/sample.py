import os
import random
import pygame

# Window
WIDTH = 1000
HEIGHT = 800
SIZE = (WIDTH, HEIGHT)
TITLE = "CONVERTER 900"

# Colors
GREEN = (0, 150, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
YELLOW = (255, 255, 200)
BLUE = (75, 200, 255)
GREY = (110, 112, 117)
GREYbLUE = (177, 185, 206)
RED = (237, 40, 40)
star_colors = [YELLOW, BLUE, RED, WHITE]

# Fonts
FONT1 = ("assets/fonts/homenuli_shadow/HomenuliShadow.ttf", 96)


def show_title_screen():
    title_text = FONT_XL.render("CONVERTER 900", 1, WHITE)
    screen.blit(title_text, [100, 200])
    

def get_unit():


    choice = input("Which unit would like you like to start with:   ")
    choice = int(choice)

    file = "len/" + file_names[choice]

    with open(file, 'r') as f:
            lines = f.read().splitlines()

    print(lines)

    category = lines[0]
    unit = random.choice(lines[1:])

    return get_unit



get_unit()

"""

def get_kilometers():
    kilometers = float(input("enter kilometers here: "))
    return kilometers

kilometers =  get_kilometers()
conv_dec = 0.621371
miles = int(kilometers * conv_dec)   
print(str(kilometers) + " kilometers is equal to " + str(miles) + "  miles ")

def get_miles():
    miles = float(input("enter miles here: "))
    return miles

miles = get_miles()
conv_dec = 1.60934
kilometers = int(miles * conv_dec)   
print(str(miles) + " miles is equal to " + str(kilometers) + " kilometers. ")
"""
