from karel.stanfordkarel import *

"""
Makes Karel repair all the walls in any world
Pre: Karel starts at the 1st row and 1st column, facing east
Post: Karel ends at the last row and the last column, facing east
Fencepost error is solved by repeating "repair wall" command
"""
def main():
    for i in range(3):
        repair_wall()
        move_to_the_wall()
    repair_wall()

"""Karel repairs the wall and going back to his initial position"""

def repair_wall():
        turn_left()
        while front_is_clear():
            if beepers_present():
                move()
            else:
                put_beeper()
        if front_is_blocked():
            if no_beepers_present():
                put_beeper()
        go_back()

"""Brining Karel back to the ground"""

def go_back():
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()

"""Karel moves to the next wall"""

def move_to_the_wall():
    for i in range(4):
        move()

# There is no need to edit code beyond this point

if __name__ == "__main__":
    run_karel_program()
