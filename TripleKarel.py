from karel.stanfordkarel import *
"""Paints all 3 houses in any world
Pre: Karel starts facing west at the upper right corner of the leftmost building
Post: Karel finished painting all 3 houses and facing west past left corner of 
the rightmost building"""

def main ():
    for i in range(3):
        paint_house()

""" Karel paints 3 walls of the house and moves to the next house if there is one"""

def paint_house():
    for i in range(2):
        paint_one_wall()
        turn_left()
        move()
    paint_one_wall()
    if front_is_blocked():
        turn_right()

""" Makes Karel move to the end of the wall, dropping a beeper before each step it takes"""
def paint_one_wall():
    while left_is_blocked():
        put_beeper()
        move()

def turn_right():
    for i in range (3):
        turn_left()


# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
